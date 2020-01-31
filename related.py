import xml.etree.ElementTree as ET
import json

descriptor='desc2020'

def get_related():
    tree = ET.parse('desc2020.xml')
    root = tree.getroot()
    # Create a dictionary
    vocabulary = {}
    count=0
    # iterate through all MeSH terms
    for child in root:
        name = child.find('DescriptorName').find('String').text.lower()
        terms=[]
        if child.find('SeeRelatedList') is not None:
            for related in child.find('SeeRelatedList'):
                term = related.find('DescriptorReferredTo').find('DescriptorName').find('String').text
                terms.append(term)
        
        if child.find('PharmacologicalActionList') is not None:
            for action in child.find('PharmacologicalActionList'):
                term = action.find('DescriptorReferredTo').find('DescriptorName').find('String').text
                terms.append(term)
        
        if len(terms) > 0:
            vocabulary[name] = terms

    print(len(vocabulary))
    with open('related.json', 'w') as outfile:
        json.dump(vocabulary, outfile)

if __name__ == '__main__':
    get_related()