import configparser

config = configparser.RawConfigParser()
config.read("D:\\Rupali Prathamesh Pandit\\CredCart2\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getURL():
        url = config.get('common data' , 'url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password