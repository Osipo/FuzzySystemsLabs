import re
from collections import defaultdict
import math
# Наивный Байес (события независимы)
# При наличии обучающих сообщений с меткой S | NOT(S)
# P(Xi | S) = All messages with word_i / All messages.
# Поскольку может оказаться, что слово данные будут только в NOT(S)
# Числитель обнулится. Поэтому для сохранения вероятности
# используют сглаживающий параметр h
# Т.е. P(Xi | S) = (h + All messages with word_i) / (2h + All messages)

#Разделить строку на слова.
#(Слово состоит из букв или цифр)
def generateWordsSet(message):
    message = message.lower()
    all_words = re.findall("[a-zA-Z0-9']+",message) #Regex
    for w in all_words:
        w = delS(w)
    return set(all_words)

def delS(word):
    return re.sub("s$","",word)

#Подсчитать частотность слов в спамных и НЕ в спамных сообщениях.
#Вернёт словарь, с ключами [слово][спам | Неспам]
#со значениями (количество встречаемости в спаме, Не в спаме).
# Argument: list of tuples like (word, isSpam)
# Return: dictionary[word][0 | 1] = counts. 0 - spam, 1 - not_spam
def count_words(t_set):
    #t_set = Обуч. выборка, состоит из пар (сообщение,isSpam)
    count = defaultdict(lambda: [0,0])
    for message, is_spam in t_set:
        for word in generateWordsSet(message):
            count[word][0 if is_spam else 1] +=1
    return count


# Вероятности для каждого слова.
# P(Xi | S) и  P(Xi | NOT(S))
def P_wi(counts, ts, nts, h):
    return [(w,
             (spam + h) / (ts + 2*h),
             (not_spam + h) / (nts + 2*h))
             for w, (spam, not_spam) in counts.items()]

# Вероятность спама.
# Произведение вероятностей представляется в виде суммы логарифмов.
# (Из-за возможного переполнения снизу вызванное арифметикой с числами
#  с плавающей точкой)ю
def P_spam(words_P,message):
    message_words = generateWordsSet(message)
    log_prob_if_spam = log_prob_if_not_spam = 0.0

    #All words in dictionary
    for w, pS, pNS in words_P:
        #Если слово в сообщении, то добавить вероятность
        #Встретить его в сообщении.
        if w in message_words:
            log_prob_if_spam += math.log(pS)
            log_prob_if_not_spam += math.log(pNS)
        # Иначе, если слово нет в сообщении
        # Добавить вероятность НЕ встретить его в сообщении.
        else:
            log_prob_if_spam += math.log(1.0 - pS)
            log_prob_if_not_spam += math.log(1.0 - pNS)

    prob_if_spam = math.exp(log_prob_if_spam)
    prob_if_not_spam = math.exp(log_prob_if_not_spam)
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)

class NaiveBayes:
    def __init__(self, h=0.5):
        self.h = h
        self.word_prob = []


    def train(self,train_set):
        # Количество спамных и НЕспамных сообщений
        num_spams = 0
        for message, is_spam in train_set:
            if is_spam:
                num_spams+=1
        num_not_spams = len(train_set) - num_spams
        print(num_spams)
        # Compute Probs.
        word_counts = count_words(train_set)
        self.word_prob = P_wi(word_counts,num_spams,num_not_spams,self.h)

    def classify(self,message):
        return P_spam(self.word_prob,message)