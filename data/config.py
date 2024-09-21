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
    # Berachain
    "https://bartio.rpc.berachain.com",
]

PROXY_FILE = "data/proxies.xlsx"
RESULTS_DIR = "data/results/"

SLEEP_TIME_BETWEEN_RPCS = [1, 3] # Sleep time between RPCs checks in seconds
SLEEP_TIME_BETWEEN_ACCOUNTS = [1, 5] # Sleep time between accounts checks in seconds
CHECK_INTERVAL = 6 * 60 * 60  # Interval in seconds to re-run the check of all proxies

SAVE_TABLE = True  # Option to save the results table, (!) every run -> new xlsx file (!)

SEND_NOTIFICATIONS = False
TG_TOKEN = '' # https://t.me/BotFather
TG_ID = '' # https://t.me/getmyid_bot