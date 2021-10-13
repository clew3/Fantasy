'''
Prints the teams that play the most in the span of that week
weeklyteams: None -> None
'''


import sys
import datetime

## Constants:
startday = datetime.date(2021, 10, 11).timetuple().tm_yday
currentday = datetime.date(2021, 10, 18).timetuple().tm_yday

## START
teams = {}

with open('games.txt', 'r') as infile:
    for line in infile:

        # get the date and find how many days away it is from startday
        lst = line.split(',')
        x_date = lst[0].split('-')
        gamedate = datetime.date(int(x_date[0]), int(x_date[1]), int(x_date[2]))
        day_of_year = gamedate.timetuple().tm_yday+1

        # if new year, add 365
        if day_of_year < 200:
            day_of_year += 365
        
        # isolate stretch of applicable dates
        week_number = (currentday-startday)//7
        if (day_of_year-startday)//7 == week_number:

            # find teams, add to team_dictionary
            team_1, team_2 = lst[1], lst[3]

            if team_1 in teams.keys():
                teams[team_1] += 1
            else: teams[team_1] = 1

            if team_2 in teams.keys():
                teams[team_2] += 1
            else: teams[team_2] = 1    

        
# find all teams with max games for the week
max_games = max(teams.values())
for team in teams:
    if teams[team] == max_games:
        print(team)
print(max_games)