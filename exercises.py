from itertools import islice


def is_anagram(s1, s2):
    """
    Write an algorithm that returns whether s1 and s2 are anagrams of each other, i.e.
    if s1 and s2 contain the same letters in a possibly different order.
    E.g.: "abc" and "cab" are anagrams, "aab" and "bba" are not.
    :param s1: string
    :param s2: string
    :return: True or False
    """

    # if both strings are equal when sorted, returns true
    return sorted(s1) == sorted(s2) and len(s1) == len(s2)

    pass


def check_parenthesis_consistency(string):
    """
    Write an algorithm that determines if the parenthesis (round brackets "()") in a string are properly balanced.
    An expression is said to be properly parenthesised if it has the form "(p)" or "pq", where p and q are
    properly parenthesised expressions. Any string (including an empty string) that does not contain any parenthesis
    is properly parenthesised.
    E.g.: "()()" is properly parenthesised, "(()" is not.
    :param string: the string to analyse.
    :return: True if the parentheses are balanced, False if not.
    """

    openParenthesis = 0
    closedParenthesis = 0

    # counts the number of open and closed parenthesis
    for c in string:
        if c == '(':
            openParenthesis += 1
        elif c == ')':
            closedParenthesis += 1

    # returns true if there are as much open parenthesis as closed ones
    return openParenthesis == closedParenthesis

    pass


def is_valid(cell, maze):
    """
    Checks if a cell of the maze has valid coordinates and has a value of 1
    :param cell: tuple (x_start, y_start) - the cell to check
    :param maze: list of lists - the maze
    :return: boolean - the cell's validity
    """
    return (cell[0] >= 0) and (cell[0] < len(maze)) and (cell[1] >= 0) and (cell[1] < len(maze[0])) and (maze[cell[0]][cell[1]] == 1)


def shortest_path(start, end, maze):
    """
    Write an algorithm that finds the shortest path in a maze from start to end
    The maze is represented by a list of lists containing 0s and 1s:
    0s are walls, paths cannot go through them
    The only movements allowed are UP/DOWN/LEFT/RIGHT
    :param start: tuple (x_start, y_start) - the starting point
    :param end: tuple (x_end, y_end) - the ending point
    :param maze: list of lists - the maze
    :return: list of positions [(x1, y1), (x2, y2), ...] representing the shortest path in the maze
    """

    # we'll use a BFS algorithm to search for the shortest path in the maze
    # if the start or the end is not valid, returns an empty list
    if maze[start[0]][start[1]] == 0 or maze[end[0]][end[1]] == 0:
        return []

    # initialize a boolean array to check if every cell has been visited
    visited = [[False for i in range(len(maze[0]))]for j in range(len(maze))]
    visited[start[0]][start[1]] = True  # marks the source as visited

    # enqueue the first cell and initializes the predecessors array
    queue = [start]
    predecessors = [[(0, 0) for i in range(len(maze[0]))]for j in range(len(maze))]

    while queue:
        node = queue.pop(0)
        # print(node[0], ",", node[1])
        if node == end:
            break  # exit the loop if we reach the end

        # add the adjacent cells to the queue if they're valid
        adjacentCells = [(node[0] - 1, node[1]), (node[0] + 1, node[1]), (node[0], node[1] - 1), (node[0], node[1] + 1)]
        for cell in adjacentCells:
            if is_valid(cell, maze) and not visited[cell[0]][cell[1]]:
                # sets the cell to visited and save its predecessor
                visited[cell[0]][cell[1]] = True
                predecessors[cell[0]][cell[1]] = node
                queue.append(cell)

    # backtracks the predecessors array to get the path from start to end
    path = [end]
    backtrack = end
    while backtrack != start:
        path.insert(0, predecessors[backtrack[0]][backtrack[1]])
        backtrack = predecessors[backtrack[0]][backtrack[1]]

    return path

    pass
