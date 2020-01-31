import xml.etree.ElementTree as ET
import json

qualifier='qual2020'
descriptor='desc2020'
supplemental='supp2020'

def crawl_terms(type):
    typename= 'DescriptorName' if type == descriptor else 'QualifierName'
    tree = ET.parse(type+'.xml')
    root = tree.getroot()
    # Create a dictionary
    vocabulary = {}
    count=0
    # iterate through all MeSH terms
    for child in root:
        name = child.find(typename).find('String').text
        for concept in child.find('ConceptList'):
            if concept.find('ScopeNote') is None:
                continue
            definition = concept.find('ScopeNote').text.strip()
            terms = concept.find('TermList')
            for term in terms:
                term_name = term.find('String').text.lower()
                vocabulary[term_name] = definition

    return vocabulary

def concat(dict_a,dict_b):
    dict_a.update(dict_b)
    with open('terms.json', 'w') as outfile:
        json.dump(dict_a, outfile)


if __name__ == '__main__':
    qual_dict=crawl_terms(qualifier)
    print('qualifiers collected')
    desc_dict=crawl_terms(descriptor)
    print('descriptors collected')
    concat(qual_dict,desc_dict)
    print('terms concatenated')
    
