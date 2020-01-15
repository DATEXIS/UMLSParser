import csv

from tqdm import tqdm

from umlsparser import UMLSParser
from umlsparser.model.Concept import Concept

umls = UMLSParser("/home/toberhauser/DEV/Data/UMLS/2019AA-full/2019AA", language_filter=['ENG'])
# target_cui = 'C0004922' # BEER
# target_cui = 'C0072973' # RAMIPRIL
target_cui = 'C0039231'  # TACHYCARDIA

with open('umls_ro_relations.csv', 'w', newline='') as csvfile:
    fieldnames = ['cui1', 'name1', 'cui2', 'name2', 'rel', 'rela', 'rui']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect=csv.unix_dialect)
    writer.writeheader()
    for line in tqdm(open("/home/toberhauser/DEV/Data/UMLS/2019AA-full/2019AA/META/MRREL.RRF")):
        line = line.split('|')
        cui1 = line[0]
        cui2 = line[4]
        rel = line[3]
        rela = line[7]
        rui = line[8]
        if '' not in [cui1, cui2] and cui1 != cui2 and rel == 'RO' and rela != '':
            writer.writerow({'cui1': cui1,
                             'name1': str(umls.get_concepts().get(cui1)),
                             'cui2': cui2,
                             'name2': str(umls.get_concepts().get(cui2)),
                             'rel': rel,
                             'rela': rela,
                             'rui': rui
                             })
