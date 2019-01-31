import sys
from os import path
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import random

currdir = path.dirname(__file__)

def wiki(query):
	title = wikipedia.search(query)[0]
	page = wikipedia.page(title)
	return page.content

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(152, 95%%, %d%%)" % random.randint(40, 100)

def create_wordcloud(text):
	mask = np.array(Image.open(path.join(currdir, "github.png")))


	# print(text)
	# print(mask)
	stopwords = set(STOPWORDS)
	wc = WordCloud(background_color="#2d3436",
					max_words=200,
					mask=mask,
	               	stopwords=stopwords,
					margin=10,
               		random_state=1)
	wc.generate(text)


	plt.title("Github")
	plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
	           interpolation="bilinear")
	wc.to_file(path.join(currdir, "output.png"))
	plt.axis("off")
	plt.show()

create_wordcloud(wiki("Github"))
