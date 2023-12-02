# imports
from time import perf_counter as pfc
def check_game(game):
    min_red,min_green,min_blue = 1,1,1
    for color in game:
        color_str = color[0].split()[-1]
        number = int(''.join(filter(str.isdigit, color[0])))
        if 'red' in color_str:
            if number >= min_red: min_red=number
        elif 'green' in color_str:
            if number >= min_green: min_green=number
        elif 'blue' in color_str:
            if number >= min_blue: min_blue=number
    return min_red*min_green*min_blue
def main():
    start1 = pfc()
    with open("2023/input/day2.txt", 'r') as f:
        day2 = f.read().split('\n')
        day2 = [game[8:] for game in day2]
        day2 = [game.split('; ') for game in day2]
    total_sum,count = 0,1
    for game in day2:
        game = [[item] for element in game for item in element.split(', ')] 
        if count == 100:game[0][0] = game[0][0].strip(': ')
        total_sum += check_game(game)
        count+=1
    stop = pfc()
    print('total_sum: ',total_sum,'time: ',stop-start1,'s')
if __name__ == "__main__":
    main()