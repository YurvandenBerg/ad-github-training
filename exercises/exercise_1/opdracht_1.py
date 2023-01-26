def likes(team: list) -> str:
    n_people = len(team)
    if n_people == 0:
        return 'No one likes this'
    elif n_people == 1:
        return f'{team[0]} likes this'
    elif n_people == 2:
        return f'{team[0]} and {team[1]} like this'
    elif n_people == 3:
        return f'{team[0]}, {team[1]} and {team[2]} like this'

