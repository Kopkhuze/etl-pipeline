import logging
import logging.config
import os.path

def log_config():
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'default_handler': {
                'class' 'logging.FileHandler',
                'level' 'DEBUG',
                'formatter': 'standard',
                'filename':os.path.join('logs','etl_pipeline.log'),

            },
        },
    }