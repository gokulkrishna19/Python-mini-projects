# match_result.py

points = {}

def record_result(team1, team2, winner):
    if team1 not in points:
        points[team1] = 0
    if team2 not in points:
        points[team2] = 0

    if winner == team1:
        points[team1] += 3
    elif winner == team2:
        points[team2] += 3
    else:
        points[team1] += 1
        points[team2] += 1

def show_points():
    print("\n📊 Points Table:")
    for team, pts in points.items():
        print(f"{team}: {pts} pts")

# Example usage
record_result("Lions", "Tigers", "Lions")
record_result("Bulls", "Tigers", "Draw")
show_points()
