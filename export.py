"""Baseline CSV exporter for the factory pilot."""
import csv
import io


def export(rows):
    # Use newline="" so csv can handle line endings itself.
    output = io.StringIO(newline="")
    writer = csv.writer(output)
    writer.writerow(["id", "name"])
    if rows:
        writer.writerows(rows)
    return output.getvalue()
