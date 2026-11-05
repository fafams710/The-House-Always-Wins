import sys

import torch

SEED = 42


def init_params():
    ...


def simulate(n_players, start, bet, p_win, max_rounds):
    torch.manual_seed(SEED)

    bankroll_t = torch.full((n_players,), start)
    history_t = torch.zeros((n_players, max_rounds + 1))

    history_t[:, 0] = bankroll_t

    for r in range(max_rounds):
        gamble_t = torch.rand((n_players, ))

        win_t = gamble_t < p_win


def main():
    players = 10000
    starting_bankroll = 1000
    bet = 50
    p_win = 18 / 37
    max_rounds = 1000

    history = simulate(players, starting_bankroll, bet, p_win, max_rounds)

    return 0


if __name__ == "__main__":
    sys.exit(main())
