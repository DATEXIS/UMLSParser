import json

from umlsparser.UMLSParser import UMLSParser

umls = UMLSParser('/home/toberhauser/DEV/Data/UMLS/2019AA-full/2019AA', language_filter=['GER', 'ENG'])

for cui, concept in umls.get_concepts().items():
    output = {
        'cui': cui,
        'names':{
            'de': list(concept.get_preferred_names_for_language('GER')),
            'en': list(concept.get_preferred_names_for_language('ENG'))
        },
        'definitions': list(concept.get_definitions()),
        'semantic_type': {
            'TUI': concept.get_tui(),
            'name': umls.get_semantic_types().get(concept.get_tui()).get_name()
        }
    }
    if output.get('definitions'):
        print(json.dumps(output))
