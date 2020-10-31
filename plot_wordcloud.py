from generate_from_frequency import generate_word_cloud, plot_word_cloud

from constants import width, height, dpi, figsize, color


if __name__ == "__main__":
    data = {
        'One': 7,
        'Two': 3,
        'Three': 2,
        'Four': 1
    }
    wc = generate_word_cloud(width, height, data)
    plot_word_cloud(figsize, dpi, wc)
