import matplotlib.pyplot as plt
import torch
from main import simulate


def generate_visualization():
    n_players = 10000
    start_bankroll = 1000
    bet = 50
    p_roulette = 18 / 37
    p_fair = 0.5
    max_rounds = 1000

    print("Running simulations...")
    history_roulette = simulate(
        n_players, start_bankroll, bet, p_roulette, max_rounds
    )
    history_fair = simulate(n_players, start_bankroll, bet, p_fair, max_rounds)

    h_roulette = history_roulette.numpy()
    h_fair = history_fair.numpy()

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Monte Carlo Roulette Simulator Results", fontsize=16)

    
    axes[0, 0].plot(h_roulette[:50, :].T, alpha=0.4, linewidth=1)
    axes[0, 0].axhline(0, color="red", linestyle="--", label="Ruin Limit (₱0)")
    axes[0, 0].set_title("C-1: 50 Sample Players' Bankrolls Over Time")
    axes[0, 0].set_xlabel("Round")
    axes[0, 0].set_ylabel("Bankroll (₱)")
    axes[0, 0].legend(loc="upper right")


    ruin_percentage = (history_roulette <= 0).float().mean(dim=0).numpy() * 100

    axes[0, 1].plot(
        ruin_percentage, color="darkred", linewidth=2, label="Ruin Rate (%)"
    )
    axes[0, 1].set_title("C-2: Ruin Rate Over Time (% Players at ₱0)")
    axes[0, 1].set_xlabel("Round")
    axes[0, 1].set_ylabel("Percentage Ruined (%)")
    axes[0, 1].set_ylim(-2, 102)
    axes[0, 1].grid(True, linestyle=":", alpha=0.6)

    
    final_bankrolls = h_roulette[:, -1]
    player_indices = range(n_players)

    
    axes[1, 0].scatter(
        player_indices, final_bankrolls, alpha=0.3, s=5, color="purple"
    )
    axes[1, 0].axhline(0, color="red", linestyle="--", label="Ruin (₱0)")
    axes[1, 0].set_title("C-3: Scatter Plot of Final Player Bankrolls (Round 1000)")
    axes[1, 0].set_xlabel("Player ID")
    axes[1, 0].set_ylabel("Final Bankroll (₱)")
    axes[1, 0].legend()

    
    mean_roulette = h_roulette.mean(axis=0)
    mean_fair = h_fair.mean(axis=0)
    axes[1, 1].plot(
        mean_roulette, label="Roulette (p = 18/37)", color="red"
    )
    axes[1, 1].plot(
        mean_fair, label="Fair Game (p = 0.5)", color="blue", linestyle="--"
    )
    axes[1, 1].set_title("C-4: Mean Bankroll Trajectory: Roulette vs Fair Game")
    axes[1, 1].set_xlabel("Round")
    axes[1, 1].set_ylabel("Mean Bankroll (₱)")
    axes[1, 1].legend()

    plt.tight_layout()
    plt.savefig("part_c_results.png", dpi=300)
    print("Success! Plot saved as 'part_c_results.png'")
    plt.show()


if __name__ == "__main__":
    generate_visualization()