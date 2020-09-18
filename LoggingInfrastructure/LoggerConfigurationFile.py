"""
Logger Demo
"""
import logging
import logging.config


class LoggerConfigurationFile:
    def test(self):
        # create logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerConfigurationFile.__name__)

        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')


loggerConfigurationFile = LoggerConfigurationFile()
loggerConfigurationFile.test()
