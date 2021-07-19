from mats import TestSequence, ArchiveManager
from Tests.example_tests import *
from global_config import num_of_sockets


# Define the precycle function to log info before the test is run.
def pre_cycle():
    logging.info("Pre Cycle")


# Define the postcycle function to log info after the test is run.
def post_cycle():
    logging.info("Post Cycle")


# Init ArchiveManger.
archive1 = ArchiveManager()

# Define each sequence in a dictionary and put the tests as the value for each sequence.
seq_dict = {"sequence1": [Test1_example('1'), Test2_example('1'), Test3_example('1'), Test4_example('1'),
                          Test5_example('1'), Test6_example('1'), Test7_example('1'), Test8_example('1'),
                          Test9_example('1'), Test10_example('1'), Test11_example('1'), Test12_example('1'),
                          Test13_example('1'), Test14_example('1'), Test15_example('1'), Test16_example('1'),
                          Test17_example('1'), Test18_example('1'), Test19_example('1'), Test20_example('1'),
                          Test21_example('1'), Test22_example('1'), Test23_example('1'), Test24_example('1'),
                          Test25_example('1'), Test26_example('1'), Test27_example('1'), Test28_example('1'),
                          Test29_example('1'), Test30_example('1'), Test31_example('1'), Test32_example('1')],
            "sequence2": [Test1_example('2'), Test2_example('2'), Test3_example('2'), Test4_example('2'),
                          Test5_example('2'), Test6_example('2'), Test7_example('2'), Test8_example('2'),
                          Test9_example('2'), Test10_example('2'), Test11_example('2'), Test12_example('2'),
                          Test13_example('2'), Test14_example('2'), Test15_example('2'), Test16_example('2'),
                          Test17_example('2'), Test18_example('2'), Test19_example('2'), Test20_example('2'),
                          Test21_example('2'), Test22_example('2'), Test23_example('2'), Test24_example('2'),
                          Test25_example('2'), Test26_example('2'), Test27_example('2'), Test28_example('2'),
                          Test29_example('2'), Test30_example('2'), Test31_example('2'), Test32_example('2')],
            "sequence3": [Test1_example('3'), Test2_example('3'), Test3_example('3'), Test4_example('3'),
                          Test5_example('3'), Test6_example('3'), Test7_example('3'), Test8_example('3'),
                          Test9_example('3'), Test10_example('3'), Test11_example('3'), Test12_example('3'),
                          Test13_example('3'), Test14_example('3'), Test15_example('3'), Test16_example('3'),
                          Test17_example('3'), Test18_example('3'), Test19_example('3'), Test20_example('3'),
                          Test21_example('3'), Test22_example('3'), Test23_example('3'), Test24_example('3'),
                          Test25_example('3'), Test26_example('3'), Test27_example('3'), Test28_example('3'),
                          Test29_example('3'), Test30_example('3'), Test31_example('3'), Test32_example('3')]}

# If we need a different sequence for each test don't use a for loop but still use the seq_dict to store each sequence.
# for num in range(num_of_sockets):
#     seq_dict["sequence{0}".format(num + 1)] = [Test1_example(), Test2_example()]


# Create a dictionary to hold each test sequence and put each test sequence with different sequences in the dictionary.
ts_dict = {}
for num in range(num_of_sockets):
    ts_dict["ts{0}".format(num+1)] = TestSequence(
                                    sequence=seq_dict["sequence{0}".format(num+1)],
                                    setup=lambda: pre_cycle(),
                                    teardown=lambda: post_cycle(),
                                    archive_manager=archive1
                                  )
