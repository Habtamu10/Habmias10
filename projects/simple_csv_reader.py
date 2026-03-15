# Simple CSV Reader/Writer
import csv
import io

def write_csv(data, headers):
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()

def read_csv(csv_string):
    reader = csv.DictReader(io.StringIO(csv_string))
    return list(reader)

def filter_rows(data, key, value):
    return [row for row in data if row.get(key) == value]

# Demo
students = [
    {"name": "Habtamu", "grade": "A", "score": "95"},
    {"name": "Alice",   "grade": "B", "score": "82"},
    {"name": "Bob",     "grade": "A", "score": "91"},
    {"name": "Carol",   "grade": "C", "score": "74"},
]

csv_data = write_csv(students, ["name", "grade", "score"])
print("CSV output:")
print(csv_data)

parsed = read_csv(csv_data)
grade_a = filter_rows(parsed, "grade", "A")
print("Grade A students:", [s["name"] for s in grade_a])
