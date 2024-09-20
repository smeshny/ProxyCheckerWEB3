import random

# Constants
RPCS = [
    "https://base.drpc.org",
    "https://rpc.blast.io",
    "https://rpc.scroll.io",
    "https://eth.llamarpc.com"
]

PROXY_FILE = "data/proxies.txt"
RESULTS_DIR = "data/results/"

# Sleep times
SLEEP_TIME_BETWEEN_RPCS = random.randint(1, 2)
SLEEP_TIME_BETWEEN_ACCOUNTS = random.randint(5, 10)
