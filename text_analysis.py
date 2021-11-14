import os
import sys
from collections import Counter
import nltk
import webcolors


def is_color(word, pos):
    """Gets a list of tagged words, returns only colors"""
    colors_list = list(webcolors.CSS3_NAMES_TO_HEX.keys())
    return pos[:2] == 'JJ' and word in colors_list


def main(file_name):
    txt = ""
    num_lines = 0
    words_tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    words_from_txt_file = []
    with open(file_name, encoding='ISO-8859-1', mode='r') as txt_file:
        # reads all lines to a text object, count lines.
        for line in txt_file:
            if line.strip():
                txt += line
                num_lines += 1
                # apply lower() only for words_list items for finding unique words
                # use the text to tokenize to words and to tokenize to sentences.
                words_from_txt_file += [i.lower() for i in words_tokenizer.tokenize(line)]
        # use tokenized words list for counting words, unique words and colors:
        num_words = len(words_from_txt_file)
        num_unique_words = len(set(words_from_txt_file))
        colors_list = list(webcolors.CSS3_NAMES_TO_HEX.keys())
        is_adjective = lambda pos: pos[:2] == 'JJ'
        colors = [word for (word, pos) in nltk.pos_tag(words_from_txt_file) if
                  is_adjective(pos) and word in colors_list]
        colors_count = Counter(colors)
        # use tokenized sentences list to find sentence average length, and maximum sentence length.
        # (in words and in characters. A sentence is a group of words ending with a '.'/ '!'/ '?'/ end of file)
        sentences_from_txt = nltk.tokenize.sent_tokenize(txt)
        avg_sent_len = float(num_words / len(sentences_from_txt))
        max_sentence = str(max(sentences_from_txt, key=len))
        max_sentence_words = len(max_sentence.split())
        max_sentence_chars = len(max_sentence)
        counter = Counter(words_from_txt_file)
        most_occur = counter.most_common(1)
        stop_words = nltk.corpus.stopwords.words('english')
        counter_non_gramatical = Counter([w for w in words_from_txt_file if not w in stop_words])
        most_occur_non_grammatical = counter_non_gramatical.most_common(1)
        sep = "---------------------------------------------"
        print("{0}{9}{0}number of lines:    {1}.{0}{9}{0}number of words:    {2}.{0}{9}{0}number of unique words:  {3}."
              "{0}{9}{0}average sentence length:  {4} words.{0}{9}{0}longest sentence length:    {5} words, {6}"
              "characters.{0}{9}{0}most popular word:    {7}.{0}{9}{0}most popular non grammatical word :    "
              "{8}.".format("\n\n", str(num_lines), str(num_words), str(num_unique_words),
                            str(avg_sent_len),
                            str(max_sentence_words),
                            str(max_sentence_chars),
                            str(most_occur[0]), str(most_occur_non_grammatical[0]), sep))
        for key, value in colors_count.items():
            print(key, value)


if __name__ == '__main__':
    input_path = ""
    if len(sys.argv) == 1:
        print("\nEnter a file path\n")
        input_path = input()
    elif len(sys.argv) > 2:

        print('You have specified too many arguments')
        sys.exit()
    elif 0 < len(sys.argv) < 2:
        print('You need to specify the path to be listed')
        sys.exit()
    else:
        input_path = sys.argv[1]
    if not input_path.endswith(".txt") or os.path.isdir(input_path):
        print('The path specified does is not a text file')
        sys.exit()
    main(input_path)
