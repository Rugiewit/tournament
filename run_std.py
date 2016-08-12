import axelrod as axl
import random
import os

turns = 200
repetitions = 100
processes = 0
seed = 1
filename = "data/strategies_std_interactions.csv"

if __name__ == "__main__":
    # Deleting the file if it exists
    try:
        os.remove(filename)
    except OSError:
        pass

    random.seed(seed)  # Setting a seed

    players = [s() for s in axl.ordinary_strategies]
    tournament = axl.Tournament(players, turns=turns, repetitions=repetitions)

    tournament.play(filename=filename, processes=processes)
