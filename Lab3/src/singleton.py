class Logger:
    _instance = None  # Private class variable to hold the single instance

    def __new__(cls):
        if cls._instance is None:
            print("Logger created exactly once")
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.init_logger()
        else:
            print("Logger already created")
        return cls._instance

    def init_logger(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)


def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
    for i in range(3):
        logger = Logger()
        logger.add_message(f"Adding message number: {i}")
        # print(logger.messages)


if __name__ == "__main__":
    main()


'''
How to make singleton thread-safe?
Ref: https://stackoverflow.com/questions/50566934/why-is-this-singleton-implementation-not-thread-safe

import threading

lock = threading.Lock()

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with lock:
                if cls not in cls._instances:
                    print("Logger created exactly once")
                    cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        else:
            print("Logger already created")
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)


def main():
    for i in range(3):
        logger = Logger()
        logger.add_message(f"Adding message number: {i}")
        print(logger.messages)


if __name__ == "__main__":
    main()

'''
