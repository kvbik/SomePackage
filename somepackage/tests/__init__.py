# implement a basic test under somepackage.tests
import unittest
import somepackage

class TestSomething(unittest.TestCase):
    def test_something_else(self):
        self.assertEqual(True, somepackage.return_what_you_get())

    def test_something_else_again(self):
        self.assertEqual(128, somepackage.return_what_you_get(128))
        
def get_suite():
    "Return a unittest.TestSuite."
    import somepackage.tests
    
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(somepackage.tests)
    return suite

