from tkinter import messagebox
class Word:
    def __init__(self, word, goal):
        self.word = word
        self.goal = goal
        self.guess = None


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
        self.current_sentence = 0
        self.current_word = 0

    # Den går et ord tilbage, så det det der sker når du trykker på backspace.
    def prev_word(self):
        self.current_word -= 1
        if self.current_word < 0:
            self.current_sentence -= 1
            if self.current_sentence < 0:
                self.current_sentence = 0
                self.current_word = 0
            else:
                self.current_word = len(self.sentences[self.current_sentence]) - 1

    # Tjekker om setningen er korekt og gir fejlne 
    def is_correct(self):
        errors = []
        for word in self.sentences[self.current_sentence]:
            if word.guess != None and word.guess != word.goal:
                errors.append("Du satte et forkert symbol på ordet " + word.word)
            
            if word.guess == None and word.goal != None:
                errors.append("Du glemte at sætte et " + word.goal + " på ordet " + word.word)

        return errors

    # Den går til næste setning hvis der en og hvis du har gætede rigtigt på alle ordne.
    def next_sentence(self):
        errors = self.is_correct()

        if len(errors) > 0:
            messagebox.showerror("Fejl", "\n".join(errors))
            self.current_word = 0
            return
        else:
            messagebox.showinfo("Succes", "Du gættede alle ordene korrekt!")
        

        self.current_word = 0
        self.current_sentence += 1

    # Den går til det næste ord.
    def next_word(self):
        self.current_word += 1
        if self.current_word >= len(self.sentences[self.current_sentence]):
            self.next_sentence()
        else: 
            self.guess(None)
    # Den gætter på hvad ordet skal være på. så det det der sker når du trykker på x og o
    def guess(self, guess):
        self.sentences[self.current_sentence][self.current_word].guess = guess

    def get_current_sentence(self):
        if self.current_sentence >= len(self.sentences):
            return None
        return self.sentences[self.current_sentence]

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