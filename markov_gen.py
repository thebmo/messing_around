"""
    This has been forked and altered from original source:
    https://gist.github.com/agiliq/131679
    Alterations are in the generate_markov_text() method
    allowing for manual seeding as well as "proper" use
    of capitalization and punction.
"""
import random

class Markov(object):

    def __init__(self, open_file):  
        self.cache = {}
        self.open_file = open_file
        self.words = self.file_to_words()
        self.word_size = len(self.words)
        self.database()


    def file_to_words(self):
        self.open_file.seek(0)
        data = self.open_file.read()
        words = data.split()
        return words


    def triples(self):
        """ Generates triples from the given data string. So if our string were
                "What a lovely day", we'd generate (What, a, lovely) and then
                (a, lovely, day).
        """

        if len(self.words) < 3:
            return

        for i in range(len(self.words) - 2):
            yield (self.words[i], self.words[i+1], self.words[i+2])

    def database(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]

    def generate_markov_text(self, size=50, seed_phrase=None):
        
        punctuation = { '.', '?', '!' }
        
        seed = random.randint(0, self.word_size-3)
        seed_word, next_word = self.words[seed], self.words[seed+1]
        w1, w2 = seed_word, next_word
        
        if seed_phrase:
            seed_phrase = seed_phrase.split(' ')
            if len(seed_phrase) > 2:
                w1 = random.choice(seed_phrase)
                seed_phrase.remove(w1)
                w2 = seed_phrase[1]
        gen_words = []
        
        try:
            for i in xrange(size):
                gen_words.append(w1)
                w1, w2 = w2, random.choice(self.cache[(w1, w2)])
                if w2[-1] in punctuation:
                    break
            gen_words.append(w2)
            
            sentence =' '.join(gen_words)
            
        except KeyError as e:
            sentence = self.generate_markov_text(size)
        
        finally:
            if sentence[-1] not in punctuation:
                sentence += random.choice(list(punctuation))
            if sentence[0].islower():
                L = sentence[0].upper()
                sentence = ''.join((L, sentence[1:]))
            return sentence
