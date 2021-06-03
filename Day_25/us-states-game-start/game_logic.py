import pandas


class Game:
    def __init__(self):
        self.state_data = pandas.read_csv("50_states.csv")
        self.score = 0
        self.guessed_states = []

    def take_guess(self, guess):
        #guess = guess.title()
        if guess in self.state_data.state.to_list():
            if not guess in self.guessed_states:
                x = self.state_data[self.state_data.state == guess].x
                y = self.state_data[self.state_data.state == guess].y
                state_coords = (int(x), int(y))
                self.score += 1
                self.guessed_states.append(guess)
                return state_coords
            else:
                return False
        else:
            return False

    def generate_states_to_learn_csv(self):
        states_to_learn = self.state_data[~self.state_data.state.isin(
            self.guessed_states)]
        states_to_learn.state.to_csv("states_to_learn.csv")
