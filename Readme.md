# CLOUD-COMPUTING-CLASS-2018
 
* Sergio Ruiz: __sergiers@opendeusto.es__
* Dagoberto Herrera: __dagobertoherreramurillo@live.com__

## Task 2.1.1: Word Count 1
`WordCountTensorFlow_1.py` computes and shows the 10 most common "words" and print the total number of words of the book.

```python
Output:
/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/sergiers/PycharmProjects/CLOUD-COMPUTING-CLASS-2018/Lab2/WordCountTensorFlow_1.py
[nltk_data] Downloading package punkt to /Users/sergiers/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[('the', 1343), (',', 1251), ('.', 810), (')', 638), ('(', 637), ('of', 586), ('to', 491), ('a', 468), (':', 454), ('in', 417)]
Total words: 25155

Process finished with exit code 0
```

Note that by default the tokenizer includes punctuation elements. Within the 10 most common words, 5 punctuation marks represent 3,790 occurrences with respect to a total of 25,155 words (15.1%).



## Task 2.1.2: Remove punctuation 
`WordCountTensorFlow_2.py` computes and prints the 10 most common words without punctuation characters, as well as the total number of words remaining:

```python
/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/sergiers/PycharmProjects/CLOUD-COMPUTING-CLASS-2018/Lab2/WordCountTensorFlow_1.py
[nltk_data] Downloading package punkt to /Users/sergiers/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[('the', 1444), ('of', 586), ('to', 531), ('in', 506), ('a', 481), ('and', 346), ('is', 289), ('we', 279), ('that', 275), ('this', 268)]
Total words: 19593

Process finished with exit code 0
```
Without the punctuation marks the word count decreases to 19,593. Within the most common words, stopwords like 'the', 'of' and 'to' predominate. The new top 10 represents 5,005 occurrences (25.6% of the total words of the document).

## Task 2.1.3: Stop Words

> Is it not "Tensorflow" the most frequent word? Why? Which are the Stop Words?

