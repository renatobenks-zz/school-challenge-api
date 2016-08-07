class Response:
    isValid = {}

    def validLetter(self, word, userLetter):
        i = 0
        self.isValid['isValid'] = False
        self.isValid['quantity'] = 0
        if userLetter in word:
            self.isValid['isValid'] = True
            self.isValid['quantity'] = word.count(userLetter)
        return self.isValid
