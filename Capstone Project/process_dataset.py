import json

# Read JSON data from file
with open('data.json', 'r') as file:
    data = json.load(file)

# Process JSON data
for language_pair, language_data in data.items():
    print(f"Language Pair: {language_pair}")
    for data_type, data_entries in language_data.items():
        print(f"  Data Type: {data_type}")
        for entry_id, entry_data in data_entries.items():
            source = entry_data["source"]
            target = entry_data["target"]
            print(f"    Entry ID: {entry_id}")
            print(f"      Source: {source}")
            print(f"      Target: {target}")
            print(f"      Data Type: {data_type}")  # Print whether it's Train or Validation