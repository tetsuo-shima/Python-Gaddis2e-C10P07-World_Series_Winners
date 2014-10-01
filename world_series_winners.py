__author__ = 'dwight'

# Write a program that reads this file and creates a dictionary in which the keys are the names of the teams and each
# key’s associated value is the number of times the team has won the World Series. The program should also create a
# dictionary in which the keys are the years and each key’s associated value is the name of the team that won that year.
# The program should prompt the user for a year in the range of 1903 through 2009. It should then display the name of
# the team that won the World Series that year and the number of times that team has won the World Series.


def main():
    ws_winners = build_world_series_dictionary('world_series.txt')
    user_year = int(input('Enter year of World Series to see winner (1903-2013): '))
    user_year = verify_ws_year(user_year)

    team = ws_winners[user_year]
    print('Winner in ' + str(user_year) + ': ' + team)

    num_wins = count_wins(team, ws_winners)
    print('The ' + team + ' have won ' + str(num_wins), end='')

    if num_wins == 1:
        print(' time.')
    else:
        print(' times.')


def build_world_series_dictionary(filename):
    file = open(filename, 'r')
    world_series_winners = {}
    line = file.readline().rstrip('\n')

    while line != '':
        line_list = line.split(',')
        team = line_list.pop()
        year = int(line_list.pop())
        world_series_winners[year] = team
        line = file.readline().rstrip('\n')

    return world_series_winners


def verify_ws_year(year):
    first_year = 1903
    latest_year = 2013
    while year < first_year or year > latest_year:
        year = int(input('Invalid year.\nEnter year of World Series to see winner: '))

    return year


def count_wins(team, ws_dict):
    count = 0

    for year in ws_dict:
        if ws_dict[year] == team:
            count += 1

    return count


main()