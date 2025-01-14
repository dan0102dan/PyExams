# Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в кучу один камень, добавить два камня или увеличить количество камней в куче в три раза. 
# При этом нельзя повторять ход, который только что сделал второй игрок. Например, если в начале игры в куче 4 камня, Петя может первым ходом получить кучу из 5, 6 или 12 камней. Если Петя добавил 1 камень и получил кучу из 5 камней, то следующим ходом Ваня может либо добавить 2 камня (и получить 7 камней), либо утроить количество камней в куче (их станет 15). Получить 6 камней Ваня не может, так как для этого нужно добавить 1 камень, а такой ход только что сделал Петя.
# Чтобы делать ходы, у каждого игрока есть неограниченное количество камней.
# Игра завершается, когда количество камней в куче становится не менее 140. Победителем считается игрок, сделавший последний ход, то есть первым получивший кучу, в которой будет 140 или больше камней. В начальный момент в куче было S камней, 1 ≤ S ≤ 139.

# Определите, наименьшее и наибольшее значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
# − Петя не может выиграть за один ход;
# − Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.

TARGET = 140
res = {}

def game(S, prev = 0):
    if S >= TARGET:
        return 0
    if (S, prev) in res:
        return res[(S, prev)]
    
    if prev == 1:
        moves = [game(S + 2, 2), game(S * 3, 3)]
    elif prev == 2:
        moves = [game(S + 1, 1), game(S * 3, 3)]
    elif prev == 3:
        moves = [game(S + 1, 1), game(S + 2, 2)]
    else:
        moves = [game(S + 1, 1), game(S + 2, 2), game(S * 3, 3)]
    winMoves = [x for x in moves if x <= 0]
    
    if winMoves:
        step = -max(winMoves) + 1
    else:
        step = -max(moves)
    
    res[(S, prev)] = step
    return step

result = [S for S in range(139, 0, -1) if game(S) == 2]
print(min(result), max(result))