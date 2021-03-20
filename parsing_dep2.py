'''
parsing de dependencias 2

relação mais complexa
'''

import spacy
pln = spacy.load('pt')

documento = pln('reserva de uma mesa para o restaurante e de um táxi para o hotel')

tarefas = documento[3], documento[10]
locais = documento[6], documento[13]

#print(tarefas, locais)

'''for local in locais:
    print("----", local)
    for objeto in local.ancestors:
        print(objeto)'''

for local in locais:
    for objeto in local.ancestors:
        if objeto in tarefas:
            print("reserva de {} é para o {} ".format(objeto,local))
            break

print('\n')
print(list(documento[6].children))