import random
def get_words(word_amount, language):

    list1 = []
    if language == "tr":
        f = open("words_tr.txt","r")
    if language == "en":
        f = open("words_en.txt","r")
    for i in f:
        list1.append(i.strip("\n"))
    return random.choices(list1,k=word_amount)
        