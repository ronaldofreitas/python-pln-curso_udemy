'''

NER (Named-Entity Recognition)
Encontrar e classificar entidades no texto, dependendo da base de dados que foi utilizada para o treinamento (pessoa, localização, empresa, numéricos)
Usado em chatbots para saber o assunto falado
Siglas: https://spacy.io/api/annotation#named-entities

as palavras utilizadas para esse modelo podem não atender casos específicos de uso
'''

import spacy
pln = spacy.load('pt')



'''
from spacy import displacy
texto = 'em Salvador, A IBM é uma empresa dos Estados Unidos voltada para a área de informática. Sua sede no Brasil fica em São Paulo e a receita em 2018 foi de aproximadamente 320 bilhões de reais'
documento = pln(texto)

for entidade in documento.ents:
    print(entidade.text, entidade.label_)
    
    # IBM ORG
    # Estados Unidos LOC
    # Brasil LOC
    # São Paulo LOC
'''

''''
psg = displacy.render(documento, style='ent')
print(psg)
'''

# encontrar pessoas PER
texto2 = 'Bill Gates nasceu em Seattle em 28/10/1955 e foi o criador da Microsoft'
documento2 = pln(texto2)
for entidade in documento2.ents:
    if entidade.label_ == 'PER':
        print(entidade.text)
