import unittest
from selenium import webdriver

class TestDemo1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='path/to/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_example(self):
        self.driver.get("http://www.example.com")
        self.assertIn("Example Domain", self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()