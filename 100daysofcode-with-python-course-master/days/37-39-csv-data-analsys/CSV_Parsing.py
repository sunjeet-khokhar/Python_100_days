import csv


def parse_football_data(data_file):
    with open(data_file,'r') as f:
        next(f,None)
        data = [row for row in (csv.reader(f.read().splitlines()))]
    return data

def max_wins_index(data_file):
    wins_list = []
    for row in parse_football_data(data_file):
        print(f"Team {row[0]} has {row[2]} wins")
        wins_list.append(int(row[2]))
    return(wins_list.index(max(wins_list)))


data_file = "football.csv"
parsed_data = parse_football_data(data_file)
print(f"The Team with maximum wins is {parsed_data[max_wins_index(data_file)][0]}")

