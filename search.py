import json

with open('../terms.json', 'r') as file:
    dict= json.load(file)
with open('../related.json','r') as file:
    related = json.load(file)
with open('../tree.json','r') as file:
    tree = json.load(file)
with open('../tree2term.json','r') as file:
    tree2term = json.load(file)

def get_tree_related(term):
    tree_num_list=[]
    term_list=[]
    if term in tree:
        tree_num_list=tree[term]
        for number in tree_num_list:
            all_rel_list=[(key,value) for key, value in tree2term.items() if number[0:-4] in key]
            for rel in all_rel_list:
                if len(rel[0]) == len(number) or len(rel[0]) == len(number)-4 or len(rel[0]) ==len(number)+4:
                    term_list.append(rel[1])
    term_list=list(set(term_list))
    term_list.remove(term)
    return term_list


def get_related(term):
    related_list=[]
    if term in related:
        related_list=related[term]
    return related_list


while(1):
    term = input("Please enter a string:\n").lower()
    if term == 'exit':
        break
    if term in dict:
        print('Definition: ',dict[term])
        all_related=get_related(term)+get_tree_related(term)
        if len(all_related) > 0:
            print('\nAlso Consider:')
            for word in all_related:
                print(word,end='                 '), print(dict[word.lower()])
    else:
        print('It can\'t be found')
    
    print('-'*40+'\n')
    
