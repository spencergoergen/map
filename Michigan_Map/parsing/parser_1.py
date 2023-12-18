import json

def restructure_data(input_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
        text_lines = data['text']

        result = {}
        current_county = None
        current_twp = None
        twp_name = None

        for line in text_lines:
            print(f"Processing line: {line}")
            if line.endswith("COUNTY:"):  # If the line contains only "COUNTY" and ends with "County"
                county_name = line.replace(" COUNTY:", "")
                result[county_name] = {}
                current_county = county_name
                print(f"Current County: {current_county}")
            elif "Twp" in line and "SCH" not in line:
                twp_name = line
                result[current_county][twp_name] = []
                current_twp = twp_name
                print(f"Current TWP: {current_twp}")
            elif "City" in line and "SCH" not in line:
                city_name = line
                result[current_county][city_name] = []
                current_twp = city_name  # Treat City as Twp for the data structure
                print(f"at City")
            elif "SCH" in line or "COUNTY" or "PUB" in line:
                print(f"At school")
                parts = line.split()
                last_word = parts[-1]
                if last_word.replace('.', '', 1).isdigit():  # Checking if the last part is a number (rate)
                    rate = float(last_word)
                    school_name = ' '.join(parts[:-1]).strip()
                    if current_county in result and current_twp in result[current_county]:
                        if result[current_county][current_twp]:
                            if school_name in result[current_county][current_twp][-1].keys():
                                result[current_county][current_twp][-1][school_name]["Rate"] = str(rate)
                            else:
                                result[current_county][current_twp][-1][school_name] = {"Rate": str(rate)}
                        else:
                            result[current_county][current_twp].append({school_name: {"Rate": str(rate)}})
                    else:
                        result[current_county][current_twp] = [{school_name: {"Rate": str(rate)}}]

        return result

# Path to your input JSON file
input_json_path = 'parsing/output.json'

# Restructure the data
restructured_data = restructure_data(input_json_path)

# Path to save the cleaned JSON file
output_json_path = 'parsing/clean.json'

# Save the restructured data into clean.json
with open(output_json_path, 'w') as clean_file:
    json.dump(restructured_data, clean_file, indent=2)

print(f"Data saved to {output_json_path}")
