
from Task_2.main import YaUploader
import unittest

class Test_create_a_folder(unittest.TestCase, YaUploader):
    res = YaUploader().create_a_folder("Palma")

    def test_res200(self):
        self.assertEqual(201, self.res)

    @unittest.expectedFailure
    def test_folderis_exist(self):
        self.assertEqual(409, self.res)