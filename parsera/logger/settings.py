import logging


class MegaHandler(logging.Handler):
    def __init__(self, filename):
        logging.Handler.__init__(self)
        self.filename = filename


    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        with open(self.filename, 'a') as f:
            f.write(msg + '\n')



logger_config = {
    'version': 1,
    'disable_existing_loggers': False, # чтобы остальные логеры тоже работали
    'formatters': {
        'std_format': {
            'format': '[* {levelname} *] - {asctime} - Message: "{message}". Logger: "{name} - {module}:{funcName}:{lineno}"',
            'style': '{'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format'
        },
        'file': {
            '()': MegaHandler,
            'level': 'DEBUG',
            'filename': '_log.log',
            'formatter': 'std_format',
        }
    },
    'loggers': {
        'asynchronous_logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            # 'propagate': False
        }
    },

    # 'filters': {},
    # 'root': {}, # '': {} # Корневой логер
    # 'incremental': True # это дополнительный конфиг к тому что где то есть ещё
}
