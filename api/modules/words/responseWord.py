class Response:
    isValid = {
        'isValid': False,
        'quantity': 0
    }

    def validLetter(self, word, userLetter):
        i = 0
        for letter in word:
            if userLetter == letter:
                i += 1
                self.isValid['quantity'] = i
                self.isValid['isValid'] = True
        return self.isValid
