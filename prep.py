import nltk

stop_words_nltk = nltk.corpus.stopwords.words('portuguese')

#Metodo para fazer o stemming na base de dado
def apply_stemmer(text_and_class):
    stemmer = nltk.stem.RSLPStemmer()  # stemmer usado com a linguagem português
    frases = []
    for (palavras, polaridade) in text_and_class:
        # aplica o stemming nas palavras da frase e desconsidera as stop_words
        com_stemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stop_words_nltk]
        frases.append((com_stemming, polaridade))
    return frases
