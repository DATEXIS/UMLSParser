import collections
import csv
from typing import DefaultDict

import numpy as np
import pandas as pd
from tqdm import tqdm

from umlsparser import UMLSParser
from umlsparser.model.Concept import Concept

#
# umls = UMLSParser("/home/toberhauser/DEV/Data/UMLS/2019AA-full/2019AA", language_filter=['ENG'])
# # target_cui = 'C0004922' # BEER
# # target_cui = 'C0072973' # RAMIPRIL
# # target_cui = 'C0039231'  # TACHYCARDIA
# data = []
# for line in tqdm(open("/home/toberhauser/DEV/Data/UMLS/2019AA-full/2019AA/META/MRREL.RRF")):
#     line = line.split('|')
#     cui1 = line[0]
#     cui2 = line[4]
#     rel = line[3]
#     rela = line[7]
#     rui = line[8]
#     if '' not in [cui1, cui2] and cui1 != cui2 and rel == 'RO' and rela != '':
#         data.append({'cui1': cui1,
#                      'name1': str(umls.get_concepts().get(cui1)),
#                      'cui2': cui2,
#                      'name2': str(umls.get_concepts().get(cui2)),
#                      'rel': rel,
#                      'rela': rela,
#                      'rui': rui
#                      })
# df = pd.DataFrame(data)
# dk = df.groupby(['cui1', 'cui2', 'name1', 'name2', 'rel', 'rela'])
# with open('umls_ro_relations.csv', 'w', newline='') as csvfile:
#     csvfile.write(pd.DataFrame.to_csv(dk.first(), quoting=csv.QUOTE_NONNUMERIC))

with open('umls_ro_relations.csv', 'r') as csvfile:
    relas = collections.defaultdict(int)
    for line in tqdm(csv.DictReader(csvfile)):
        relas[line['rela']] += 1

    print(sorted(relas.items(), key=lambda x: x[1], reverse=True))
