
class Word:
    def __init__(self, word, goal):
        self.word = word
        self.goal = goal


# Singleton class
class Game:

    __instance = None

    @staticmethod
    def getInstance():
        if Game.__instance == None:
            Game()
        return Game.__instance
    
    def __init__(self):
        if Game.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Game.__instance = self

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

        self.sentences.append(words)