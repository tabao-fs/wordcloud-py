import os
import random
import matplotlib.pyplot as plt
import numpy as np

from io import StringIO
from os import path
from PIL import Image

from wordcloud import WordCloud


width = 1280
height = 720
dpi = 96
figsize = (width/dpi, height/dpi)
color = [
    'hsl(205, 68%, 31%)',
    'hsl(213, 70%, 35%)',
    'hsl(220, 70%, 35%)',
    'hsl(220, 65%, 35%)',
    'hsl(215, 60%, 35%)',
    'hsl(240, 80%, 35%)'
]


def deep_purple_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return color[random.randint(0, len(color) - 1)]


def generate_word_cloud(width, height, data):
    wc = WordCloud(
        width=width,
        height=height,
        background_color='white',
    )
    wc.generate_from_frequencies(frequencies=data)

    return wc


def plot_word_cloud(figsize, dpi, wc):
    plt.figure(figsize=figsize, dpi=dpi)
    plt.axes([0,0,1,1])
    plt.imshow(wc.recolor(color_func=deep_purple_func), interpolation='nearest', aspect='equal')
    plt.axis('off')
    plt.show()


def save_word_cloud_fig(figsize, dpi, wc, filename):
    plt.figure(figsize=figsize, dpi=dpi)
    plt.axes([0,0,1,1])
    plt.imshow(wc.recolor(color_func=deep_purple_func), interpolation='nearest', aspect='equal')
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=dpi)


def get_word_cloud_svg(figsize, dpi, wc):
    img_data = StringIO()
    plt.figure(figsize=figsize, dpi=dpi)
    plt.axes([0,0,1,1])
    plt.imshow(wc.recolor(color_func=deep_purple_func), interpolation='nearest', aspect='equal')
    plt.axis('off')
    plt.savefig(img_data, format='svg', bbox_inches='tight', pad_inches=0, dpi=dpi)
    img_data.seek(0)

    return img_data.getvalue()


def create_word_cloud(data):
    wc = generate_word_cloud(width, height, data)
    plot_word_cloud(figsize, dpi, wc)


def get_mask(filename):
    d = path.dirname(__file__)
    mask = np.array(Image.open(path.join(d, filename)))
    return mask


if __name__ == "__main__":
    data = {
        'One': 7,
        'Two': 3,
        'Three': 2,
        'Four': 1
    }
    create_word_cloud(data)
