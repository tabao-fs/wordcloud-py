import json

from generate_from_frequency import generate_word_cloud, plot_word_cloud
from constants import width, height, dpi, figsize, color

  
def get_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data


if __name__ == "__main__":
    filename = 'input/sample.json'
    data = get_data(filename)
    wc = generate_word_cloud(width, height, data)
    plot_word_cloud(figsize, dpi, wc)
