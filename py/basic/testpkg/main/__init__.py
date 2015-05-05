import requests
import sys
from testpkg.main.conf import CONFIG


def sample():
    env = CONFIG.ENVIRONMENT_NAME
    args = ' '.join(sys.argv[1:])
    print ("Running sample script in environment '{}'"
           ", with args: {}").format(env, args)


def run_tests():
    import unittest
    from types import ModuleType

    success = True
    if len(sys.argv) > 1:
        # assume any additional args are tests or test modules to be run
        test_suite = unittest.TestLoader().loadTestsFromNames(sys.argv[1:])

    else:
        # no args, just discover all the tests in our package automatically
        test_suite = unittest.TestLoader().discover('testpkg')

    result = unittest.TextTestRunner(verbosity=1).run(test_suite)
    success = result.wasSuccessful()

    if success:
        return 0

    return 1

