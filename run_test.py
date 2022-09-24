import axelrod as axl
import os
import utils

players = [s() for s in axl.paper_strategies]  # Create players


turns = 500
repetitions = 500
seed = 1
filename = "data/strategies_test_interactions.csv"
processes = 8
def main(players=players):
    # Deleting the file if it exists
    try:
        os.remove(filename)
    except OSError:
    
        pass

    tournament = axl.Tournament(players, turns=turns, repetitions=repetitions, seed=seed)

    results = tournament.play(filename=filename)
    utils.obtain_assets(results, "strategies", "tst")
    results.write_summary('assets/test_summary.csv')

if __name__ == "__main__":
    main()
