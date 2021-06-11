import logging

class loggerconfig:

    def logging():
        logging.basicConfig(filename='DataStructures.log',level=logging.DEBUG)

if __name__=="__main__":
    logger = loggerconfig()
    logger.logging()