import collections

from langdetect.lang_detect_exception import LangDetectException
from tqdm import tqdm

from umlsparser.UMLSParser import UMLSParser
from langdetect import detect

umls = UMLSParser('/home/toberhauser/DEV/Data/UMLS/2019AA-full/2019AA', language_filter=['GER'])
# beer = umls.get_concepts()['C0004922']
# print(beer.cui, beer.get_preferred_names_for_language('GER'), beer.get_preferred_names_for_language('ENG'))


language_counter = collections.defaultdict(collections.Counter)

def langdetect_thread(definition: str):
    try:
        lang = detect(definition)
    except LangDetectException:
        lang = 'ERROR'
    language_counter[source].update({lang: 1})


for cui, concept in tqdm(list(umls.get_concepts().items())[:1000]):
    for definition, source in concept.get_definitions():
        if len(definition) > 0:
            langdetect_thread(definition)
            # thread = threading.Thread(target=langdetect_thread, args=(definition,))
            # threads.append(thread)
            # thread.start()

# [x.join() for x in threads]

for source, languages in language_counter.items():
    print(source, languages)
