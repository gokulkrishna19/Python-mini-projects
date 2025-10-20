# tournament_manager.py

teams = []

def add_team(name):
    teams.append(name)
    print(f"Team '{name}' added successfully!")

def show_teams():
    print("\nRegistered Teams:")
    for i, team in enumerate(teams, start=1):
        print(f"{i}. {team}")

# Example usage
add_team("Team A")
add_team("Team B")
add_team("Team C")

show_teams()
