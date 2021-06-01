import logging
from mats import Test


class Test2_example(Test):

    def __init__(self):
        super().__init__(moniker='Test2_example')

    def execute(self):
        logging.debug("Execute test2")
        logging.error("Test2 FAIL")
        return False
