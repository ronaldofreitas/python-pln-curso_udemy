import spacy
pln = spacy.load('pt')

documento = pln('Estou aprendendo processamento de linguagem natural, curso em curitiba')

# cada palavra no 'documento' é considerado um 'token'
# POS = part-of-speech

'''
for token in documento:
    print(token.text, token.pos_)
'''

'''
# lemma = raiz da palavra
# pos = parte da fala
# tag = informações morfológicas, como se o verbo está no passado
# shape = formato (maiúsculo, minusculo, digitos)
# alpha = se é alfabético
# stop = se é stopword
for token in documento:
    print(token.text, token.lemma_, 
    token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
'''

# identificar Nomes Próprios... nome de cidade, nome de pessoas etc
for token in documento:
    if token.pos_ == 'PROPN':
        print(token.text)
