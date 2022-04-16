'''
GloVe = é um algoritimo usado para fazer calculo de relacionamento entre palavras
'''

import spacy
from spacy import displacy
#pln = spacy.load('pt')
#pln = spacy.load('pt_core_news_sm')
pln = spacy.load('pt_core_news_lg')


'''p1 = pln('olá')
p2 = pln('oi')
p3 = pln('ou')

r = p1.similarity(p2)
print(r) # 0.8258470163434681 ou 82% de similaridade
r = p1.similarity(p3)
print(r) # 0.556686068341704 ou 55% de similaridade'''

texto1 = pln('quando será lançado o novo filme?')
texto2 = pln('o novo filme será lançado mês que vem')
texto3 = pln('qual a cor do carro?')

r = texto1.similarity(texto2)
print(r) # 0.7892121872777581 79%

r = texto1.similarity(texto3)
print(r) # 0.6799004875840708 69%
