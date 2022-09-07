import axelrod as axl
import os
import utils

players = [s() for s in axl.test_strategies]  # Create players

turns = 200
repetitions = 100

processes = 20
seed = 1
filename = "data/strategies_test_interactions.csv"

def main(players=players):
    # Deleting the file if it exists
    try:
        os.remove(filename)
    except OSError:
        pass

    tournament = axl.Tournament(players, turns=turns, repetitions=repetitions, seed=seed)

    results = tournament.play(filename=filename, processes=processes)
    utils.obtain_assets(results, "strategies", "std")
    results.write_summary('assets/test_summary.csv')

if __name__ == "__main__":
    main()
