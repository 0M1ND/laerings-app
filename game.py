
class Word:
    def __init__(self, word, goal):
        self.word = word
        self.goal = goal


class Game:
    def __init__(self):
        self.sentences = []

    def sentence_to_string(self, sentence):
        return " ".join([word.word for word in sentence])

    def add_sentence(self, sentence):
        # En sætning kan se sådan her ud
        # Jeg(O) spiser(X) aftensmad når jeg(O) kommer(X) hjem.
        words = []
        for w in sentence.split(" "):
            # Check om ordet har enten (X) eller (O) i sig
            if w.find("(X)") != -1:
                # Fjern (X) fra ordet
                w = w.replace("(X)", "")
                words.append(Word(w, "X"))
            elif w.find("(O)") != -1:
                # Fjern (O) fra ordet
                w = w.replace("(O)", "")
                words.append(Word(w, "O"))
            else:
                words.append(Word(w, None))

        print(words)
        self.sentences.append(words)