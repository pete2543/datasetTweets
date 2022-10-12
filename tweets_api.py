import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
import emoji
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import word_tokenize
from pythainlp.tokenize import word_tokenize
from cleantext import clean
tert=[]
query = "โหนกระแส"
tweets = []
limit = 400

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
         tweets.append([tweet.date, tweet.username, tweet.content])

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                           "]+", flags=re.UNICODE)

tweet_noemoji=emoji_pattern.sub(r'',str(tweets))

# Cleaning text from unused characters
def clean_text(text):
# removing urls
    text = str(text).replace(r'https[\w:/\.]+', ' ')
    # remove everything except characters and punctuation
    text = str(text).replace(r'[^\.\w\s]', ' ')
    text = str(text).replace('[^a-zA-Z]', ' ')
    text = str(text).replace(r'\s\s+', ' ')
    text = text.lower().strip()
    return text

text = re.sub(r'https[\w:/\.|\?|\!]+', '', tweet_noemoji, flags=re.MULTILINE)
df = pd.DataFrame(eval(text),columns=['Date', 'User', 'Tweet'])
print(text)

#โหลด CSV
df.to_csv('.\\tw_api\\tweetsdataโหนกระแส.csv')