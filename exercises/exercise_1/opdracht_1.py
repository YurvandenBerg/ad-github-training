def likes(team: list) -> str:
    if len(team) ==0:
        return "No one likes this"
    elif len(team) ==1:
        return f"{team[0]} likes this"
    elif len(team) ==2:
        return f"{team[0]} en {team[1]} like this"
    elif len(team) == 3:
        return f"{team[0]}, {team[1]} en {team[2]} like this"
