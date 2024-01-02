import json
import re

def transform_string(input_string):
    # Use regular expression to find patterns like "City of [CityName]"
    pattern = r"City of (\w+)"
    match = re.search(pattern, input_string)
    if match:
        city_name = match.group(1)
        transformed_string = f"{city_name} City"
        return transformed_string
    else:
        return input_string

input_file_path = 'townships.geojson'
output_file_path = 'townships2.geojson'

with open(input_file_path, 'r') as file:
    data = json.load(file)

# Find and modify the LABEL object
for feature in data['features']:
    if 'properties' in feature and 'LABEL' in feature['properties']:
        label = feature['properties']['LABEL']
        transformed_label = transform_string(label)
        feature['properties']['LABEL'] = transformed_label

# Save the modified GeoJSON to a new file
with open(output_file_path, 'w') as file:
    json.dump(data, file, indent=2)

print("New file '{}' has been created with the modified LABEL object.".format(output_file_path))
