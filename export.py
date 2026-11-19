"""Baseline CSV exporter for the factory pilot."""
import csv
import io


def export(rows):
    output = io.StringIO(newline="")
    writer = csv.writer(output)
    if rows:
        writer.writerow(["id", "name"])
        writer.writerows(rows)
    return output.getvalue()