"Tensorflow" is not the most frequent word because the list of common terms is headed by articles, pronouns, verbs, prepositions ... ('the', 'of', 'to', 'in', 'a', ' and ',' is', 'we', 'that', 'this'). This type of extremely common words are called stop words, and generally add little semantic value to document analysis (Stanford, 2008, https://nlp.stanford.edu).


`WordCountTensorFlow_3.py` computes and prints the total number of words remaining and the ten most common word after removing the stop words.

```python
/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/sergiers/PycharmProjects/CLOUD-COMPUTING-CLASS-2018/Lab2/WordCountTensorFlow_3.py
[nltk_data] Downloading package punkt to /Users/sergiers/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[('tensorflow', 193), ('data', 102), ('tensor', 99), ('code', 90), ('learning', 81), ('function', 74), ('one', 73), ('use', 65), ('example', 64), ('available', 63)]
Total words: 11220

Process finished with exit code 0
```



## Task 2.2.1: Accessing your twitter account information



To perform this task, we use harcoded tokens. As a good practice, we have abstracted the tokens to a different class, in order to commit the same code without sharing the tokens of the application. The case with the credentials is called `Credentials.py`.


```python
/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/sergiers/PycharmProjects/CLOUD-COMPUTING-CLASS-2018/Lab2/Twitter_1.py
Name: The all seeing eye
Location: 
Friends: 1
Created: 2013-07-05 14:31:06
Description: 

Process finished with exit code 0
```


> Is the data printed correctly? Is it yours? The information is mine and it is printed correctly.


## Task 2.2.2: Accessing Tweets

According to twitter:
> The Twitter REST API utilizes a technique called ‘cursoring’ to paginate 
large result sets. Cursoring separates results into pages (the size of which are defined by the count 
request parameter) and provides a means to move backwards and forwards through these pages.

This cursor also provides our way to access the twitter data, such as tweets, Jsons etc:


```python
/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/sergiers/PycharmProjects/CLOUD-COMPUTING-CLASS-2018/Lab2/Twitter_2.py

Timeline: 

RT @Terrazocultor: @DiffHell Como dijo un cantante:
"No es el Mercedes"
"Es quién lo conduce"
RT @nobbis: Real-time photogrammetry with #ARKit https://t.co/4kqnI84ypa
RT @lrubiogarcia: WANT. big data de mis nalgas https://t.co/ihb9fE4of4

Process finished with exit code 0
```



## Extra: Using PIN-Code auth:

There is a more "correct" way to autorize applications. Normally when a user wants to use an application he should not use "tokens" or similar elements, since this is not a user friendly procedure. To solve this, the Twitter API implements an authentication system called PIN-Based authentication, which allows you to authorize the application without the need to use harcoded private tokens. You just have to generate the URL of the application which, when opened in the internet browser, will provide you with a numeric PIN that you must copy and paste into the application (in our case, we are using the `import browser` methods to automatically open the URL in the web browser). The application will automatically receive the private tokens, being this process a black box for the user. Finally, another good practice would be to implement a singleton pattern so that access to the application can only be instantiated once.

The file is called `Twitter_0.py`.



The result:
```python
/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/sergiers/PycharmProjects/CLOUD-COMPUTING-CLASS-2018/Lab2/Twitter_0.py
URL for obtaining the pincode is: https://api.twitter.com/oauth/authorize?oauth_token=uQci4gAAAAAAToKjAAABYhTiews

Copy/Paste the pincode from the web browser: 7972044
Name: The all seeing eye
Location: 
Friends: 3
Created: 2013-07-05 14:31:06
Description: 

Process finished with exit code 0
```

Note that in this case we just copy-paste the PIN into the terminal in the application. But if we want to go further, we can do [web scraping](https://en.wikipedia.org/wiki/Web_scraping) in order to automatically extract the PIN into our application, making the life easier for the user.

## Task 2.3: Tweet pre-processing

The idea with a tweet is to obtain all your data in the most comfortable way possible (If it is an RT, 
if it carries mention, if it carries hastagh, emojis etc). For this, we need to tokenize the tweet. We can 
use `nltk`, but this tokenization is very poor, as we can see below:

```python
TOKENIZER: 
['RT', '@', 'JordiTorresBCN', ':', 'just', 'an', 'example', '!', ':', 'D', 'http', ':', '//JordiTorres.Barcelona', '#', 'masterMEI']
Process finished with exit code 0
```

To improve this, we can use regex. A regular expression, regex or regexp a sequence of characters that define a search pattern. If we define "how it would be" each thing (for example, a mention starts with '@' and ends with a blank) We can tokenize more effectively. In this example, we print our three first tweets from timeline, first RAW tweet and then, tokenized:


```python
/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/sergiers/PycharmProjects/CLOUD-COMPUTING-CLASS-2018/Lab2/Twitter_2.py


Timeline: 
RT @Terrazocultor: @DiffHell Como dijo un cantante:
"No es el Mercedes"
"Es quién lo conduce"
RT @nobbis: Real-time photogrammetry with #ARKit https://t.co/4kqnI84ypa
RT @lrubiogarcia: WANT. big data de mis nalgas https://t.co/ihb9fE4of4
RT @OrdureBizarre_: https://t.co/ApiwWg1p38
RT @FreeMemesKids: 😂 https://t.co/Cq5YtVgnzi
@DiffHell @Terrazocultor Tas pasao
RT @danielegrasso: No, Albert Rivera no ha dicho que estaría "encantado de liderar el movimiento transversal" feminista. 

Aquí va la trans…
RT @astro_duque: Hace 50 años (2 Marzo 1968) la Unión Soviética envió una nave Saiús a la Luna con un maniquí (parecido a Gagarin😆) para es…
RT @Terrazocultor: Igual que hay "circuitos útiles", hay "programas útiles"
El primer programa serio que hagamos puede ser una base de dato…
RT @ProgressBar201X: 2018 is 18% complete. https://t.co/n9TnzdfxSE



['RT', '@Terrazocultor', ':', '@DiffHell', 'Como', 'dijo', 'un', 'cantante', ':', '"', 'No', 'es', 'el', 'Mercedes', '"', '"', 'Es', 'quién', 'lo', 'conduce', '"']
['RT', '@nobbis', ':', 'Real-time', 'photogrammetry', 'with', '#ARKit', 'https://t.co/4kqnI84ypa']
['RT', '@lrubiogarcia', ':', 'WANT', '.', 'big', 'data', 'de', 'mis', 'nalgas', 'https://t.co/ihb9fE4of4']
['RT', '@OrdureBizarre_', ':', 'https://t.co/ApiwWg1p38']
['RT', '@FreeMemesKids', ':', '😂', 'https://t.co/Cq5YtVgnzi']
['@DiffHell', '@Terrazocultor', 'Tas', 'pasao']
['RT', '@danielegrasso', ':', 'No', ',', 'Albert', 'Rivera', 'no', 'ha', 'dicho', 'que', 'estaría', '"', 'encantado', 'de', 'liderar', 'el', 'movimiento', 'transversal', '"', 'feminista', '.', 'Aquí', 'va', 'la', 'trans', '…']
['RT', '@astro_duque', ':', 'Hace', '50', 'años', '(', '2', 'Marzo', '1968', ')', 'la', 'Unión', 'Soviética', 'envió', 'una', 'nave', 'Saiús', 'a', 'la', 'Luna', 'con', 'un', 'maniquí', '(', 'parecido', 'a', 'Gagarin', '😆', ')', 'para', 'es', '…']
['RT', '@Terrazocultor', ':', 'Igual', 'que', 'hay', '"', 'circuitos', 'útiles', '"', ',', 'hay', '"', 'programas', 'útiles', '"', 'El', 'primer', 'programa', 'serio', 'que', 'hagamos', 'puede', 'ser', 'una', 'base', 'de', 'dato', '…']
['RT', '@ProgressBar201X', ':', '2018', 'is', '18', '%', 'complete', '.', 'https://t.co/n9TnzdfxSE']

Process finished with exit code 0
```

___

Finally, we want to mention that we must be careful with the number of requests made to twitter, since you can be banned 15 minutes:

> 429	Too Many Requests	Returned when a request cannot be served due to the application’s rate limit having been exhausted for  the resource. See Rate Limiting.


```python
Traceback (most recent call last):
  File "/Users/sergiers/PycharmProjects/CLOUD-COMPUTING-CLASS-2018/Lab2/Twitter_2.py", line 27, in <module>
    for status in listStatus:
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/tweepy/cursor.py", line 49, in __next__
    return self.next()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/tweepy/cursor.py", line 197, in next
    self.current_page = self.page_iterator.next()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/tweepy/cursor.py", line 108, in next
    data = self.method(max_id=self.max_id, parser=RawParser(), *self.args, **self.kargs)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/tweepy/binder.py", line 250, in _call
    return method.execute()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/tweepy/binder.py", line 234, in execute
    raise TweepError(error_msg, resp, api_code=api_error_code)
tweepy.error.TweepError: Twitter error response: status code = 429

Process finished with exit code 1
```
