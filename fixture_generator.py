# fixture_generator.py

def generate_fixtures(teams):
    print("\nTournament Fixtures:")
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            print(f"{teams[i]} vs {teams[j]}")

# Example usage
teams = ["Team A", "Team B", "Team C"]
generate_fixtures(teams)
