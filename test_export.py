import csv
import io
import unittest

from export import export


class ExportTest(unittest.TestCase):
    def test_empty_export_includes_header(self):
        self.assertEqual(list(csv.reader(io.StringIO(export([])))), [["id", "name"]])

    def test_nonempty_export_preserves_header_and_rows(self):
        rows = [[7, "Dupont, Alice"], [8, "Martin"]]
        self.assertEqual(list(csv.reader(io.StringIO(export(rows)))),
                         [["id", "name"], ["7", "Dupont, Alice"], ["8", "Martin"]])
