from DataScienceExamples.DataScienceTasks import Task_4
from sklearn.model_selection import train_test_split
import math
import glob
import re
import random
from collections import Counter

#Вероятность спама, при наличии заданного слова.
def p_spam_given_word(word_prob):
    word, ps, pns = word_prob
    return ps / (ps + pns)




classifier = Task_4.NaiveBayes(0.01) # h = 0.01
path = r"C:\DataScience\spam\*\*"
data = []
for fn in glob.glob(path):
    is_spam = "ham" not in fn
    with open(fn,'r', encoding='ansi') as file:
        for line in file:
            if line.startswith("Subject:"):
                subject = re.sub(r"^Subject: ","",line).strip()
                data.append((subject,is_spam))
random.seed(0)
lc = math.floor(len(data)*0.75)
X_train, X_test = data[:lc], data[lc:]
print(X_train)
print(X_test)
classifier.train(X_train)
classified = [(subject, is_spam, classifier.classify(subject)) for subject, is_spam in X_test]
counts = Counter((is_spam, spam_probability > 0.5) for _,is_spam,spam_probability in classified)
print(counts)


#TP = spam is spam
#TN = nspam is nspam = 353.
#FP = nspam is spam
#FN = spam is nspam = 503
#Precision = True_Positve / (True_Positive + False_Positive)
#Scale = True_Positve / (True_Positive + False_Negative)
