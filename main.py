# game_app.py
import toga
import random

class Game(toga.App):
    def startup(self):
        self.main_box = toga.Box()

        self.label = toga.Label('Guess a number between 1 and 100:')
        self.input = toga.TextInput()
        self.button = toga.Button('Submit', on_press=self.check_guess)

        self.main_box.add(self.label)
        self.main_box.add(self.input)
        self.main_box.add(self.button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

        self.secret_number = random.randint(1, 100)

    def check_guess(self, widget):
        try:
            guess = int(self.input.value)
            if guess == self.secret_number:
                self.label.text = 'Congratulations! You guessed the number.'
            elif guess < self.secret_number:
                self.label.text = 'Too low! Try again.'
            else:
                self.label.text = 'Too high! Try again.'
        except ValueError:
            self.label.text = 'Invalid input. Enter a number between 1 and 100.'

def main():
    return Game()

if __name__ == '__main__':
    main().main_loop()
