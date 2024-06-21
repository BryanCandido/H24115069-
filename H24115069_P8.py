import csv

file_name = "pe8_data.csv"
with open(file_name, "r") as file:
    reader = csv.reader(file)
    next(reader)

    #1. win-loss percentage of Home lower than the win-loss percentage of Away
    east_teams = []
    print("1. Eastern Conference teams with a win-loss percentage greater than 0.5:")
    for row in reader:
        conference, team, wl, pct, gb, pf, pa, home, away = row
        if conference == "Eastern" and float(pct) > 0.5:
            east_teams.append(team)
            print(team)
    if not east_teams:
        print("1. No Eastern Conference teams had a win-loss percentage greater than 0.5.")

    file.seek(0)

    #2. Average difference between points scored (PF) and points allowed (PA) for Eastern teams with win-loss percentage 
    east_win_teams = []
    point_diff = 0
    count = 0
    for row in reader:
        conference, team, wl, pct, gb, pf, pa, home, away = row
        if conference == "Eastern" and float(pct) > 0.5:
            east_win_teams.append(team)
            point_diff += float(pf) - float(pa)
            count += 1

    if count > 0:
        avg_point_diff = point_diff / count
        print("\n3. Average difference between points scored (PF) and points allowed (PA) for Eastern teams with a win-loss percentage greater than 0.5:")
        print(avg_point_diff)
    else:
        print("\n3. No Eastern Conference teams had a win-loss percentage greater than 0.5.")

    #3. Teams with higher rank
    western_teams = []
    print("\n2. Western Conference teams with a lower win rate at home compared to away:")
    for row in reader:
        conference, team, wl, pct, gb, pf, pa, home, away = row
        if conference == "Western" and int(home) < int(away):
            western_teams.append(team)
            print(team)
    if not western_teams:
        print("\n2. No Western Conference teams had a lower win rate at home compared to away.")

    file.seek(0) 

    

file_name.close()