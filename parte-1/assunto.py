
import spacy 
nlp = spacy.load('pt_core_news_sm')


def get_subject_object_phrase(doc, dep):
    doc = nlp(doc)
    for token in doc:
        if dep in token.dep_:
            subtree = list(token.subtree)
            start = subtree[0].i
            end = subtree[-1].i + 1
    return str(doc[start:end])

frase = '''
A decisão da semana passada do Supremo Tribunal Federal (STF), que confirmou uma liminar do ministro Alexandre de Moraes, de impor multa e bloquear contas bancárias do deputado Daniel Silveira (PTB-RJ) continua causando perplexidade entre juristas. Para alguns dos principais penalistas do país, a Corte criou uma inovação, em matéria penal, não prevista na legislação.


A medida também chamou a atenção dentro do Ministério Público que, até o momento, não via essa possibilidade. Procuradores ouvidos pela reportagem estranharam a decisão e consideram que esse precedente questionável poderá agora ser aplicado a qualquer pessoa.


Na última sexta (1º), por 9 votos a 2, a maioria dos ministros referendou a aplicação de multa diária de R$ 15 mil a Daniel Silveira, além do bloqueio de todas as suas contas bancárias, para forçá-lo a colocar a tornozeleira eletrônica. O parlamentar se recusava a instalar o equipamento para ser monitorado, por considerar que a medida afetava o exercício de seu mandato e, por isso, deveria ser autorizada pela maioria dos deputados federais, como ocorre em caso de prisão.

Como Moraes entendia que não haveria prejuízo ao mandato – ele poderia se deslocar dentro do estado do Rio de Janeiro e também viajar a Brasília – optou então por impor a multa e o bloqueio. O que surpreendeu o mundo jurídico é que as duas medidas não estão previstas no Código de Processo Penal (CPP) e, por isso, não poderiam, a rigor, ser impostas.

“Todo poder é condicionado pela legalidade. Então, no processo penal você só pode punir alguém – e falo punir genericamente, considerando a palavra punir não só como pena, mas uma medida cautelar também é uma forma de punir, de limitar liberdade – dentro dos estritos limites da legalidade, dentro daqueles institutos previstos na lei”, disse à Gazeta do Povo Aury Lopes Jr., advogado, doutor em direito processual penal e professor titular da PUC-RS.

O uso de tornozeleira eletrônica é uma medida que substitui a prisão preventiva, que é decretada quando há risco à ordem pública, à investigação ou à aplicação da lei penal. Moraes impôs o monitoramento porque, em suas palavras, Silveira “voltou a proferir ataques direcionados” ao STF e também a “proferir ofensas direcionadas” aos ministros.

Em eventos públicos, o deputado conclamou as pessoas a “enfrentar o sistema”, referindo-se ao tribunal. Disse que não havia “bússola moral” a integrantes da Corte. “E vai continuar essa história se nós dobrarmos os joelhos e aceitarmos essas imposições que vêm através do Judiciário, a via mais rara de tomada de poder”, afirmou, durante o congresso Brasil Profundo, realizado em de Londrina (PR), no dia 12.

“Ô ministro, olha só, o senhor está cometendo muitas inconstitucionalidades. Eu acho que o senhor tem que pegar... agir dentro da Constituição. Sabe por quê? Senão o senhor está chateando toda a Federação, toda a República Federativa do Brasil. Está ficando complicado aqui para o senhor continuar vivendo aqui, nem que seja juiz”, disse ainda Daniel Silveira.

Ao determinar o monitoramento eletrônico – medida que já havia sido adotada no ano passado, precisamente em substituição a uma prisão preventiva – Moraes disse que ele já havia violado sua área de circulação e até tentado fugir da Polícia Federal, em Petrópolis - o que a defesa de Silveira nega. A recusa em colocar novamente o aparelho, permanecendo dentro da Câmara, seria “completa deturpação da natureza do cargo de deputado federal”.

“Estranha e esdrúxula situação, onde o réu utiliza-se da Câmara dos Deputados para esconder-se da Polícia e da Justiça, ofendendo a própria dignidade do Parlamento, ao tratá-lo como covil de réus foragidos da Justiça”, escreveu o ministro na decisão que impôs a multa e o bloqueio de bens.

No mesmo dia da decisão, quinta-feira (31), Daniel Silveira foi à Polícia Federal e aceitou instalar o aparelho. A multa, assim, deixou de ser aplicada e as contas do deputado permaneceram liberadas. Ainda assim, o precedente foi aberto com aval da maioria dos ministros, que, na sexta, confirmaram a possibilidade não prevista em lei de que um réu seja atingido no bolso se descumprir uma medida substitutiva da prisão preventiva.
'''
#dep='nsubj' for subject and 'dobj' for object
dpp = "nsubj"
print( get_subject_object_phrase(frase, dpp) )