'''
Lematização:
- extrair a palavra base 
- análise vocabular e morfológica

Stemização:
- extrair o radical das palavras
'''

import spacy
pln = spacy.load('pt')

doc = pln('encontrei encontraram encontrarão encontrariam')

'''
for token in documento:
    print(token.text, token.lemma_)
'''
print([token.lemma_ for token in doc])