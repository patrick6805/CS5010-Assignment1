"""CSV-driven tests for the input parsing functions in main.py.

Run from the directory containing main.py and this test file:
    python test_parsing.py

The test cases are loaded from parsing_test_cases.csv. Each case may provide
multiple inputs so invalid entries can be followed by a valid entry.
"""

import csv
import contextlib
import importlib
import io
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

CASES_FILE = Path(__file__).with_name("parsing_test_cases.csv")


class ParsingFunctionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Imports main.py as a module. Keep main.py in the same project folder.
        cls.app = importlib.import_module("main")
        with CASES_FILE.open("r", newline="", encoding="utf-8") as file:
            cls.cases = list(csv.DictReader(file))

    def test_csv_cases(self):
        for case in self.cases:
            with self.subTest(
                case_id=case["case_id"],
                function=case["function"],
                description=case["description"],
            ):
                function = getattr(self.app, case["function"])
                inputs = json.loads(case["inputs_json"])
                expected = json.loads(case["expected_return_json"])
                expected_message = case["expected_output_contains"]

                captured_output = io.StringIO()
                with patch("builtins.input", side_effect=inputs), \
                     contextlib.redirect_stdout(captured_output):
                    actual = function()

                self.assertEqual(actual, expected)
                if expected_message:
                    self.assertIn(expected_message, captured_output.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
