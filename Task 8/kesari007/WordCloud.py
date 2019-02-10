import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

myfile = open('MyTextFile.txt',encoding='utf-8')

# Contains all the lines in the form of a single string
mystr = myfile.read()

tokens = mystr.lower().split()
for i in range(len(tokens)):
    tokens[i] = re.sub(r"[^a-z]"," ",tokens[i]).strip()
my_str = " ".join(tokens)
wordcloud = WordCloud(width=500, height=500, colormap="Oranges_r").generate(my_str) 
# plot the WordCloud image  

plt.figure(figsize=(6,6)) 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.title("Shakespeare-Verse wordcloud")
plt.axis("off") 
plt.margins(x=0, y=0) 
plt.savefig("WordCloud.png")
plt.show() 
