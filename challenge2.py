from bondspread import load_bond_csv, bounds, interpolate

def interpolate_spread(bonds_gov, bonds_corp):
    gov_terms = sorted(bonds_gov.keys())
    function = lambda point: sum(map(lambda v: v['yield_f'],bonds_gov[point]))/len(bonds_gov[point])
    for cb in bonds_corp:
        low, high = bounds(gov_terms, cb['term_f'])
        cb['curve_f'] = interpolate(gov_terms[low], gov_terms[high], function, cb['term_f'])
        cb['spread_to_curve'] = cb['yield_f'] - cb['curve_f']
    return bonds_corp


bonds_gov, bonds_corp = load_bond_csv('problem/sample_input.csv')
bonds_corp = interpolate_spread(bonds_gov, bonds_corp)

with open('challenge2.csv','wb') as ch1:
    ch1.write('bond,curve, spread_to_curve\n')
    for bc in bonds_corp:
        p = {
            "bond": bc['bond'],
            "spread_to_curve": bc['spread_to_curve'],
        }
        ch1.write("{bond},{spread_to_curve}%\n".format(**p))
