import unittest
from src.report_generator import generate_report
import os

class TestReportGenerator(unittest.TestCase):
    def test_generate_report(self):
        generate_report("TestProject", {"Stars": 100, "Forks": 50})
        self.assertTrue(os.path.exists("TestProject_report.pdf"))

if __name__ == "__main__":
    unittest.main()
