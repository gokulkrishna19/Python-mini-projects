
# leaderboard.py

points = {
    "Lions": 6,
    "Tigers": 3,
    "Bulls": 4,
}

def show_leaderboard():
    print("\n🏅 Leaderboard:")
    sorted_table = sorted(points.items(), key=lambda x: x[1], reverse=True)
    for rank, (team, pts) in enumerate(sorted_table, 1):
        print(f"{rank}. {team} — {pts} pts")

show_leaderboard()
