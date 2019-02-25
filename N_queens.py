def num_of_Nqueens_solutions(n):
    # queens_placement - x positions of queens
    def helper_DFS(queens_placement, xy_dif, xy_sum):
        nonlocal placements
        y = len(queens_placement)
        if  y == n:
            placements += 1
            return
        for x in range(n):
            if not(x in queens_placement 
                        or x-y in xy_dif 
                        or x+y in xy_sum):
                helper_DFS(queens_placement + [x], [x-y] + xy_dif, [x+y] + xy_sum)

    
    placements = 0
    helper_DFS([], [], [])
    return placements

for n in range(1, 10):
    print(n, num_of_Nqueens_solutions(n))