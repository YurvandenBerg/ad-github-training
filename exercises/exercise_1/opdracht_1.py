def likes(team: list) -> str:
    if len(team) == 0:
        print("No one likes this")
    elif len(team) == 1:
        print(str(team[0])+ " likes this")
    elif len(team) == 2:
        print(str(team[0]) + ' en ' + str(team[1]) + ' like this')
    return True

likes(['dima', 'evelien'])