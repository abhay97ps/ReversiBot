import copy
from Model.State import State


def North(i, j, board, turn):
    if i == 0 or board[i - 1][j] == 0 or board[i - 1][j] == turn:
        return
    else:
        for k in range(i - 2, -1, -1):
            if board[k][j] == 0:
                return [k, j]
            elif board[k][j] == turn:
                return
        return


def East(i, j, board, turn):
    if j == 7 or board[i][j + 1] == 0 or board[i][j + 1] == turn:
        return
    else:
        for k in range(j + 2, 8):
            if board[i][k] == 0:
                return [i, k]
            elif board[i][k] == turn:
                return
        return


def South(i, j, board, turn):
    if i == 7 or board[i + 1][j] == 0 or board[i + 1][j] == turn:
        return
    else:
        for k in range(i + 2, 8):
            if board[k][j] == 0:
                return [k, j]
            elif board[k][j] == turn:
                return
        return


def West(i, j, board, turn):
    if j == 0 or board[i][j - 1] == 0 or board[i][j - 1] == turn:
        return
    else:
        for k in range(j - 2, -1, -1):
            if board[i][k] == 0:
                return [i, k]
            elif board[i][k] == turn:
                return
        return


def NorthEast(i, j, board, turn):
    if i == 0 or j == 7 or board[i - 1][j + 1] == 0 or board[i - 1][j + 1] == turn:
        return
    else:
        k1, k2 = i - 2, j + 2
        while k1 > -1 and k2 < 8:
            if board[k1][k2] == 0:
                return [k1, k2]
            elif board[k1][k2] == turn:
                return
            k1, k2 = k1 - 1, k2 + 1
        return


def SouthEast(i, j, board, turn):
    if i == 7 or j == 7 or board[i + 1][j + 1] == 0 or board[i + 1][j + 1] == turn:
        return
    else:
        k1, k2 = i + 2, j + 2
        while k1 < 8 and k2 < 8:
            if board[k1][k2] == 0:
                return [k1, k2]
            elif board[k1][k2] == turn:
                return
            k1, k2 = k1 + 1, k2 + 1
        return


def SouthWest(i, j, board, turn):
    if i == 7 or j == 0 or board[i + 1][j - 1] == 0 or board[i + 1][j - 1] == turn:
        return
    else:
        k1, k2 = i + 2, j - 2
        while k1 < 8 and k2 > -1:
            if board[k1][k2] == 0:
                return [k1, k2]
            elif board[k1][k2] == turn:
                return
            k1, k2 = k1 + 1, k2 - 1
        return


def NorthWest(i, j, board, turn):
    if i == 0 or j == 0 or board[i - 1][j - 1] == 0 or board[i - 1][j - 1] == turn:
        return
    else:
        k1, k2 = i - 2, j - 2
        while k1 > -1 and k2 > -1:
            if board[k1][k2] == 0:
                return [k1, k2]
            elif board[k1][k2] == turn:
                return
            k1, k2 = k1 - 1, k2 - 1
        return


def opp(x):
    if x == 1:
        return -1
    else:
        return 1


def flipNorth(pos, board, turn):
    i, j = pos
    board[i][j] = turn

    if i == 0:
        return board
    if board[i - 1][j] == 0 or board[i - 1][j] == turn:
        return board
    for k in range(i - 2, -1, -1):
        if board[k][j] == 0:
            return board
        elif board[k][j] == opp(turn) and k == 0:
            return board
        elif board[k][j] == turn:
            break

    i -= 1
    while i >= 0 and board[i][j] != turn:
        board[i][j] = turn
        i -= 1
    return board


def flipEast(pos, board, turn):
    i, j = pos
    board[i][j] = turn

    if j == 7:
        return board
    if board[i][j + 1] == 0 or board[i][j + 1] == turn:
        return board
    for k in range(j + 2, 8):
        if board[i][k] == 0:
            return board
        elif board[i][k] == opp(turn) and k == 7:
            return board
        elif board[i][k] == turn:
            break

    j += 1
    while j < 8 and board[i][j] != turn:
        board[i][j] = turn
        j += 1
    return board


def flipSouth(pos, board, turn):
    i, j = pos
    board[i][j] = turn

    if i == 7:
        return board
    if board[i + 1][j] == 0 or board[i + 1][j] == turn:
        return board
    for k in range(i + 2, 8):
        if board[k][j] == 0:
            return board
        elif board[k][j] == opp(turn) and k == 7:
            return board
        elif board[k][j] == turn:
            break

    i += 1
    while i < 8 and board[i][j] != turn:  # while i < k:
        board[i][j] = turn
        i += 1
    return board


