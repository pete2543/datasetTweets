import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "ไอซ์อภิษฎา"
tweets = []
limit = 200


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date,tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'Tweet'])
df.to_csv('.\\tw_api\\tweetsdataไอซ์อภิษฎา..csv')