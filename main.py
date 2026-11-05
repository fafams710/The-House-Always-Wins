import sys

import torch

SEED = 42


def init_params():
    ...


def simulate(n_players, start, bet, p_win, max_rounds):
    torch.manual_seed(SEED)

    bankroll_t = torch.full((n_players,), start)
    history_t = torch.zeros((n_players, max_rounds + 1))
    total_bet = 0
    total_winnings = 0
    p_lose = 1 - p_win
    history_t[:, 0] = bankroll_t

    for r in range(max_rounds):
        gamble_t = torch.rand((n_players, ))

        active_player_t = bankroll_t > 0

        win_t = active_player_t & (gamble_t < p_win)

        bet_t = torch.where(win_t, bet, -bet)

        winnings_t = torch.where(active_player_t, bet_t, 0)

        bankroll_t += winnings_t

        total_bet += active_player_t.sum() 

        total_winnings += winnings_t.sum()

        history_t[:, r + 1] = bankroll_t

        average = total_winnings / total_bet
        
        ev_theory = (p_win * bet) + (p_lose * -bet)

        difference = (average - ev_theory)

        if (r + 1) in [1000]:
            print(f"Average: {average:.2f}")
            print(f"Estimated Theoretical Value: {ev_theory:.2f}")
            print(f"Difference: {difference :.2f}")


        if (r + 1 ) in [100,500,1000]:
            p_lose = 1 - p_win
            new_history = history_t[:,: r + 2]
            eliminated_players = (bankroll_t == 0 ).sum()
            eliminated_players_percentage = (eliminated_players / n_players ) * 100
            changes = torch.diff(new_history, dim=1)
            average = torch.mean(changes)

            print(f"Round {r + 1}: {eliminated_players_percentage}%")

        
            
    return history_t


def main():
    players = 10000
    starting_bankroll = 1000
    bet = 50
    p_win = 18 / 37
    max_rounds = 1000

    history = simulate(players, starting_bankroll, bet, p_win, max_rounds)

    print(history)

    return 0


if __name__ == "__main__":
    sys.exit(main())
