import logging
import time

from mats import Test

# Have all of the tests in one file or different files for each different types
# or bundles of tests with different and very specific names so that it will be
# easier to access and put each test in the sequence of tests.


class Test1_example(Test):

    def __init__(self,socket_id):
        super().__init__(moniker='Test1_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 30:
            logging.debug(f'Test1_example running .... socket_id={self._socket_id}')
            logging.info(f'Test1_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test1_example running .... socket_id={self._socket_id}')
            logging.error(f'Test1_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")



