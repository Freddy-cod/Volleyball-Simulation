from random import * # Import random

def print_intro():
    print("This program simulates a game of volleyball between two")
    print('team called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")


def get_inputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. team A wins a serve? "))
    b = float(input("What is the prob. team  B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n


def sim_n_games(n, prob_a, prob_b):
    # Simulates n games of volleyball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    wins_a = wins_b = 0
    games = 0
    while wins_a <= n / 2 and wins_b <= n / 2:
        games += 1
        if games % 2 == 0:
            score_a, score_b = sim_one_game(prob_a, prob_b, 'A')

        else:
            score_a, score_b = sim_one_game(prob_a, prob_b, 'B')

        if score_a > score_b:
            wins_a = wins_a + 1
        else:
            wins_b = wins_b + 1
        return wins_a, wins_b


def sim_one_game(prob_a, prob_b, serving):
    # Simulates a single game or volleyball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B

    score_a = 0
    score_b = 0
    while not game_over(score_a, score_b):
        if serving == "A":
            if random() < prob_a:
                scoreA = score_a + 1
            else:
                serving = "B"
        else:
            if random() < prob_b:
                score_b = score_b + 1
            else:
                serving = "A"
        return score_a, score_b


def game_over(a, b):
    # a and b represent scores for a volley ball game
    # Returns True if the game is over, False otherwise.
    return (a >= 25 and a - b >= 2) or (b >= 25 and b - a >= 2)


def print_summary(wins_a, wins_b):
    # Prints a summary of wins for each player.
    n = wins_a + wins_b
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1: 0.1%})".format(wins_a, wins_a / n))
    print("Wins for B: {0} ({1: 0.1%})".format(wins_b, wins_b / n))
