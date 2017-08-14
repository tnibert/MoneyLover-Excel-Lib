import unittest
import dataframes

class TestDataframe(unittest.TestCase):

    def test_fileToDataframe(self):
        self.testdf = dataframes.fileToDataframe("sample.xlsx")

    def test_dataframeToFile(self):
        test = dataframes.dataframeToFile(self.testdf, "dftofiletest.xlsx")
        assert test == 1

    def test_dataframeTomlRow(self):
        dataframes.dataframeTomlRow(self.testdf)

    def test_mlRowToDataframe(self):
        pass

if __name__ == '__main__':
    unittest.main()
