import unittest
from moneylover import *
from net import *


class jsontest(unittest.TestCase):
    def test(self):
        with open('tests/jsontest.json') as data_file:
            data = json.load(data_file)
        test, hdr = loadMLWorkbook("sample.xlsx")
        print(data)
        js = ls_to_json(test)
        print(js)
        # not sure why this is failing, will revisit later
        assert js == data

if __name__ == '__main__':
    unittest.main()
