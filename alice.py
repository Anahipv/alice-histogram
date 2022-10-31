from nltk.tokenize import word_tokenize
from alice_functions import normalize, remove_stopwords, count_words, word_probability, display_histogram

# Leer el texto de Alice y StopWords, guardar en una variable cada uno
with open('AliceInWonderland.txt', encoding='utf-8') as f:
    alice_text = f.read()

with open('stopwords.txt', encoding='utf-8') as f:
    stop_words = f.read()

# Con nltk tokenizar el texto Alice y stopWords
alice_tokenized = word_tokenize(alice_text)
stopwords_tokenized = word_tokenize(stop_words)

# Crear un set desde stop_words
stopwords_set = set(stopwords_tokenized)

# Remover caracteres especiales y normalizar el texto de Alice
alice_normalized = normalize(alice_tokenized)
alice_final = remove_stopwords(alice_normalized, stopwords_set)

# Crear un diccionario contando la frequencia con la que aprece cada palabra y calcular la probabilidad
alice_dic = count_words(alice_final)
alice_histogram = word_probability(alice_dic)

# Graficar el histograma
display_histogram(alice_histogram)


