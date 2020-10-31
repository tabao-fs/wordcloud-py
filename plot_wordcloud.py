import json
import sys

from generate_from_frequency import generate_word_cloud, plot_word_cloud
from constants import width, height, dpi, figsize, color

  
def get_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data


if __name__ == "__main__":
    '''
    Plot wordcloud frequency
    '''
    if len(sys.argv) <= 1:
        filename = 'input/sample.json'
        print("Json file was not provided. Sample will be used.")
    else:
        filename = sys.argv[1]

    data = get_data(filename)
    wc = generate_word_cloud(width, height, data)
    plot_word_cloud(figsize, dpi, wc)
