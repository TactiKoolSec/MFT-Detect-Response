#!/usr/bin/env python3
import argparse
import csv
from datetime import date
from uuid import uuid4

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog = "Template2Detect",
                    description = "Convert template files to detection rules")
    parser.add_argument("-f", "--file", default="", required=True, help="Single file to convert")
    parser.add_argument("-c", "--csv", default="", required=True, help="CSV file to read from")
    parser.add_argument("-o", "--output", help="File to output to. If not provided, outputs to stdout")
    args = parser.parse_args()


    with open(args.file) as handle:
        data = handle.read()

    pairs = {"DATE": str(date.today()), "GUID": str(uuid4())}
    with open(args.csv) as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            #print(row)
            pairs[row['Key']] = row['Value' ]
    for k,v in pairs.items():
        data = data.replace(f"{{{k}}}", v)
        #print({k},v)
    if args.output:
        with open(args.output, "w") as handle:
            handle.write(data)
    else:
        print(data)





