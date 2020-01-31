import xml.etree.ElementTree as ET
import json

descriptor='desc2020'
qualifier='qual2020'

def get_tree_number(type):
    tree = ET.parse(type+'.xml')
    root = tree.getroot()
    # Create a dictionary
    vocabulary = {}
    tree2term={}
    # iterate through all MeSH terms

    for child in root:
        typename='DescriptorName' if type==descriptor else 'QualifierName'
        name = child.find(typename).find('String').text.lower()
        terms=[]
        if child.find('TreeNumberList') is not None:
            for related in child.find('TreeNumberList'):
                term = related.text
                terms.append(term)
        
        if len(terms) > 0:
            vocabulary[name] = terms
            for num in terms:
                tree2term[num] = name
                
    return vocabulary,tree2term

def concat(dict_a,dict_b,filename):
    dict_a.update(dict_b)
    with open(filename+'.json', 'w') as outfile:
        json.dump(dict_a, outfile)

if __name__ == '__main__':
    qual_tree, qual_tree2term=get_tree_number(qualifier)
    print('qualifiers collected')
    desc_tree, desc_tree2term=get_tree_number(descriptor)
    print('descriptors collected')
    concat(qual_tree,desc_tree,'tree')
    print('tree numbers concatenated')
    concat(qual_tree2term,desc_tree2term,'tree2term')
    print('tree2term concatenated')
    