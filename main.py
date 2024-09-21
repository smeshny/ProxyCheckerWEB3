import asyncio
import random
from src.rpc_checker import RPCChecker
from src.proxy_manager import ProxyManager
from src.result_processor import ResultProcessor
from utils.custom_logger import logger
from data.config import RPCS, PROXY_FILE, SLEEP_TIME_BETWEEN_ACCOUNTS, SAVE_TABLE, CHECK_INTERVAL

async def check_proxy(index, proxy_name, proxy, rpc_checker, total_proxies):
    results = await rpc_checker.check_all_rpcs(proxy_name, proxy)

    working_rpcs = sum(1 for result in results if result["status"] != "error")
    total_rpcs = len(results)
    logger.debug(f"Proxy: {proxy_name} Working RPCs: {working_rpcs}/{total_rpcs}. Check finished!")
    
    return (1 if working_rpcs > 0 else 0), {"proxy_name": proxy_name, "proxy": proxy, "rpcs": results}

async def check_proxies():
    proxy_manager = ProxyManager(PROXY_FILE)
    rpc_checker = RPCChecker(RPCS)
    result_processor = ResultProcessor()

    proxies_list = await proxy_manager.get_proxies_list()
    total_proxies = len(proxies_list)
    logger.debug(f"Total proxies to check: {total_proxies}")

    proxy_tasks = []
    for index, (proxy_name, proxy) in enumerate(proxies_list):
        task = asyncio.create_task(check_proxy(index, proxy_name, proxy, rpc_checker, total_proxies))
        proxy_tasks.append(task)
        await asyncio.sleep(random.uniform(*SLEEP_TIME_BETWEEN_ACCOUNTS))

    results = await asyncio.gather(*proxy_tasks, return_exceptions=True)

    working_proxies = 0
    combined_results = []
    for result in results:
        if isinstance(result, Exception):
            logger.debug(f"Error processing proxy: {str(result)}")
        else:
            working_proxy, proxy_result = result
            working_proxies += working_proxy
            combined_results.append(proxy_result)

    if SAVE_TABLE:
        await result_processor.make_table_with_results(combined_results)

    return working_proxies, total_proxies, combined_results

async def main():
    while True:
        working_proxies, total_proxies, combined_results = await check_proxies()
        logger.success(f"🫡 Working proxies: {working_proxies}/{total_proxies}")

        non_working_proxies = [result["proxy_name"] 
                               for result in combined_results 
                               if all(rpc["status"] == "error" for rpc in result["rpcs"])]
        if non_working_proxies:
            logger.warning(f"🙀 Non-working proxies: {', '.join(non_working_proxies)}")

        logger.success(f"🫡 Next check will start in {CHECK_INTERVAL/60:.1f} minutes.")
        await asyncio.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    asyncio.run(main())