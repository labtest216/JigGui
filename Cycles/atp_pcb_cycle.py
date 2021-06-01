import logging
from mats import TestSequence, ArchiveManager
from Tests.atp_pcb_test1 import Test1_example
from Tests.atp_pcb_test2 import Test2_example

def pre_cycle():
    logging.info("Pre Cycle")


def post_cycle():
    logging.info("Post Cycle")


sequence1 = [Test1_example(), Test2_example()]
ts1 = TestSequence(
    sequence=sequence1,
    setup=lambda: pre_cycle(),
    teardown=lambda: post_cycle(),
)

ts1.start()