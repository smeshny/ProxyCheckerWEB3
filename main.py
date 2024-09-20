import asyncio
from src.rpc_checker import RPCChecker
from src.proxy_manager import ProxyManager
from src.result_processor import ResultProcessor
from utils.logger import Logger
from utils.logger import GREEN, RESET
from data.config import RPCS, PROXY_FILE, SLEEP_TIME_BETWEEN_ACCOUNTS, SAVE_TABLE, CHECK_INTERVAL

async def check_proxies():
    Logger.configure_logging()

    proxy_manager = ProxyManager(PROXY_FILE)
    rpc_checker = RPCChecker(RPCS)
    result_processor = ResultProcessor()

    proxies_list = await proxy_manager.get_proxies_list()
    combined_results = []
    total_proxies = len(proxies_list)
    working_proxies = 0

    for index, (proxy_name, proxy) in enumerate(proxies_list):
        results = await rpc_checker.check_all_rpcs(proxy_name, proxy)

        working_rpcs = sum(1 for result in results if result["status"] != "error")
        total_rpcs = len(results)
        remaining_proxies = total_proxies - (index + 1)
        Logger.log_info(f"Proxy: {proxy_name} ({proxy}), Working RPCs: {working_rpcs}/{total_rpcs}, Remaining Proxies: {remaining_proxies}", color=GREEN)

        if working_rpcs > 0:
            working_proxies += 1

        combined_results.append({"proxy_name": proxy_name, "proxy": proxy, "rpcs": results})

        await asyncio.sleep(SLEEP_TIME_BETWEEN_ACCOUNTS)

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