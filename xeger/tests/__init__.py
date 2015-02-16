import unittest
import test_xeger

def suite():
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromModule(test_xeger))
    return suite
