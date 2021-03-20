
import spacy
from spacy import displacy

pln = spacy.load('pt')
documento = pln('Que locais podemos visitar em Curitiba e para ficar em Guarulhos?')

lugares = documento[5], documento[10]
acoes = documento[3], documento[8]
 
for local in lugares:
    for acao in local.ancestors:
        if acao in acoes:
            print("{} para {}".format(local, acao))
            break