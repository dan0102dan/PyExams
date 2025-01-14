# Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может увеличить количество камней в куче в два раза или добавить в кучу два камня. Так же за всю игру можно только один раз сделать суперход – ход, после которого количество камней в куче не изменится, а очередь хода перейдёт к сопернику. То есть суперход может сделать один раз либо Ваня, либо Петя. Для того чтобы делать ходы, у каждого игрока есть неограниченное количество камней. Выигрывает тот игрок, после хода которого количество камней в куче становится не менее 20. 
# В начальный момент в куче было S камней; 1 ≤ S ≤ 19. Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
# Найдите наибольшее и наименьшее значения S, при которых у Вани есть выигрышная стратегия.


TARGET = 20

def game(S, superMove = False):
    if S >= TARGET:
        return 0
    
    moves = [game(S * 2, superMove), game(S + 2, superMove)]
    if not(superMove):
        moves.append(game(S, True))

    winMoves = [x for x in moves if x <= 0]

    if winMoves:
        step = -max(winMoves) + 1
    else:
        step = -max(moves)
    
    return step

res = [S for S in range(1, TARGET) if game(S) < 0]
print(min(res), max(res))