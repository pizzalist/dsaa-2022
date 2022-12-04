
def get_maze_answer(maze : dict) -> list:
    """ 미로에 대한 정보를 dict 타입으로 입력 받아서 해당 미로의 답을 반환한다.
    Args:
        maze (dict) : 미로에 대한 정보를 포함하고 있으며, 해당 정보는 위치 정보와 이동 가능한 방향에 대한 정보를 포함한다.
    Example:
        maze = {(1, 1): {'E': 0, 'W': 0, 'N': 0, 'S': 1},
                (2, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 0},
                (3, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 0},
                (1, 2): {'E': 1, 'W': 0, 'N': 0, 'S': 0},
                (2, 2): {'E': 0, 'W': 1, 'N': 0, 'S': 1},
                (3, 2): {'E': 1, 'W': 1, 'N': 1, 'S': 0},
                (1, 3): {'E': 0, 'W': 1, 'N': 0, 'S': 1},
                (2, 3): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (3, 3): {'E': 0, 'W': 1, 'N': 1, 'S': 0}}
    Returns:
        maze_solution (list) : `maze` 데이터를 바탕으로 최적의 이동 솔루션을 list 타입으로 출력한다.
                                list의 값은 공간 위치에 대한 정보를 포함한다.
    Example:
        >>> solution = get_maze_answer(maze)
        >>> solution
            [(3, 3), (3, 2), (2, 2), (2, 1), (1, 1)]
    """
    #stack에 푸시 스타트 
    stack = []
    stack.append(list(maze.keys())[-1])
    #while문으로 위치에 오면 팝
    while len(stack)>0:
        X, Y = stack[-1]
        if (X,Y) == (1,1):
            maze[(X,Y)] = 'X'
            break
        if maze[(X,Y)] != 'X':
            bool = False
            if  maze.get((X,Y))['E'] == 1 and maze.get((X,Y+1)) != 'X':
                stack.append((X,Y+1))
                bool = True
            if  maze.get((X,Y))['W'] == 1 and maze.get((X,Y-1)) != 'X':
                stack.append((X,Y-1))
                bool = True
            if  maze.get((X,Y))['N'] == 1 and maze.get((X-1,Y)) != 'X':
                stack.append((X-1,Y))
                bool = True
            if  maze.get((X,Y))['S'] == 1 and maze.get((X+1,Y)) != 'X':
                stack.append((X+1,Y))
                bool = True
            if  bool == False : 
                stack.pop()
            maze[(X,Y)] = 'X'
        else:
            stack.pop()
    for key in maze:
        value = maze.get(key)
        if value != 'X' and (key in stack):
            stack.remove(key)

    return stack

maze = {(1, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 1},
                (2, 1): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (3, 1): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (4, 1): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (5, 1): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (6, 1): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (7, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 0},
                (1, 2): {'E': 1, 'W': 1, 'N': 0, 'S': 0},
                (2, 2): {'E': 0, 'W': 0, 'N': 0, 'S': 1},
                (3, 2): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (4, 2): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (5, 2): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (6, 2): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (7, 2): {'E': 0, 'W': 1, 'N': 1, 'S': 0},
                (1, 3): {'E': 0, 'W': 1, 'N': 0, 'S': 1},
                (2, 3): {'E': 1, 'W': 0, 'N': 1, 'S': 0},
                (3, 3): {'E': 1, 'W': 0, 'N': 0, 'S': 1},
                (4, 3): {'E': 1, 'W': 0, 'N': 1, 'S': 0},
                (5, 3): {'E': 0, 'W': 0, 'N': 0, 'S': 1},
                (6, 3): {'E': 1, 'W': 0, 'N': 1, 'S': 1},
                (7, 3): {'E': 1, 'W': 0, 'N': 1, 'S': 0},
                (1, 4): {'E': 1, 'W': 0, 'N': 0, 'S': 0},
                (2, 4): {'E': 1, 'W': 1, 'N': 0, 'S': 0},
                (3, 4): {'E': 1, 'W': 1, 'N': 0, 'S': 0},
                (4, 4): {'E': 0, 'W': 1, 'N': 0, 'S': 1},
                (5, 4): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (6, 4): {'E': 0, 'W': 1, 'N': 1, 'S': 0},
                (7, 4): {'E': 1, 'W': 1, 'N': 0, 'S': 0},
                (1, 5): {'E': 0, 'W': 1, 'N': 0, 'S': 1},
                (2, 5): {'E': 0, 'W': 1, 'N': 1, 'S': 1},
                (3, 5): {'E': 0, 'W': 1, 'N': 1, 'S': 0},
                (4, 5): {'E': 0, 'W': 0, 'N': 0, 'S': 1},
                (5, 5): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (6, 5): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (7, 5): {'E': 0, 'W': 1, 'N': 1, 'S': 0}}
print(get_maze_answer(maze))