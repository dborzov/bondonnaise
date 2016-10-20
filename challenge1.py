from bondspread import BondCSV, closest
from collections import defaultdict

bonds_gov = defaultdict(list); bonds_corp = []
for bond in BondCSV('problem/sample_input.csv'):
    if bond['type']=='government':
        bonds_gov[bond['term_f']].append(bond)
    elif bond['type']=='corporate':
        bonds_corp.append(bond)

gov_terms = sorted(bonds_gov.keys())
print "Government terms: ", gov_terms
for each in bonds_corp:
    closest_term = closest(gov_terms, each['term_f'])
    print 'For {}({}) the closest val is {}'.format(each['bond'], each['term_f'], gov_terms[closest_term])
