'''
palavras que aparecem com muita frequencia e que não tem significado especifico

exemplo: 'de', 'da', 'e', 'a', 'ou', 'se'

'''

import spacy
pln = spacy.load('pt')
from spacy.lang.pt.stop_words import STOP_WORDS

#print(len(STOP_WORDS)) {'fazeis', 'toda', 'quinta', 'quê', 'sistema', 'vossas', 'duas', 'através', 'das', 'nas', 'tendes', 'sétimo', 'eu', 'são', 'nem', 'zero', 'tipo', 'três', 'e.... etc
#print(STOP_WORDS)
#print(pln.vocab['ir'].is_stop) # True
#print(pln.vocab['caminhar'].is_stop) # False

documento = pln('o globo terrestre foi mostrado na Globo')
#documento = pln('Estou aprendendo processamento de linguagem natural, curso em curitiba')
for token in documento:
    if not pln.vocab[token.text].is_stop:
        print(token.text)