import logging
import os
import sys


DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def is_debug_mode():
    get_trace = getattr(sys, 'gettrace', lambda : None)
    return get_trace() is not None


class Logger:
    def __init__(self, name: str, stream: bool = True):
        self.name = name
        self.log_level = logging.DEBUG if is_debug_mode() else logging.INFO

        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.log_level)

        if not os.path.isdir('logs'):
            os.mkdir('logs')

        self.handler = logging.FileHandler(filename = os.path.join('logs', f'{name}.log'),
                                           encoding = 'utf-8', mode = 'w')
        self.formatter = logging.Formatter('{asctime} [{levelname}]: {name}: {message}', DATETIME_FORMAT, style = '{')

        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

        if stream:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(self.formatter)
            self.logger.addHandler(stream_handler)
