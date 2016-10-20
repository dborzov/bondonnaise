import csv, re

class BondCSV:
    def __init__(self, filepath):
        self.fd = csv.DictReader(open(filepath,'rb')).__iter__()

    def __iter__(self):
        return self

    def next(self):
        bond = self.fd.next()
        assert 'term' in bond
        bond["term_f"] = unmarshall("([\.\d+]+) years*", bond["term"])
        assert bond["term_f"] > 0
        assert 'yield' in bond
        bond["yield_f"] = unmarshall("([\.\d+]+)\%", bond["yield"])
        return bond


def unmarshall(regex, value):
    m = re.search(regex,value)
    if m is None:
        raise Error("Unsupported BondCSV Format")
    return float(m.group(1))
