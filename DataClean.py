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
df = pd.read_csv("TwitterDataUSAbitcoin3rddec.csv")

print("before cleaning Sentiment")
with open ('TwitterDataUSAbitcoin3rddec.csv', encoding ='UTF-8') as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')
    line_count=0
    positive2=0
    for row in csv_reader:
        if(line_count==0):
            line_count=1
        else:
            if(TextBlob(row[1]).polarity>0):
                positive2=positive2+1
            line_count=line_count+1
positive2=positive2/(line_count)*100
print(positive2)
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
day=[]
day=df.created_at[:]
testing = df.Text[:]
test_result = []
for t in testing:
    print("I work")
    test_result.append(tweet_cleaner(t))

line_count2=0
sentiment2=0
neutral=0
positive=0
negative=0
i=0
with open ('TwitterDataUSAbitcoin3rddecSentiment.csv', mode='a+', newline='', encoding='UTF-8') as my_file:
    my_writer = csv.writer(my_file, delimiter=',')
    my_writer.writerow([ 'Text','created_at','sentiment'])


    for item in test_result :

        if(line_count2==0):
            line_count2=1
        else:

            line_count2=line_count2+1
            if(TextBlob(item).polarity > 0):
                positive=positive+1
            elif(TextBlob(item).polarity==0):
                neutral=neutral+1
            else:
                negative=negative+1

        my_writer.writerow([item, day[i], TextBlob(item).polarity])
        i = i + 1


positive=positive/line_count2*100
negative=negative/line_count2*100
neutral=neutral/line_count2*100
print(positive)
print("\n")
print(negative)
print("\n")
print(neutral)