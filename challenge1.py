import csv, re

def unmarshall(regex, value):
    m = re.search(regex,value)
    if m is None:
        raise Error("Unsupported BondCSV Format")
    return float(m.group(1))


with open('problem/sample_input.csv') as csvfile:
    for bond in csv.DictReader(csvfile):
        assert 'term' in bond
        m = re.search("([\.\d+]+) years*",bond["term"])
        if m is None:
            raise Error("Unsupported BondCSV Format")
        bond["term_f"] = unmarshall("([\.\d+]+) years*", bond["term"])
        assert bond["term_f"] > 0
        bond["yield_f"] = unmarshall("([\.\d+]+)\%", bond["yield"])
        print bond
