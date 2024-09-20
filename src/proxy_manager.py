import pandas as pd
from pathlib import Path

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
        
        return proxies