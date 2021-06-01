import pandas


class Game:
    def __init__(self):
        self.state_data = pandas.read_csv("50_states.csv")
        self.score = 0

    def take_guess(self, guess):
        guess = guess.title()
        if guess in self.state_data.state.to_list():
            x = self.state_data[self.state_data.state == guess].x
            y = self.state_data[self.state_data.state == guess].y
            self.score += 1
            return (int(x), int(y))
        else:
            return False
