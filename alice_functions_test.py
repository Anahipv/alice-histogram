from nltk.tokenize import word_tokenize
from alice_functions import remove_stopwords, normalize
from alice import stopwords_set

def test_stopwords_normalize():

    l = "hola. don't will I'll she'll hEre's jfkldsJS $$$ I'd don't x J upon Upon y your another already always"
    lt =  word_tokenize(l)
    ln = normalize(lt)

    assert normalize(lt) ==['hola', 'do', 'will', 'i', 'she', 'here', 'jfkldsjs', 'i', 'do', 'x', 'j', 'upon', 'upon', 'y', 'your', 'another', 'already', 'always']
    assert remove_stopwords(ln, stopwords_set) == ['hola', 'will', 'here', 'jfkldsjs']






