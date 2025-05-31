#!/usr/bin/env python3

#import re, io
import argparse, sys

parser = argparse.ArgumentParser(
    prog="pgb",
    description='''
    Parse GeneBank records''',
    epilog="M.Hryc (2025)"
)
parser.add_argument(
    "-i", "--input",
    required=True,
    type=str,
    help='''
Path to input file'''
)
parser.add_argument(
    "-r", "--record",
    type=int, default=0,
    help='''
Index (0 based) of the record to print'''
)
parser.add_argument(
    "-f", "--field",
    type=str, default="origin",
    help='''
Pick which field of the record to show, options: locus, definition, accession,
version, keywords, source, organism, comment, features, origin'''
)

def split_records(infile: str) -> [str]:
    gb_file = []
    with open(infile, 'r') as f:
        record = []
        for line in f:
            if not (line == "//\n" or line == "//"):
                record.append(line)
            else:
                gb_file.append(''.join(record))
                record.clear()

    return gb_file

def parse_source(inlist):
    return
def parse_origin(inlist):
    parsed_list = []
    for line in inlist:
        parsed_list.append(line.translate(str.maketrans('', '', " 0123456789")))

    return ''.join(parsed_list)

def parse_record(inrecord: str):
    record_structure = {
        "LOCUS": [],
        "DEFINITION": [],
        "ACCESSION": [],
        "VERSION": [],
        "KEYWORDS": [],
        "SOURCE": [],
        "ORGANISM": [],
        "REFERENCE": [],
        "COMMENT": [],
        "FEATURES": [],
        "ORIGIN": []
    }
    keys, record = [key for key in record_structure.keys()], inrecord.split('\n')

    key_idx = 0
    for line in record:
        try:
            if keys[key_idx + 1] in line:
                key_idx += 1
                #print(keys[key_idx])
        except IndexError:
            pass

        record_structure[keys[key_idx]]\
            .append(
                line.replace(keys[key_idx], "").strip()
            )
    record_structure["LOCUS"] = record_structure["LOCUS"][0]
    record_structure["DEFINITION"] = ''.join(record_structure["DEFINITION"])
    record_structure["ACCESSION"] = record_structure["ACCESSION"][0]
    record_structure["VERSION"] = ''.join(record_structure["VERSION"])
    record_structure["KEYWORDS"] = ''.join(record_structure["KEYWORDS"])
    record_structure["SOURCE"] = record_structure["SOURCE"][0] + '\n'
    record_structure["ORGANISM"] = ''.join(record_structure["ORGANISM"]) + '\n'
#    record_structure["REFERENCE"] =
    record_structure["COMMENT"] = ''.join([line + '\n' for line in record_structure["COMMENT"]])
    record_structure["FEATURES"] = ''.join([line + '\n' for line in record_structure["FEATURES"]])
    record_structure["ORIGIN"] = parse_origin(record_structure["ORIGIN"])

    return record_structure

if __name__ == "__main__":
    args = parser.parse_args()
    args.field = args.field.upper()

    gb_records = split_records(args.input)
    sys.stdout.write(
        parse_record(gb_records[args.record])[args.field]
    )
