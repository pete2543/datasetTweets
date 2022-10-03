import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
import emoji
from nltk.tokenize import regexp_tokenize
#from nltk.tokenize import word_tokenize
from pythainlp.tokenize import word_tokenize
from cleantext import clean

df = pd.DataFrame({'id':[1,2,3,4,5,6],
                   'text':['Oh no Monday','Oh no Monday','Gotcha 🇫🇷!',
                           'Coffee, please😁','Coffee, please 😁','Mails 🌎'],
                   'dates':['2019-05-30T17:48:45+0000','2019-05-30T17:48:45+0000',
                           '2019-05-25T19:40:43+0000','2019-03-30T14:41:20+0000',
                           '2019-03-30T14:41:20+0000','2019-04-10T19:50:49+0000'],
                   'group':['meme','humour','meme','gif','gif','meme'],
                   'theme':['light','light','funny','dark','sad','funny']})

pat = r'[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]|[\U0001F1E0-\U0001F1FF]'

df['text'].str.replace(pat, '', regex=True)
print(df)