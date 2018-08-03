import logging
import inspect
from generic.path import *


def customLogger(withoutDate ,logLevel=logging.DEBUG ):
    # Take the name of the caller (class / method).
    loggerName = inspect.stack()[1][3]

    # Create a logger and pass the caller name to see who called.
    logger = logging.getLogger(loggerName)

    # Set ascent_logging level to DEBUG to log all msges.
    logger.setLevel(logging.DEBUG)

    # Create a file handler to create a log file same name as the caller and use mode(write to it or append to it)
    fileHandler = logging.FileHandler(LOG_PATH + "automation.log", mode='a')

    # Set ascent_logging level for writing in a file which is provided by the user
    fileHandler.setLevel(logLevel)

    if withoutDate:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%Y/%m/%d %H:%M:%S ')
        print('2')
    else:
        formatter = logging.Formatter('%(message)s')
        print('1')


    # Set the formatter to the file handler
    fileHandler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(fileHandler)

    print(logger)

    # Return the logger to the caller
    return logger



