import csv
import json
import sys
from risk_score_chartjs import generate_risk_score_chartjs

path = sys.argv[1]


def read_csv(csv_file, result_file):
    # Open the CSV file for reading
    with open(csv_file, mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)

        # Process each row in the CSV file
        for row in csv_reader:
            trait = row['trait']
            percentile = int(row['percentile'])

            # Create output JSON object
            output_data = {
                "values": {
                    "trait": trait,
                    "percentile": percentile
                },
                "chartjs": {
                    "risk_lv": generate_risk_score_chartjs(score=percentile, lang='lv'),
                    "risk_en": generate_risk_score_chartjs(score=percentile, lang='en'),
                },
            }

            with open(result_file, 'w') as json_file:
                json.dump(output_data, json_file, indent=4)

            break



# Example usage
csv_file = '/output/vcf/pgs_output.csv'  # Path to your CSV result file
result_file = '/output/output.json'  # Path to your JSOn result file
read_csv(path + csv_file, path + result_file)
