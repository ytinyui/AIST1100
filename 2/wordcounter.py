import string as s
import re

STOPWORD_FILENAME = "stopwords.txt"


def top_words(fl, n=10):

    def filter(ls, filter_words):
        result = []
        for x in ls:
            if not x.lower() in filter_words:
                result.append(x)
        return result

    with open(STOPWORD_FILENAME, 'r') as f:
        stopwords = f.read().rsplit(',')  # return list of stopwords
    with open(fl, 'r') as f:
        # return list of words from text (with numbers, without punctuation)
        words = re.sub(r'[^\w\s]', ' ', f.read()).rsplit()

    words = filter(words, stopwords)
    # remove words with numbers
    for x in words:
        if any([str(i) in x for i in range(10)]):
            words.remove(x)
    words = filter(words, list(s.ascii_letters))
    # count words
    w_count = []
    for x in words:
        if w_count.count([x, words.count(x)]) == 0:
            w_count.append([x, words.count(x)])
    w_count.sort(key=lambda x: -x[1])

    return {w_count[i][0]: w_count[i][1] for i in range(n if n < len(w_count) else len(w_count))}


if __name__ == '__main__':
    print(top_words('dummy.txt', n=5))
