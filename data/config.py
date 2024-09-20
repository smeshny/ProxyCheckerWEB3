import random

# Constants
RPCS = [
    # ETH
    "https://eth.llamarpc.com",
    # "https://eth.drpc.org",
    # SCROLL
    "https://rpc.scroll.io",
    # "https://rpc.ankr.com/scroll",
    # "https://scroll.drpc.org",
    # BASE
    # "https://rpc.ankr.com/base",
    "https://base.drpc.org",
    # "https://base.llamarpc.com",
    # BLAST
    "https://rpc.blast.io",
    # "https://rpc.envelop.is/blast",
    # "https://blast-rpc.publicnode.com",
]

PROXY_FILE = "data/proxies.xlsx"
RESULTS_DIR = "data/results/"

# Sleep times
SLEEP_TIME_BETWEEN_RPCS = random.randint(1, 2)
SLEEP_TIME_BETWEEN_ACCOUNTS = random.randint(5, 10)


SAVE_TABLE = True  # Option to save the results table
CHECK_INTERVAL = 10  # Interval in seconds to re-run the check
