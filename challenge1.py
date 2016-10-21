from bondspread import load_bond_csv, closest

def identify_benchmarks(bonds_gov, bonds_corp):
    gov_terms = sorted(bonds_gov.keys())
    if len(gov_terms)==0:
        raise Error('No government bonds loaded')
    for cb in bonds_corp:
        closest_term = closest(gov_terms, cb['term_f'])
        cb['benchmark'] = bonds_gov[closest_term][0]
        cb['spread_to_benchmark'] = cb['yield_f'] - cb['benchmark']['yield_f']
    return bonds_corp

bonds_gov, bonds_corp = load_bond_csv('problem/sample_input.csv')
bonds_corp = identify_benchmarks(bonds_gov, bonds_corp)

with open('challenge1.csv','wb') as ch1:
    ch1.write('bond,benchmark,spread_to_benchmark\n')
    for bc in bonds_corp:
        p = {
            "bond": bc['bond'],
            "benchmark": bc['benchmark']['bond'],
            "spread_to_benchmark": bc['spread_to_benchmark']
        }
        ch1.write("{bond},{benchmark},{spread_to_benchmark}%\n".format(**p))
