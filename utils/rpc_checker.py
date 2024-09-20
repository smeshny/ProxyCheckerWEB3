import asyncio
from web3 import Web3
from web3.providers.async_rpc import AsyncHTTPProvider
from data.config import SLEEP_TIME_BETWEEN_RPCS
from utils.logger import Logger

class RPCChecker:
    def __init__(self, rpcs):
        self.rpcs = rpcs

    async def check_rpc_with_proxy(self, rpc, proxy):
        await asyncio.sleep(SLEEP_TIME_BETWEEN_RPCS)
        try:
            provider = AsyncHTTPProvider(rpc, request_kwargs={"proxy": f"http://{proxy}"})
            w3 = Web3(provider)
            status = await w3.is_connected(show_traceback=True)
            Logger.log_info(f"Proxy: {proxy}, RPC: {rpc}, Status: {status}")
        except Exception as e:
            status = "error"
            Logger.log_error(f"Proxy: {proxy}, RPC: {rpc}, Error: {e}")
        return {"rpc": rpc, "status": status}

    async def check_all_rpcs(self, proxy):
        tasks = [asyncio.create_task(self.check_rpc_with_proxy(rpc, proxy)) for rpc in self.rpcs]
        results = await asyncio.gather(*tasks)
        return results