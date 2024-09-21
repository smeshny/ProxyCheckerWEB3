import datetime
import os
import sys
from abc import ABC

from loguru import logger
from notifiers.logging import NotificationHandler

from data.config import TG_TOKEN, TG_ID, SEND_NOTIFICATIONS


class Logger(ABC):
    def __init__(self) -> None:
        self.logger = logger
        self.logger.remove()
        
        logger_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level><bold>{level: <8}</bold></level> | "
            "<level>{message}</level>"
        )
        self.logger.add(sys.stdout, format=logger_format)
        date = datetime.datetime.now().date()
        self.logger.add(
            f"./logs/{date}.log",
            rotation="100 MB",
            level="DEBUG",
            format=logger_format,
        )

        if SEND_NOTIFICATIONS:
            tg_handler = NotificationHandler(
                "telegram", defaults={"token": TG_TOKEN, "chat_id": TG_ID}
            )
            self.logger.add(tg_handler, level="SUCCESS", format=logger_format)

    def __getattr__(self, name):
        return getattr(self.logger, name)


logger = Logger()
