from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import urllib
import requests
import numpy as np
import matplotlib.pyplot as plt




input = 'India is my country and I proud to be an Indian. It ranks as the seventh largest country of the world as well as second most populated country of the world. It is also known as Bharat, Hindustan and Aryavart. It is a peninsula means surrounded by oceans from three sides such as Bay of Bengal in east, Arabian Sea in west and Indian Ocean in south. The national animal of India is tiger, national bird is peacock, national flower is lotus and national fruit is mango. The flag of India has tricolor, saffron means purity (the uppermost), white means peace (the middle one having an Ashok Chakra) and green means fertility (the lowest one). Ashok Chakra contains equally divided 24 spokes. The national anthem of India is “Jana Gana Mana”, the national song is “Vande Mataram” and national sport is Hockey.India is a country where people speak many languages and people of different castes, creeds, religions and cultures live together. That’s why India is famous for common saying of “unity in diversity”. It is well known as the land of spirituality, philosophy, science and technology. People of various religions like Hinduism, Buddhism, Jainism, Sikhism, Islam, Christianity and Judaism lives here together from the ancient time. It is famous country for its agriculture and farming which are the backbones of it from the ancient time. It uses it own produced food grains and fruits. It is a famous tourist’s paradise because it attracts people’s mind from all over the world. It is rich in monuments, tombs, churches, historical buildings, temples, museums, scenic beauty, wild life sanctuaries, places of architecture, etc are the source of revenue to it.It is the place where Taj Mahal, Fatehpur Sikri, golden temple, Qutab Minar, Red Fort, Ooty, Nilgiris, Kashmir, Kajuraho, Ajanta and Ellora caves, etc wonders exist. It is the country of great rivers, mountains, valleys, lakes and oceans. The national language of India is Hindi. It is a country where 29 states and UTs. It has 28 states which again have many small villages. It is a chief agricultural country famous for producing sugarcane, cotton, jute, rice, wheat, cereals etc crops. It is a country where great leaders (Shivaji, Gandhiji, Nehru, Dr. Ambedkar, etc), great scientists (Dr. Jagadeeshchandra Bose, Dr Homi Bhabha, Dr. C. V Raman, Dr. Naralikar, etc) and great reformers (Mother Teresa, Pandurangashastri Alhavale, T. N. Sheshan) took birth. It is a country where diversity exists with strong unity and peace.'


mask = np.array(Image.open( r'C:\Users\ok\Pictures\map.png'))

 
def generate_wordcloud(input, mask):
    word_cloud = WordCloud(width = 512, height = 512, background_color='white', stopwords=STOPWORDS, mask=mask).generate(input)
    plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    
generate_wordcloud(input, mask)
