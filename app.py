from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from datetime import datetime
import os

app = Flask(__name__)

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

DATA_FILE = "data/entries.json"

def load_entries():
    """Load journal entries from JSON file"""
    try:
        with open(DATA_FILE, 'r') as file:
            content = file.read().strip()
            if not content:  # File is empty
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        # If JSON is malformed, return empty list
        return []

def save_entries(entries):
    """Save journal entries to JSON file"""
    with open(DATA_FILE, 'w') as file:
        json.dump(entries, file, indent=4)

@app.route('/')
def index():
    """Main page showing all journal entries"""
    entries = load_entries()
    return render_template('index.html', entries=entries)

@app.route('/add_entry', methods=['POST'])
def add_entry():
    """Add a new journal entry"""
    content = request.form.get('content', '').strip()
    if content:
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "content": content
        }
        entries = load_entries()
        entries.append(entry)
        save_entries(entries)
    return redirect(url_for('index'))

@app.route('/api/entries')
def get_entries():
    """API endpoint to get all entries as JSON"""
    entries = load_entries()
    return jsonify(entries)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000) 