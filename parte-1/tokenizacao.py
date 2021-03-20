'''
tokenização é separar cada uma das palavras em formato correto
'''

import spacy
from spacy import displacy
pln = spacy.load('pt')

documento = pln('estou aprendendo processamento de linguagem natural, curso em curitiba')

for token in documento:
    print(token)