import re
from nltk.corpus import brown

FIVE_KB = 5*1024
FIVEHUNDRED_MB = 536870912
ONE_GB = 1073741824

data = ""
urls = []
words = []
excluded_words = ["http", "robots", "html", "index", "https"]
wordlist = set(brown.words())

def read_chunk(file, chunk_size=FIVEHUNDRED_MB):
    while True:
        content = file.read(chunk_size)
        if not content:
            break
        yield content


def add_data(data_chunk):
    global data
    data = data + data_chunk


def read_urls(data_chunk):
    for match in re.finditer('"url":', data_chunk):
        url = data_chunk[match.end() : data_chunk.find('",', match.end())]
        urls.append(url)


def extract_words_from_urls():
    global words
    for url in urls:
        words.append(re.findall(r'\b[^\d\W]+\b', url))
    words = [item for sublist in words for item in sublist if item in wordlist and \
             item not in excluded_words and len(item) > 3]


def get_most_frequent_words(n):
    from collections import Counter

    counter = Counter(words)
    most_frequent = counter.most_common(n)
    return most_frequent


def get_most_frequent_ngrams(n):
    from nltk import ngrams
    from collections import Counter

    ngrams = ngrams(words, n)
    counter = Counter(ngrams)
    most_frequent = counter.most_common(10)
    return most_frequent


def main():
    with open('D:/CommonCrawlData/cdx-00000', mode='r', encoding='utf-8') as f:
        for data_chunk in read_chunk(f):
            #add_data(data_chunk)
            read_urls(data_chunk)
            extract_words_from_urls()
            print(get_most_frequent_words(10))
            print(get_most_frequent_ngrams(3))


if __name__ == "__main__":
    main()