class ProxyManager:
    def __init__(self, proxy_file):
        self.proxy_file = proxy_file

    async def get_proxies_list(self):
        with open(self.proxy_file, "r") as file:
            proxies_list = [line.strip() for line in file]
        return proxies_list