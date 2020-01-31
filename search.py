import json

with open('../terms.json', 'r') as file:
    dict= json.load(file)
with open('../related.json','r') as file:
    related = json.load(file)
with open('../tree_number.json','r') as file:
    tree_numbers = json.load(file)

def get_tree_related(term):
    tree_list=[]
    if term in tree_numbers:
        tree_list=tree_numbers[term]
    # for number in tree_list:
        
    return tree_list


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
                print(word)
    else:
        print('It can\'t be found')
    
    print('-'*40+'\n')
    
