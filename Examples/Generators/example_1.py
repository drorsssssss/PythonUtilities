import logging
import time,datetime

log_level="debug"

conf_log_level = getattr(logging,log_level.upper())


logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                    level=conf_log_level,handlers=[logging.FileHandler('example.log'),logging.StreamHandler()])

def test_gen():
    logging.info("annnnnn")

    while True:
        yield "dror"

        for i in range(1,3):
            yield i

        yield "end"
        logging.info("annnnnn")
        logging.debug("annnnnn")


for i in test_gen():
    print(i)
