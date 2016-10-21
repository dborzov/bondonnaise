import csv, re
from collections import defaultdict

class BondCSV:
    def __init__(self, filepath):
        self.fd = csv.DictReader(open(filepath,'rb')).__iter__()

    def __iter__(self):
        return self

    def next(self):
        bond = self.fd.next()
        assert 'term' in bond
        bond["term_f"] = _unmarshall("([\.\d+]+) years*", bond["term"])
        assert bond["term_f"] > 0
        assert 'yield' in bond
        assert bond['type'] in ['government', 'corporate']
        bond["yield_f"] = _unmarshall("([\.\d+]+)\%", bond["yield"])
        return bond


def load_bond_csv(filepath):
    bonds_gov = defaultdict(list); bonds_corp = []
    for bond in BondCSV(filepath):
        if bond['type']=='government':
            bonds_gov[bond['term_f']].append(bond)
        elif bond['type']=='corporate':
            bonds_corp.append(bond)
    return bonds_gov, bonds_corp

def _unmarshall(regex, value):
    m = re.search(regex,value)
    if m is None:
        raise Error("Unsupported BondCSV Format")
    return float(m.group(1))
