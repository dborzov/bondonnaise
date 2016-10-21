from bondspread import load_bond_csv, bounds, interpolate

def interpolate_spread(bonds_gov, bonds_corp):
    gov_terms = sorted(bonds_gov.keys())
    function = lambda point: sum(map(lambda v: v['yield_f'],bonds_gov[point]))/len(bonds_gov[point])
    for cb in bonds_corp:
        low, high = bounds(gov_terms, cb['yield_f'])
        cb['spread_to_curve'] = interpolate(gov_terms[low], gov_terms[high], function, cb['yield_f'])
    return bonds_corp


bonds_gov, bonds_corp = load_bond_csv('problem/sample_input.csv')
bonds_corp = interpolate_spread(bonds_gov, bonds_corp)
print map(lambda x:x['yield_f'],bonds_corp)
