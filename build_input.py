import json
import csv
import sys

path = sys.argv[1]


def json_to_csv(base_directory):

    json_file = base_directory + "/input/input.json"
    csv_file = base_directory + "/input/input.csv"

    # Read the JSON data from the file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extract the required fields
    sex = data.get("field_sex", {}).get("value", "")
    trait = data.get("field_polygenic_risk_trait", {}).get("value", "")
    filename = data.get("field_genome_file", {}).get("filename", "")

    # Prepend the base directory to the filename
    genome_file = base_directory + filename

    # Create the CSV file and write the header and data
    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the header
        csv_writer.writerow(["sample", "trait", "genome_file", "sex"])
        # Write the data
        csv_writer.writerow(["XXX", trait, genome_file, sex])

json_to_csv(path)