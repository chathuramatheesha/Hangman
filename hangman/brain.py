import random
import words
import art
class Hangman:
    def __init__(self):
        self.word = ''
        self.lives = 6
        self.display = ''

        for _ in range(self.capacity()):
            self.display.append('_')

    def get_display(self):
        return self.display

    def is_guess_in_display(self, guess):
        if guess in self.display:
            return True
        return False

    def is_guess_in_word(self, guess):
        if guess in self.word:
            return True
        return False

    def position(self, guess):
        for position in range(self.capacity()):
            letter = self.word[position]
            if letter == guess:
                self.display[position] = letter

    def capacity(self):
        return len(self.word)

    def minus_life(self):
        self.lives -= 1

    def is_lives_empty(self):
        return not self.lives

    def change_word(self):
        self.word = random.choice(words.word_list)
        self.display = []
        for _ in range(self.capacity()):
            self.display.append('_')

    def is_win(self):
        if "_" not in self.display:
            return True
        return False

    def lives_art(self):
        return art.stages[self.lives]

    def __str__(self):
        return self.word
