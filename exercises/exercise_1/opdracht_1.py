def likes(team: list) -> str:
    if len(team) == 0:
        print("no one likes this")
    elif len(team) == 1:
        print(str(team[0]) + ' likes this')
    elif len(team) == 2:
        print(str(team[0]) + ' and '+str(team[1]) + ' like this')
    elif len(team) == 3:
        print(str(team[0]) + ', ' + str(team[1]) + ' and ' +str(team[2]) + ' like this')

