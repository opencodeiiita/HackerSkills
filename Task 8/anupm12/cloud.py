from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 
import csv 

file_ob = open(r"HackerSkills\Task 8\anupm12\file.csv") 
reader_ob = csv.reader(file_ob) 
reader_contents = list(reader_ob) 

text = "" 

for row in reader_contents : 
    for word in row : 
        text = text + " " + word 

wordcloud = WordCloud(width=480, height=480, colormap="Oranges_r").generate(text) 

plt.figure() 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off") 
plt.margins(x=0, y=0) 
plt.show() 