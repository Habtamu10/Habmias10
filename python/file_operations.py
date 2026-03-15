# Python File Operations
import os
import json
import tempfile

def write_json(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def read_json(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def append_line(filepath, line):
    with open(filepath, "a") as f:
        f.write(line + "\n")

def read_lines(filepath):
    with open(filepath, "r") as f:
        return [line.rstrip("\n") for line in f]

with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as tf:
    tmpname = tf.name

data = {"name": "Habtamu", "skills": ["Python", "JavaScript", "Java"]}
write_json(tmpname, data)
loaded = read_json(tmpname)
print("Read back:", loaded)
os.unlink(tmpname)
