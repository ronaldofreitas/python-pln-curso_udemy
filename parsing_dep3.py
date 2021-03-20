
import spacy
from spacy import displacy

pln = spacy.load('pt')
documento = pln('reserva de uma mesa para o restaurante e de um táxi para o hotel')

#displacy.serve(documento, style='dep')
#displacy.render(documento, style='dep', jupyter=True)

print( list(documento[3].ancestors) )

print( list(documento[3].children) )