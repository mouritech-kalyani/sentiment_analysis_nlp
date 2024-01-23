# convert letters into lower case
# remove punctuations from the string
# tokenization and stop words


import string
from collections import Counter
import matplotlib.pyplot as plt

text = open('readFile.txt', encoding='utf-8').read()
lower_text=text.lower()
# print('Lower test is: ',lower_text)
#  first str : specifies list of characters that need to be replaced
#  second str: specifies list of characters with which characters need to replaces
#  third str: specifies the list of characters that needs to be deleted

# first str = 'abc'
#  second str = 'gef'

clean_text = lower_text.translate(str.maketrans('', '', string.punctuation))
# print('Clean text is : ', clean_text)

tokenized_words = clean_text.split()
# print('Tokenized word is: ', tokenized_words)

# Making Stop word list

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

# print('Final word list: ', final_words)        

# NLP Algorithm
# 1. Check of the word in final word list is also present in emotion.txt file
#  - Open emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split
#  2. If word is present -> Add the emotion to emotion_list
#  3. Finally count each emotion in the emotion list
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

# print(emotion_list)
counters = Counter(emotion_list)
print('counters is', counters)

fig, axis1 = plt.subplots()
axis1.bar(counters.keys(), counters.values())
fig.autofmt_xdate()
plt.savefig('emotion_chart.jpg')
plt.show()