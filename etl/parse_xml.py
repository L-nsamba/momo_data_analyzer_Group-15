import xml.etree.ElementTree as ET
import json

# Loading and parsing the XML file
tree = ET.parse("data/raw/modified_sms_v2.xml")
root = tree.getroot()

#Storing the SMS records in a dictionary
sms_records = []
for sms in root.findall("sms"):
    record = {
        "address": sms.get("address"),
        "date": sms.get("readable_date"),
        "body": sms.get("body")
    }
    sms_records.append(record)

#Converting the data stored in the dictionary to json format
json_data = json.dumps(sms_records, indent=4)

#Creation of the json file to store the new data in json format
with open("data/processed/transactions", "w") as json_file:
    json_file.write(json_data)

print("Successfully converted XML --> JSON!")

