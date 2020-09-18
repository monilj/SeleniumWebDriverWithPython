import logging
import LoggingInfrastructure.GenericCustomLoggerUtility as cl


class LoggingUsingGenericMethod:
    log = cl.customLogger(logging.DEBUG)

    def method1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):
        m2Log = cl.customLogger(logging.INFO)
        m2Log.debug('debug message')
        m2Log.info('info message')
        m2Log.warning('warn message')
        m2Log.error('error message')
        m2Log.critical('critical message')

    def method3(self):
        m3Log = cl.customLogger(logging.INFO)
        m3Log.debug('debug message')
        m3Log.info('info message')
        m3Log.warning('warn message')
        m3Log.error('error message')
        m3Log.critical('critical message')


loggingUsingGenericMethod = LoggingUsingGenericMethod()
loggingUsingGenericMethod.method1()
loggingUsingGenericMethod.method2()
loggingUsingGenericMethod.method3()