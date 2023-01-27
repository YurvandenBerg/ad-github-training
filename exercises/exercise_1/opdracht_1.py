def likes(team: list) -> str:
    if len(team) == 0:
        return "no one likes this"
    elif len(team) == 1:
        return str(team[0]) + ' likes this'
    elif len(team) == 2:
        return str(team[0]) + ' and '+str(team[1]) + ' like this'
