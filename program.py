import json

file_path = 'data.json'

with open(file_path, 'r') as file:
    data = json.load(file)

filtered_records = [record for record in data['Root']['data']['record'] if record['field'][3]]

print(filtered_records)

filtered_json_file_path = 'filtered_data.json'

filtered_json_data = json.dumps(filtered_records, indent=2)

with open(filtered_json_file_path, 'w') as file:
    file.write(filtered_json_data)

print("Filtered data saved to:", filtered_json_file_path)