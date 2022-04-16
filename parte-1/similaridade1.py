
import spacy
from spacy import displacy
#pln = spacy.load('pt')
pln = spacy.load('pt_core_news_sm')

texto = pln('gato cachorro cavalo pessoa')

for t1 in texto:
    for t2 in texto:
        similaridade = int( t1.similarity(t2) * 100 )
        print("{} é {}% similar a {} ". format(t1, similaridade, t2))


#r = texto1.similarity(texto2)
#print(r) # 0.7892121872777581 79%
