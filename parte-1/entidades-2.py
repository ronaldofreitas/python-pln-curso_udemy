import spacy

pln = spacy.load('pt_core_news_lg')

f = open("./texto3.txt", "r")
#f = open("./texto.txt", "r")
texto2 = f.read()

#texto2 = 'Xuxa e Ronaldinho são bem conhecidos, mas Baratt, Carlos e Carla não são'
#texto2 = 'Bill Gates nasceu em Seattle em 28/10/1955 e foi o criador da Microsoft'
documento2 = pln(texto2)
for entidade in documento2.ents:
    if entidade.label_ == 'PER':
        print(entidade.text)
