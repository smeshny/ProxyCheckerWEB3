import pandas as pd
from pathlib import Path
from utils.better_proxy import Proxy

class ProxyManager:
    def __init__(self, proxy_file):
        self.proxy_file = proxy_file

    async def get_proxies_list(self):
        file_extension = Path(self.proxy_file).suffix.lower()
        
        if file_extension == '.xlsx':
            df = pd.read_excel(self.proxy_file, header=None, skiprows=1)
        elif file_extension == '.txt':
            df = pd.read_csv(self.proxy_file, sep=' ', header=None, skiprows=1)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")

        proxies = list(df.dropna().itertuples(index=False, name=None))
        
        processed_proxies = []
        for name, proxy in proxies:
            prossed_proxy = Proxy.from_str(proxy)
            prossed_proxy = prossed_proxy.as_login_pass_host_port
            processed_proxies.append([name, prossed_proxy])
        
        return processed_proxies