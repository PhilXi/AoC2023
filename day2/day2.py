from time import perf_counter as pfc
def check_game(game):
    check = None
    for color in game:
        color_str = color[0].split()[-1]
        number = int(color[0][:2])
        if 'red' in color_str:
            check = int(number) <= 12
        if 'green' in color_str:
            check = int(number) <= 13
        if 'blue' in color_str:
            check = int(number) <= 14
        if check == False:
            break
    return check
def main():
    start1 = pfc()
    with open("2023/input/day2.txt", 'r') as f:
        day2 = f.read().split('\n')
        day2 = [game[8:] for game in day2]
        day2 = [game.split('; ') for game in day2]
    count = 1
    total_sum = 0
    for game in day2:
        game = [[item] for element in game for item in element.split(', ')] 
        if count == 100:game[0][0] = game[0][0].strip(': ')
        if check_game(game) == True:
            total_sum+=count
        count+=1
    stop = pfc()
    print('total_sum: ',total_sum,'time: ',stop-start1,'s')
if __name__ == "__main__":
    main()