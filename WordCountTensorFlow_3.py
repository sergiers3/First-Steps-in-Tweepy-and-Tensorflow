from nltk.corpus import stopwords

import nltk
import re
nltk.download('punkt')
from collections import Counter

#Create a function that returns the tokens of a file
def get_tokens():
    with open('FirstContactWithTensorFlow.txt', 'r') as tf:
        text = tf.read()
        tokens = nltk.word_tokenize(text)

        #Remove punctuation
        lowers = text.lower()
        no_punctuation = re.sub(r'[^\w\s]', '', lowers)
        tokens = nltk.word_tokenize(no_punctuation)


    return tokens

#Obtain the tokens from the file
tokens = get_tokens()
#count = Counter(tokens)

# lambda expression here
# store stopwords in a variable for eficiency
# avoid retrieving them from ntlk for each iteration
sw = stopwords.words('english')


filtered = [w for w in tokens if not w in sw]
count = Counter(filtered)


#Print 10 most common
print (count.most_common(10))
#Print total number of words
print ("Total words: " + str(len(list(count.elements()))))