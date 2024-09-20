import logging

# ANSI escape codes for colors
GREEN = "\033[92m"
RESET = "\033[0m"

class Logger:
    @staticmethod
    def configure_logging():
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    @staticmethod
    def log_info(message, color=None):
        if color:
            message = f"{color}{message}{RESET}"
        logging.info(message)

    @staticmethod
    def log_error(message):
        logging.error(message)