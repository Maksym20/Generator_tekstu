import numpy as np
import glob, os



class Markov():
    text = ''
    generated_text = ''
    words_dict = {}
    words_array = []

    def __init__(self, path):
        if path.endswith('.txt'):
            with open(path, encoding='utf8') as f:
                self.text = f.read()
        elif path.endswith('/'):
            text_files = [path + text_file for text_file in os.listdir(path) if text_file.endswith('.txt')]
            for text_file in text_files:
                with open(text_file, encoding='utf8') as f:
                    print(text_file)
                    self.text += "\n " + f.read()
        else:
            raise Exception('Allowed only *.txt files')

        self.words_array = self.text.split()
        self.pairs = self._make_pairs(self.words_array)

        for word_key, word_value in self.pairs:
            if word_key in self.words_dict.keys():
                self.words_dict[word_key].append(word_value)
            else:
                self.words_dict[word_key] = [word_value]

    def Generate(self, n_words = 100):
        first_word = np.random.choice(self.words_array)
        while first_word.islower():
            first_word = np.random.choice(self.words_array)

        chain = [first_word]

        for i in range(n_words):
            chain.append(np.random.choice(self.words_dict[chain[-1]]))

        self.generated_text = ' '.join(chain)
        self.generated_text = self.generated_text.replace('.','.\n')
        return self.generated_text

    def _make_pairs(self, words_array):
        for i in range(len(words_array)-1):
            yield (words_array[i], words_array[i+1])

markv = Markov('text.txt')
# markv = Markov('texts/')

g_text = markv.Generate(n_words = 200)
print(g_text)

