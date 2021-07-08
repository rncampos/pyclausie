from pyclausie import ClausIE
cl = ClausIE.get_instance()

sents = ["Política Canção Britain's."]
#sents = ["After gaël giving 5,000 people a second chance at life, doctors are celebrating the 25th anniversary of Britain's first heart transplant."]
#sents = ["He wan After her"]
#sents = ["Marie was born in Paris. She was born's in France."]
#sents = ['António Pires de Lima, que mantém divergências políticas públicas com Nobre Guedes, considerou que a ausência do ex-ministro do Ambiente vai limitar o âmbito do próprio Congresso.']
triples = cl.extract_triples(sents)
if triples != None:
    for triple in triples:
        print(f"{triple[1]} --> {triple[2]} --> {triple[3]}")