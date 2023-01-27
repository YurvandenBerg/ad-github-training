def likes(team: list) -> str:
    likes = str()
    if len(team) == 0:
        likes = "No one likes this"
    elif len(team) == 1:
        likes = str(team[0])+ " likes this"
    elif len(team) == 2:
        likes = str(team[0]) + ' en ' + str(team[1]) + ' like this'
    elif len(team) == 3:
        likes = str(team[0]) + ' en ' + str(team[1]) + ' en ' + str(team[2]) + ' like this'
    elif len(team) >= 4:
        likes = str(team[0]) + ' en ' + str(team[1]) + ' en' + str(len(team) - 2) + ' others like this'
    return likes

likes = likes(['dima', 'evelien', 'wies'])

print(likes)