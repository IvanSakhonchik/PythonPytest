import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(pastime)s - %(name)s - %(levelness)s - %(message)s',
                    filename='log.log',
                    filemode='w')