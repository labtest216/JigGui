import time
import logging
from mats import Test


class Test2_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test2_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 30:
            logging.debug(f'Test2_example running .... socket_id={self._socket_id}')
            logging.info(f'Test2_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test2_example running .... socket_id={self._socket_id}')
            logging.error(f'Test2_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")



