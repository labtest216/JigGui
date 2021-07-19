import logging
import time
import tkinter as tk

from mats import Test


# Create example tests to put into the Gui.


class Test1_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test1_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test1_example running .... socket_id={self._socket_id}')
            logging.info(f'Test1_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test1_example running .... socket_id={self._socket_id}')
            logging.error(f'Test1_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test2_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test2_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=True):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test1_example running .... socket_id={self._socket_id}')
            logging.info(f'Test1_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test1_example running .... socket_id={self._socket_id}')
            logging.error(f'Test1_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class NfcStickerCheck(Test):

    def __init__(self, socket_id, func):
        super().__init__(moniker='NFC Sticker Check', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=True):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        """Jump Popup Windows that asking operator if he put sticker then operator click ok..."""
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test1_example running .... socket_id={self._socket_id}')
            logging.info(f'Test1_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test1_example running .... socket_id={self._socket_id}')
            logging.error(f'Test1_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test3_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test3_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test3_example running .... socket_id={self._socket_id}')
            logging.info(f'Test3_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test3_example running .... socket_id={self._socket_id}')
            logging.error(f'Test3_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test4_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test4_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test4_example running .... socket_id={self._socket_id}')
            logging.info(f'Test4_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test4_example running .... socket_id={self._socket_id}')
            logging.error(f'Test4_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test5_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test5_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test5_example running .... socket_id={self._socket_id}')
            logging.info(f'Test5_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test5_example running .... socket_id={self._socket_id}')
            logging.error(f'Test5_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test6_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test6_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test6_example running .... socket_id={self._socket_id}')
            logging.info(f'Test6_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test6_example running .... socket_id={self._socket_id}')
            logging.error(f'Test6_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test7_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test7_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test7_example running .... socket_id={self._socket_id}')
            logging.info(f'Test7_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test7_example running .... socket_id={self._socket_id}')
            logging.error(f'Test7_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test8_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test8_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test8_example running .... socket_id={self._socket_id}')
            logging.info(f'Test8_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test8_example running .... socket_id={self._socket_id}')
            logging.error(f'Test8_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test9_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test9_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test9_example running .... socket_id={self._socket_id}')
            logging.info(f'Test9_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test9_example running .... socket_id={self._socket_id}')
            logging.error(f'Test9_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test10_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test10_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test10_example running .... socket_id={self._socket_id}')
            logging.info(f'Test10_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test10_example running .... socket_id={self._socket_id}')
            logging.error(f'Test10_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test11_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test11_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test11_example running .... socket_id={self._socket_id}')
            logging.info(f'Test11_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test11_example running .... socket_id={self._socket_id}')
            logging.error(f'Test11_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test12_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test12_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test12_example running .... socket_id={self._socket_id}')
            logging.info(f'Test12_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test12_example running .... socket_id={self._socket_id}')
            logging.error(f'Test12_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test13_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test13_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test13_example running .... socket_id={self._socket_id}')
            logging.info(f'Test13_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test13_example running .... socket_id={self._socket_id}')
            logging.error(f'Test13_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test14_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test14_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test14_example running .... socket_id={self._socket_id}')
            logging.info(f'Test14_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test14_example running .... socket_id={self._socket_id}')
            logging.error(f'Test14_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test15_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test15_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test15_example running .... socket_id={self._socket_id}')
            logging.info(f'Test15_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test15_example running .... socket_id={self._socket_id}')
            logging.error(f'Test15_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test16_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test16_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test16_example running .... socket_id={self._socket_id}')
            logging.info(f'Test16_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test16_example running .... socket_id={self._socket_id}')
            logging.error(f'Test16_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test17_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test17_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test17_example running .... socket_id={self._socket_id}')
            logging.info(f'Test17_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test17_example running .... socket_id={self._socket_id}')
            logging.error(f'Test17_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test18_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test18_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test18_example running .... socket_id={self._socket_id}')
            logging.info(f'Test18_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test18_example running .... socket_id={self._socket_id}')
            logging.error(f'Test18_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test19_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test19_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test19_example running .... socket_id={self._socket_id}')
            logging.info(f'Test19_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test19_example running .... socket_id={self._socket_id}')
            logging.error(f'Test19_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test20_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test20_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test20_example running .... socket_id={self._socket_id}')
            logging.info(f'Test20_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test20_example running .... socket_id={self._socket_id}')
            logging.error(f'Test20_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test21_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test21_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test21_example running .... socket_id={self._socket_id}')
            logging.info(f'Test21_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test21_example running .... socket_id={self._socket_id}')
            logging.error(f'Test21_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test22_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test22_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test22_example running .... socket_id={self._socket_id}')
            logging.info(f'Test22_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test22_example running .... socket_id={self._socket_id}')
            logging.error(f'Test22_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test23_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test23_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test23_example running .... socket_id={self._socket_id}')
            logging.info(f'Test23_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test23_example running .... socket_id={self._socket_id}')
            logging.error(f'Test23_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test24_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test24_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test24_example running .... socket_id={self._socket_id}')
            logging.info(f'Test24_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test24_example running .... socket_id={self._socket_id}')
            logging.error(f'Test24_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test25_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test25_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test25_example running .... socket_id={self._socket_id}')
            logging.info(f'Test25_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test25_example running .... socket_id={self._socket_id}')
            logging.error(f'Test25_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test26_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test26_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test26_example running .... socket_id={self._socket_id}')
            logging.info(f'Test26_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test26_example running .... socket_id={self._socket_id}')
            logging.error(f'Test26_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test27_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test27_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test27_example running .... socket_id={self._socket_id}')
            logging.info(f'Test27_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test27_example running .... socket_id={self._socket_id}')
            logging.error(f'Test27_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test28_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test28_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test28_example running .... socket_id={self._socket_id}')
            logging.info(f'Test28_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test28_example running .... socket_id={self._socket_id}')
            logging.error(f'Test28_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test29_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test29_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test29_example running .... socket_id={self._socket_id}')
            logging.info(f'Test29_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test29_example running .... socket_id={self._socket_id}')
            logging.error(f'Test29_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test30_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test30_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test30_example running .... socket_id={self._socket_id}')
            logging.info(f'Test30_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test30_example running .... socket_id={self._socket_id}')
            logging.error(f'Test30_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test31_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test31_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test31_example running .... socket_id={self._socket_id}')
            logging.info(f'Test31_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test31_example running .... socket_id={self._socket_id}')
            logging.error(f'Test31_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")


class Test32_example(Test):

    def __init__(self, socket_id):
        super().__init__(moniker='Test32_example', pass_if=True)
        self._socket_id = socket_id

    def setup(self, is_passing=False):
        logging.info(f"Setup socket{self._socket_id}")

    def execute(self, is_passing):
        logging.debug(f"execute socket{self._socket_id}")
        i = 0
        while i < 4:
            logging.debug(f'Test32_example running .... socket_id={self._socket_id}')
            logging.info(f'Test32_example running .... socket_id={self._socket_id}')
            logging.warning(f'Test32_example running .... socket_id={self._socket_id}')
            logging.error(f'Test32_example running .... socket_id={self._socket_id}')
            time.sleep(1)
            i += 1

    def teardown(self, is_passing):
        logging.warning(f"teardown socket{self._socket_id}")
