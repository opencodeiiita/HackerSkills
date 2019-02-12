from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib
import matplotlib.pyplot as plt

#%matplotlib inline
matplotlib.rcParams['figure.figsize'] = (16.0, 9.0)
script = open("spiderman.txt").read()
stopwords = set(STOPWORDS)
spiderman_action = np.array(Image.open("spiderman.png"))


from matplotlib.colors import LinearSegmentedColormap
colors = ["#DF1F2D", "#B11313", "#2B3784", "#447BBE", "#a71814", "#0a2b4e"]
cmap = LinearSegmentedColormap.from_list("mycmap", colors)

wc = WordCloud(background_color="white", stopwords=stopwords, mask=spiderman_action, width=446, height=640, colormap=cmap,contour_width=40, contour_color='black')
wc.generate(script)
plt.figure(figsize=[10,15])
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0,y=0)
plt.show()

