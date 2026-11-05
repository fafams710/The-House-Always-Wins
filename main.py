import sys

import torch
from visualization import generate_visualization

SEED = 42


def simulate(n_players, start, bet, p_win, max_rounds):
    torch.manual_seed(SEED)

    bankroll_t = torch.full((n_players,), start)
    history_t = torch.zeros((n_players, max_rounds + 1))

    history_t[:, 0] = bankroll_t

    for r in range(max_rounds):
        gamble_t = torch.rand((n_players, ))

        active_player_t = bankroll_t > 0

        win_t = active_player_t & (gamble_t < p_win)

        bet_t = torch.where(win_t, bet, -bet)

        winnings_t = torch.where(active_player_t, bet_t, 0)

        bankroll_t += winnings_t

        history_t[:, r + 1] = bankroll_t

    return history_t

def statistical_analysis(history_t, n_players, bet, p_win,check_rounds = [100, 500, 1000] ):


    p_lose = 1 - p_win
    starting_bankroll = history_t[:, 0].mean().item()
    ev_theory = (p_win * bet) + (p_lose * -bet)
    active_players = history_t[:, :-1] > 0
    changes = torch.diff(history_t, dim=1)
    new_changes = changes[active_players]
    average = new_changes.mean().item()
    difference = average - ev_theory
    print(f"Average: {average:.2f}")
    print(f"Estimated Theoretical Value: {ev_theory:.2f}")
    print(f"Difference: {difference :.2f}")

    for n in (check_rounds):

        eliminated_players = (history_t[:, n] == 0).sum().item()
        eliminated_players_percentage = (eliminated_players / n_players ) * 100

        print(f"Round {n}: {eliminated_players_percentage:.2f}% eliminated")

    final_bankroll = history_t[:, -1]
    players_above_bankroll = (final_bankroll > starting_bankroll).sum().item()  
    players_above_bankroll_percentage = (players_above_bankroll / n_players) * 100
    print(f"Players with bankroll above starting bankroll: {players_above_bankroll_percentage:.2f}%")


    return history_t





def statistical_analysis(history_t, n_players, bet, p_win, check_rounds=[100, 500, 1000]):

    p_lose = 1 - p_win
    starting_bankroll = history_t[:, 0].mean().item()
    ev_theory = (p_win * bet) + (p_lose * -bet)
    active_players = history_t[:, :-1] > 0
    changes = torch.diff(history_t, dim=1)
    new_changes = changes[active_players]
    average = new_changes.mean().item()
    difference = average - ev_theory
    print(f"Average: {average:.2f}")
    print(f"Estimated Theoretical Value: {ev_theory:.2f}")
    print(f"Difference: {difference:.2f}")

    for n in (check_rounds):

        eliminated_players = (history_t[:, n] == 0).sum().item()
        eliminated_players_percentage = (eliminated_players / n_players) * 100

        print(f"Round {n}: {eliminated_players_percentage:.2f}% eliminated")

    final_bankroll = history_t[:, -1]
    players_above_bankroll = (final_bankroll > starting_bankroll).sum().item()
    players_above_bankroll_percentage = (
        players_above_bankroll / n_players) * 100
    print(
        f"Players with bankroll above starting bankroll: {players_above_bankroll_percentage:.2f}%")

    return history_t


def main():
    players = 10000
    starting_bankroll = 1000
    bet = 50
    p_win = 18 / 37
    max_rounds = 1000
    fair_p_win = 0.5

    print("Unfair Game Analysis:")
    history = simulate(players, starting_bankroll, bet, p_win, max_rounds)
    statistical_analysis(history, players, bet, p_win, check_rounds=[100, 500, 1000])
    print("\nFair Game Analysis:")
    fair_history = simulate(players, starting_bankroll, bet, fair_p_win, max_rounds)
    fair_history = statistical_analysis(fair_history, players, bet, fair_p_win, check_rounds=[100, 500, 1000])
    print("\n Unfair Game Tensors.")
    print(history)
    print("\n Fair Game Tensors.")
    print(fair_history)

    generate_visualization()
    return 0


if __name__ == "__main__":
    sys.exit(main())