'''
a biblioteca SpaCy já tem por default diversos algorítimos de redes neurais convulucionais 
'''

'''
import pt_core_news_sm
pln = pt_core_news_sm.load()
'''
import spacy
pln = spacy.load('pt')

documento = pln('o globo terrestre foi mostrado na Globo')
#documento = pln('Estou aprendendo processamento de linguagem natural, curso em curitiba')

# cada palavra no 'documento' é considerado um 'token'
# POS = part-of-speech ou 'partes da fala'.... pega palavra por palavra e classifica se é substantivo, adjetivos, verbos, nome próprios etc


for token in documento:
    print(token.text, token.pos_)


'''
ADJ: adjective
ADP: adposition
ADV: adverb
AUX: auxiliary verb
CONJ: coordinating conjunction
DET: determiner
INTJ: interjection
NOUN: noun
NUM: numeral
PART: particle
PRON: pronoun
PROPN: proper noun
PUNCT: punctuation
SCONJ: subordinating conjunction
SYM: symbol
VERB: verb
X: other
'''

# lemma = raiz da palavra
# pos = partes da fala
# tag = informações morfológicas, como se o verbo está no passado
# dep = depencia sintática
# shape = formato (maiúsculo, minusculo, digitos)
# alpha = se é alfabético
# stop = se é stopword
'''for token in documento:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

'''
'''# identificar Nomes Próprios... nome de cidade, nome de pessoas etc
for token in documento:
    if token.pos_ == 'PROPN':
        print(token.text)
'''

