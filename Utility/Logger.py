import logging

class Logger:

    @staticmethod
    def get_Logger():

        logger = logging.getLogger()
        file = logging.FileHandler("D:\\Rupali Prathamesh Pandit\\CredCart2\\Logs\\CredCartLogs.log")
        format = logging.Formatter(" %(asctime)s : %(funcName)s : %(lineno)s : %(levelno)s : %(message)s ")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger