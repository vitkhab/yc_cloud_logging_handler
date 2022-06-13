import yandexcloud
from pyclm.logging import Logger
import logging

class YandexCloudLoggingHandler(logging.Handler):

    def __init__(self, log_group_id, resource_id, request_id, function_version):
        logging.Handler.__init__(self)

        self.request_id = request_id
        self.function_version = function_version

        self.logger = Logger(
            sdk=yandexcloud.SDK(),
            log_group_id=log_group_id,
            resource_type="serverless.function",
            resource_id=resource_id,
            elements=1,
            period=0
        )
    
        self.loggers = {
            "TRACE": self.logger.trace,
            "DEBUG": self.logger.debug,
            "INFO": self.logger.info,
            "WARN": self.logger.warn,
            "ERROR": self.logger.error,
            "FATAL": self.logger.fatal
        }

    def emit(self, record):
        msg = self.format(record)

        if record.levelname in self.loggers:
            self.loggers[record.levelname](
                msg,
                request_id=self.request_id,
                version_id=self.function_version
            )
        else:
            self.loggers["DEBUG"](
                msg,
                request_id=self.request_id,
                version_id=self.function_version
            )
