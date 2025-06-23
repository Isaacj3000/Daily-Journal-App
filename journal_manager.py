import json 
from datetime import datetime

DATA_FILE = "journal.json"

def create_entry(content):
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "content": content
    }
 
    try:
        with open(DATA_FILE, "r") as file:
            entries = json.load(file)
    except FileNotFoundError:
        entries = []

    entries.append(entry)
    with open(DATA_FILE, "w") as f:
        json.dump(entries, f, indent=4)
    print("Entry created successfully")
