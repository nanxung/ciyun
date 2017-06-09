#coding:utf-8
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
def ciyun(file):
    d = path.dirname(__file__)

    # Read the whole text.
    text = open(path.join(d, 'wordcy')).read()

    #    read the mask / color image taken from
    # http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
    alice_coloring = np.array(Image.open(path.join(d, file)))
    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
               font_path='myas.ttf',  # 设置字体格式，如不设置显示不了中文
               stopwords=stopwords, max_font_size=80, random_state=42)
# generate word cloud
    wc.generate(text)

# create coloring from image
    image_colors = ImageColorGenerator(alice_coloring)

# show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
#     plt.figure()
# # recolor wordcloud and show
# # we could also give color_func=image_colors directly in the constructor
#     plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
#     plt.axis("off")
#     plt.figure()
#     plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
#     plt.axis("off")
#     plt._imsave('cy.png')
    plt.savefig('cy.png')

