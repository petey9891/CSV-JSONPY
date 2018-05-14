import csv
import json

"""
    Converts CSV file with two columns into JSON file with dictionary format
"""

def csv_to_json():

    # file = <input file>


    with open(file, "r") as csvfile:
        csv_list = []
        reader = csv.reader(csvfile, delimiter=",")

        for row in  reader:
            csv_list.append(row)
    csvfile.close()

    csv_list.pop(0)

    csv_dict = {}
    for row in csv_list:
        csv_dict[row[0]] = row[1]

    jsonfile = open("../resources/json_info.json", "w")

    json.dump(csv_dict, jsonfile, indent=4)

    jsonfile.close()

if __name__ == "__main__":
    csv_to_json()
