'''
parsing de dependencias 2

relação entre pai-filho entre as palavras
'''

import spacy
pln = spacy.load('pt')

documento = pln('reserve uma passagem saindo de guarulhos e chegando em curitiba')
# exemplocaso de uso: um chatbot que precisa identificar a origem e o destino

origem = documento[5]
destino = documento[9]

#print(list(origem.ancestors)) # [passagem, reserve]
#print(list(destino.ancestors)) # [chegando, reserve]

print(documento[0].is_ancestor(documento[2])) # True