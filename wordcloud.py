import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud
import string

import matplotlib.pyplot as plt
# Start with one review:
df = pd.read_csv("wordcountaustraila.csv")

text = df.Word[1:100]
word=[]
for t in text:
    print(t)
    if(t=='rt'):
        continue
    if(t!='https'):
        word.append(t)
makeword=" ".join(str(k) for k in word)


# Create and generate a word cloud image:
wordcloud = WordCloud().generate(makeword)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()