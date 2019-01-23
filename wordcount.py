import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import  OrderedDict
import operator

final_dictionary={}

with open( 'TwitterDataaustraliaxrp3rddec.csv', encoding= "UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count=0

    for row in csv_reader:
        if line_count==0:
            line_count=line_count+1
        else:
            txt= row[1]
            final_txt= txt.lower()
            stop_words= set(stopwords.words('english'))
            pattern = r'\w+'

            tokenizer= RegexpTokenizer(pattern)
            word_tokens=tokenizer.tokenize(final_txt)
            filtered_sentence=[v for v in word_tokens if not v in stop_words]
            for v in filtered_sentence:
                if v not in final_dictionary:
                    final_dictionary[v]=1
                else:
                    final_dictionary[v]=final_dictionary[v]+1






            line_count=line_count+1
sorted_dictionary= sorted(final_dictionary.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_dictionary)

with open('wordcountaustraila.csv', mode='a+', newline='', encoding='UTF-8' ) as my_file:
    my_writer = csv.writer(my_file, delimiter=',')
    my_writer.writerow(['Word', 'Count'])
    for key in sorted_dictionary:
        current_word=key[0]
        current_count=key[1]
        my_writer.writerow([current_word, current_count])




