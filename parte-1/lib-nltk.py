# rslp é um stemizador para a lingua portuguesa

import nltk
import spacy
pln = spacy.load('pt')

documento = pln('Estou aprendendo processamento de linguagem natural, curso em curitiba')

#nltk.download('rslp')
# [nltk_data] Downloading package rslp to /home/ronaldo/nltk_data...
# [nltk_data]   Unzipping stemmers/rslp.zip.

'''
stemmer = nltk.stem.RSLPStemmer()
r = stemmer.stem('aprendendo')
print(r)
"aprend"  --- o radical da palavra
'''

stemmer = nltk.stem.RSLPStemmer()

for token in documento:
    print(token.text, token.lemma_, stemmer.stem(token.text))
    '''
    Estou Estou est
    aprendendo aprender aprend
    processamento processamento process
    de de de
    linguagem linguagem lingu
    natural natural natur
    , , ,
    curso cursar curs
    em em em
    curitiba curitiba curitib
    '''