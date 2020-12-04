game_board = list(range(1, 10))

win_comb = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def show_board():
    print('---------')
    for i in range(3):
        print('|', game_board[0 + i * 3], game_board[1 + i * 3], game_board[2 + i * 3], '|')
    print('---------')

def ask_gamer(player_step):
    while True:
        value = input("Куда ходить: "+ player_step + "?")
        if not (value in '123456789'):
            print("Неправильный символ. Повторите.")
            continue
        value = int(value)
        if str(game_board[value - 1]) in 'XO':
            print("Клетка уже занята")
            continue
        game_board[value - 1] = player_step
        break

def check_win():
    for each in win_comb:
        if (game_board[each[0]-1]) == (game_board[each[1]-1]) == (game_board[each[2]-1]):
            return game_board[each[1]-1]
    else:
        return False

def main():
    step = 0
    while True:
        show_board()
        if step % 2 == 0:
            ask_gamer('X')
        else:
            ask_gamer('O')
        if step > 3:
            winner = check_win()
            if winner:
                show_board()
                print(winner, "Выиграл!")
                break
        step += 1
        if step > 8:
            show_board()
            print("Ничья")
            break

main()


