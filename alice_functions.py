def remove_stopwords(text, filtering):
    """
    Remueve de una lista las palabras que esten en el filtering y devuelve una lista filtrada
    """
    return list(filter(lambda x: not x in filtering, text))

# Normalizar los token, isalpha() devuelve True si todos los caracteres de la cadena son alfabetos
def normalize(text):
    """
    Recibe una lista y la devuelve sin ningun tipo de puntuacion y todas en minuscula
    """
    # new_text = list(filter(lambda x: x.isalpha(), text))
    # return list(map(lambda x: x.lower(), new_text))
    return list(map(lambda x: x.lower(), filter(lambda x: x.isalpha(), text)))

def count_words(lista):
    """
    Cuenta la cantidad de veces que aparece una palabra y devulve un diccionario
    """
    frequence_words = {}
    for word in lista:
        if not word in frequence_words:
            frequence_words[word] = 1
        else:
            frequence_words[word] += 1
    return frequence_words

def word_probability(dic):
    """
    Calcula la probabilidad de que aparezca una palabra en el texto
    """ 
    length = len(dic)
    return dict(map(lambda x: (x[0], round(x[1] / length, 2)), dic.items()))

def display_histogram(histogram):
    # probabilidad de 0 a 1
    dis_hist = {}
    for k, v in histogram.items():
        if v > 0.02:
            rep = int(v * 50 / 1)
            dis_hist[k] = "#" * rep
    for k, v in dis_hist.items():
        print(f'{k} : {v}')