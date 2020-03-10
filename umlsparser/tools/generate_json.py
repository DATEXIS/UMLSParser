import json

from umlsparser.UMLSParser import UMLSParser

umls = UMLSParser('/home/devfoo/Dev/Data/UMLS/2019AA-full/2019AA/', language_filter=['ENG', 'GER'])

with open('umls.jsonlines', 'w') as outfile:
    for cui, concept in umls.get_concepts().items():
        output = {
            'cui': cui,
            'names':{
                'de': {
                    'preferred': list(concept.get_preferred_names_for_language('GER')),
                    'all': list(concept.get_names_for_language('GER'))
                },
                'en': {
                    'preferred': list(concept.get_preferred_names_for_language('ENG')),
                    'all': list(concept.get_names_for_language('ENG'))
                }
            },
            'definitions': list(concept.get_definitions()),
            'semantic_type': {
                'TUI': concept.get_tui(),
                'name': umls.get_semantic_types().get(concept.get_tui()).get_name()
            }
        }
        outfile.write(json.dumps(output) + '\n')
