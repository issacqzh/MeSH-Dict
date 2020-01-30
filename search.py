import json

with open('../terms.json', 'r') as file:
        data= json.load(file)
running = True
while(running):
    term = input("Please enter a string:\n")
    if term.lower() == 'exit':
        break
    try:
        print(data[term.lower()])
    except:
        print('It can\'t be found')
    print('')
    