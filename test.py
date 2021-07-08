from pyclausie import ClausIE
cl = ClausIE.get_instance()


sents = ["Marie was born in Paris. She was born in France."]

triples = cl.extract_triples(sents)
if triples != None:
    for triple in triples:
        print(f"{triple[1]} --> {triple[2]} --> {triple[3]}")