def flipWest(pos, board, turn):
    i, j = pos
    board[i][j] = turn

    if j == 0:
        return board
    if board[i][j - 1] == 0 or board[i][j - 1] == turn:
        return board
    for k in range(j - 2, -1, -1):
        if board[i][k] == 0:
            return board
        elif board[i][k] == opp(turn) and k == 0:
            return board
        elif board[i][k] == turn:
            break

    j -= 1
    while j >= 0 and board[i][j] != turn:
        board[i][j] = turn
        j -= 1
    return board


def flipNorthEast(pos, board, turn):
    i, j = pos
    board[i][j] = turn

    if i == 0 or j == 7:
        return board
    if board[i - 1][j + 1] == 0 or board[i - 1][j + 1] == turn:
        return board
    k1, k2 = i - 2, j + 2
    while k1 > -1 and k2 < 8:
        if board[k1][k2] == 0:
            return board
        elif board[k1][k2] == opp(turn) and k1 == 0 and k2 == 7:
            return board
        elif board[k1][k2] == turn:
            break
        k1, k2 = k1 - 1, k2 + 1
    i, j = i - 1, j + 1
    while i >= 0 and j < 8 and board[i][j] != turn:
        board[i][j] = turn
        i, j = i - 1, j + 1
    return board


def flipSouthEast(pos, board, turn):
    i, j = pos
    board[i][j] = turn

    if i == 7 or j == 7:
        return board
    if board[i + 1][j + 1] == 0 or board[i + 1][j + 1] == turn:
        return board
    k1, k2 = i + 2, j + 2
    while k1 < 8 and k2 < 8:
        if board[k1][k2] == 0:
            return board
        elif board[k1][k2] == opp(turn) and k1 == 7 and k2 == 7:
            return board
        elif board[k1][k2] == turn:
            break
        k1, k2 = k1 + 1, k2 + 1
    i, j = i + 1, j + 1
    while i < 8 and j < 8 and board[i][j] != turn:
        board[i][j] = turn
        i, j = i + 1, j + 1
    return board


def flipSouthWest(pos, board, turn):
    i, j = pos
    board[i][j] = turn

    if i == 7 or j == 0:
        return board
    if board[i + 1][j - 1] == 0 or board[i + 1][j - 1] == turn:
        return board
    k1, k2 = i + 2, j - 2
    while k1 < 8 and k2 > -1:
        if board[k1][k2] == 0:
            return board
        elif board[k1][k2] == opp(turn) and k1 == 7 and k2 == 0:
            return board
        elif board[k1][k2] == turn:
            break
        k1, k2 = k1 + 1, k2 - 1
    i, j = i + 1, j - 1
    while i < 8 and j >= 0 and board[i][j] != turn:
        board[i][j] = turn
        i, j = i + 1, j - 1
    return board


def flipNorthWest(pos, board, turn):
    i, j = pos
    board[i][j] = turn

    if i == 0 or j == 0:
        return board
    if board[i - 1][j - 1] == 0 or board[i - 1][j - 1] == turn:
        return board
    k1, k2 = i - 2, j - 2
    while k1 > -1 and k2 > -1:
        if board[k1][k2] == 0:
            return board
        elif board[k1][k2] == opp(turn) and k1 == 0 and k2 == 0:
            return board
        elif board[k1][k2] == turn:
            break
        k1, k2 = k1 - 1, k2 - 1
    i, j = i - 1, j - 1
    while i >= 0 and j >= 0 and board[i][j] != turn:
        board[i][j] = turn
        i, j = i - 1, j - 1
    return board


def possible(board, i, j, turn):
    tbr = [North(i, j, board, turn), East(i, j, board, turn), South(i, j, board, turn), West(i, j, board, turn),
           NorthEast(i, j, board, turn), SouthEast(i, j, board, turn), SouthWest(i, j, board, turn),
           NorthWest(i, j, board, turn)]
    gen = [x for x in tbr if x is not None]
    return gen


def flip(brd, possible_pos, turn):
    states = []
    for pos in possible_pos:
        board = copy.deepcopy(brd)
        board = flipNorth(pos, board, turn)
        board = flipEast(pos, board, turn)
        board = flipSouth(pos, board, turn)
        board = flipWest(pos, board, turn)
        board = flipNorthEast(pos, board, turn)
        board = flipSouthEast(pos, board, turn)
        board = flipSouthWest(pos, board, turn)
        board = flipNorthWest(pos, board, turn)
        states.append(State(board))
    return states


def Next(state, turn):
    state_array = []
    board = state.Board
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == turn:
                possible_pos = possible(board, i, j, turn)
                new_states = flip(copy.deepcopy(board), possible_pos, turn)
                state_array += new_states
    return state_array


def Check(state, turn):
    board = state.Board
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == turn:
                possible_pos = possible(board, i, j, turn)
                if possible_pos:
                    return True
                else:
                    continue

    return False
