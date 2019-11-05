import collections
import logging
import threading

from langdetect.lang_detect_exception import LangDetectException
from tqdm import tqdm

from UMLSParser import UMLSParser
from langdetect import detect

umls = UMLSParser('/home/toberhauser/DEV/Data/UMLS/2019AA-full/2019AA', language_filter=['SPA', 'GER'])

language_counter = collections.defaultdict(collections.Counter)


def langdetect_thread(definition: str):
    try:
        lang = detect(definition)
    except LangDetectException:
        lang = 'ERROR'
    language_counter[source].update({lang: 1})


for cui, concept in tqdm(umls.get_concepts().items()):
    for definition, source in concept.get_definitions():
        if len(definition) > 0:
            langdetect_thread(definition)

for source, languages in language_counter.items():
    print(source, languages)
