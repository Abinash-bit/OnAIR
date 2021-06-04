import unittest
import sys 

from src.test.test_driver import TestDriver
from src.test.data_handling.parsers.test_parser_util import TestParserUtil
from src.test.data_handling.parsers.test_forty_two_parser import TestFortyTwoParser
from src.test.data_handling.parsers.test_generic_parser import TestGenericParser
from src.test.data_handling.test_time_synchronizer import TestTimeSynchronizer
from src.test.data_handling.test_data_source import TestDataSource
from src.test.run_scripts.test_execution_engine import TestExecutionEngine
from src.test.systems.test_spacecraft import TestSpacecraft
from src.test.systems.test_status import TestStatus
from src.test.reasoning.test_brain import TestBrain
from src.test.systems.test_telemetry_test_suite import TestTelemetryTestSuite
# from src.test.run_scripts.test_sim import TestSimulator

test_dict = {'driver' : 0,
             'execution_engine' : 1}

def create_suite():
    suite = []
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestDriver))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestParserUtil))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestFortyTwoParser))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestGenericParser))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestTimeSynchronizer))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestDataSource))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestExecutionEngine))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestSpacecraft))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestStatus))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestBrain))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestTelemetryTestSuite))
    # suite.append(unittest.TestLoader().loadTestsFromTestCase(TestSimulator))
    

    return suite

def run_tests(suite):
    for test in suite:
        unittest.TextTestRunner(verbosity=1).run(test)

def test_individual_suite(test):
    unittest.TextTestRunner(verbosity=1).run(test) 

if __name__ == '__main__':
    suite = create_suite()
    if len(sys.argv) == 2:
        try: 
            test_individual_suite(suite[int(sys.argv[1])])
        except: 
            print('Please enter a valid test index')
    else:
        run_tests(suite)
