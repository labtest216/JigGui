import logging
from mats import Test


class Test1_example(Test):

    def __init__(self):
        super().__init__(moniker='Test1_example', pass_if=True)

    def execute(self, is_passing=True):
        logging.debug("Execute test1")
        logging.info("Test1 PASS")
        return True