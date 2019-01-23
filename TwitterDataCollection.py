from textblob import TextBlob
import tweepy
import csv
import pandas as pd
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer
import regex as re
import lxml
tok = WordPunctTokenizer()
pat1 = r'@[A-Za-z0-9]+'
pat2 = r'https?://[A-Za-z0-9./]+'
combined_pat = r'|'.join((pat1, pat2))



consumer_key = 'lf8uIky58rDZG5FatANoHGF5U'
consumer_secret = 'aZSe1Vjys7r7UrFhDfqppt3UP1Gjpps0y6g2AYHaAqRNU0mWYN'
access_token = '753845369956478976-GotFc7FPl7HZe6b7NYwRCr1DkzNc2cX'
access_token_secret = 'aaMZp4QGxeBiCbCKUWsSaEqScg3IdsPAhEVYKtn5zFXaC'
auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)

#fetch_tweets=tweepy.Cursor(api.search, q='bitcoin').items(5)
#for i in fetch_tweets:
    #print(i)
    #print(i.text)
    #print("\n")

#fetch_tweets2 = t
# weepy.Cursor(api.search, q='bitcoin', geocode='61.52401,105.318756,100km').items(5)




with open ('TwitterDataaustralialitecoin3rddec.csv', mode='a+', newline='', encoding='UTF-8') as my_file:
    my_writer = csv.writer(my_file, delimiter=',')
    my_writer.writerow(['TweetID', 'Text', 'user_screen_name','created_at'])
    fetch_tweets2 = tweepy.Cursor(api.search, q='litecoin', created_at='20/11/2018', geocode='-25.2744,133.7751,1000km').items(10000)

    for i2 in fetch_tweets2:
        print("this works")
        current_ID = str(i2.id)
        current_Txt = str(i2.text)
        user_screen_name = str(i2.user.screen_name)
        created_at = str(i2.created_at)

        my_writer.writerow([current_ID, current_Txt, user_screen_name, created_at])

with open('TwitterDataaustralialitecoin3rddec.csv', mode='r', encoding='UTF-8') as my_file2:
    csv_reader = csv.reader(my_file2, delimiter=',')
    line_count=0
    for row in csv_reader:
        print("---------")
        print(row[0])
        print(row[1])
        print(row[2])
        print("----------")
print("hi")

with open ('TwitterDataaustralialitecoin3rddec.csv', encoding ='UTF-8') as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')
    line_count=0
    sentiment=0
    for row in csv_reader:
        if(line_count==0):
            line_count=1
        else:

            print(row[1])
            sentiment= sentiment+ TextBlob(row[1]).polarity
            print(sentiment)
            line_count=line_count+1
final=sentiment/(line_count-1)
print(final)

df = pd.read_csv("TwitterDataaustralialitecoin3rddec.csv")


def tweet_cleaner(text):
    soup = BeautifulSoup(text, 'lxml')
    souped = soup.get_text()
    stripped = re.sub(combined_pat, '', souped)
    try:
        clean = stripped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        clean = stripped
    letters_only = re.sub("[^a-zA-Z]", " ", clean)
    lower_case = letters_only.lower()
    # During the letters_only process two lines above, it has created unnecessay white spaces,
    # I will tokenize and join together to remove unneccessary white spaces
    words = tok.tokenize(lower_case)
    return (" ".join(words)).strip()

testing = df.Text[:100]
test_result = []
for t in testing:
    print("I work")
    test_result.append(tweet_cleaner(t))
print(test_result)
line_count2: int=0
sentiment2=0
for item in test_result :
    if(line_count2==0):
        line_count2=1
    else:

        print(item)
        sentiment2= sentiment2+ TextBlob(item).polarity
        print(sentiment2)
        line_count2=line_count2+1
final2=sentiment2/(line_count2-1)
print(final2)








