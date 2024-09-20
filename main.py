import asyncio
from utils.rpc_checker import RPCChecker
from utils.proxy_manager import ProxyManager
from utils.result_processor import ResultProcessor
from utils.logger import Logger
from utils.logger import GREEN, RESET
from data.config import RPCS, PROXY_FILE, SLEEP_TIME_BETWEEN_ACCOUNTS

async def main():
    Logger.configure_logging()

    proxy_manager = ProxyManager(PROXY_FILE)
    rpc_checker = RPCChecker(RPCS)
    result_processor = ResultProcessor()

    proxies_list = await proxy_manager.get_proxies_list()
    combined_results = []
    total_proxies = len(proxies_list)

    for index, proxy in enumerate(proxies_list):
        results = await rpc_checker.check_all_rpcs(proxy)

        working_rpcs = sum(1 for result in results if result["status"] != "error")
        total_rpcs = len(results)
        remaining_proxies = total_proxies - (index + 1)
        Logger.log_info(f"Proxy: {proxy}, Working RPCs: {working_rpcs}/{total_rpcs}, Remaining Proxies: {remaining_proxies}", color=GREEN)

        combined_results.append({"proxy": proxy, "rpcs": results})

        await asyncio.sleep(SLEEP_TIME_BETWEEN_ACCOUNTS)

    await result_processor.make_table_with_results(combined_results)

if __name__ == "__main__":
    asyncio.run(main())