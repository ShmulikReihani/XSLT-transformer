import logging

'''
  Using logging library for define a logger for each class.
  Each class will have a file handler that shows all the logs of the program.
'''


class Logger:

    def __init__(self, file_name, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(file_name + '.log')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
