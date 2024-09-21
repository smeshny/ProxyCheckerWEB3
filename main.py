import asyncio
from src.rpc_checker import RPCChecker
from src.proxy_manager import ProxyManager
from src.result_processor import ResultProcessor
from utils.logger import Logger
from utils.logger import GREEN, RESET
from data.config import RPCS, PROXY_FILE, SLEEP_TIME_BETWEEN_ACCOUNTS, SAVE_TABLE, CHECK_INTERVAL

async def process_proxy(index, proxy_name, proxy, rpc_checker, total_proxies):
    await asyncio.sleep(index * SLEEP_TIME_BETWEEN_ACCOUNTS)
    results = await rpc_checker.check_all_rpcs(proxy_name, proxy)

    working_rpcs = sum(1 for result in results if result["status"] != "error")
    total_rpcs = len(results)
    remaining_proxies = total_proxies - (index + 1)
    Logger.log_info(f"Proxy: {proxy_name} ({proxy}) "
                    f"Working RPCs: {working_rpcs}/{total_rpcs} "
                    f"Remaining Proxies: {remaining_proxies}")
    
    return (1 if working_rpcs > 0 else 0), {"proxy_name": proxy_name, "proxy": proxy, "rpcs": results}

async def check_proxies():
    Logger.configure_logging()

    proxy_manager = ProxyManager(PROXY_FILE)
    rpc_checker = RPCChecker(RPCS)
    result_processor = ResultProcessor()

    proxies_list = await proxy_manager.get_proxies_list()
    total_proxies = len(proxies_list)

    tasks = [process_proxy(index, proxy_name, proxy, rpc_checker, total_proxies)
             for index, (proxy_name, proxy) in enumerate(proxies_list)]

    # Limit concurrency to 5 tasks at a time (adjust as needed)
    results = await asyncio.gather(*tasks, return_exceptions=True)

    working_proxies = 0
    combined_results = []
    for result in results:
        if isinstance(result, Exception):
            Logger.log_error(f"Error processing proxy: {str(result)}")
        else:
            working_proxy, proxy_result = result
            working_proxies += working_proxy
            combined_results.append(proxy_result)

    if SAVE_TABLE:
        await result_processor.make_table_with_results(combined_results)

    return working_proxies, total_proxies

async def main():
    while True:
        working_proxies, total_proxies = await check_proxies()
        Logger.log_info(f"Working proxies: {working_proxies}/{total_proxies}", color=GREEN)
        Logger.log_info(f"Next check will start in {CHECK_INTERVAL} seconds.", color=GREEN)
        await asyncio.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    asyncio.run(main())