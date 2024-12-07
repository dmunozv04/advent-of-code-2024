from itertools import cycle
def main():
    part1()
    part2()

    
    
def part1():
    VECTORS = [
        (0,-1), #up
        (1,0), #right
        (0, 1), #down
        (-1,0), #left
    ]
    vectors_cycle = cycle(VECTORS)
    with open("day06/real_input.txt", "r") as f:
        mat = [list(line.strip()) for line in f]
    loc = ()
    vec = next(vectors_cycle)
    for idy, y in enumerate(mat):
        for idx, x in enumerate(y):
            if x == "^":
                loc = (idx, idy)
    mat[loc[1]][loc[0]] = "x"
    count = 1
    keep = True
    while keep:
        try:
            if(mat[loc[1] + vec[1]][loc[0] + vec[0]]) == "#": #obstacle
                vec = next(vectors_cycle)

            loc = (loc[0] + vec[0], loc[1] + vec[1])
            if(mat[loc[1]][loc[0]]) != "x":
                count +=1
                mat[loc[1]][loc[0]] = "x"
        except IndexError: # got out of the map
            print(count)
            keep = False
            break
            
        
            
def part2():
    VECTORS = [
        (0, -1),  # up
        (1, 0),   # right
        (0, 1),   # down
        (-1, 0),  # left
    ]
    with open("day06/real_input.txt", "r") as f:
        mat_og = [list(line.strip()) for line in f]
    loc = ()
    for idy, y in enumerate(mat_og):
        for idx, x in enumerate(y):
            if x == "^":
                loc = (idx, idy)
    loc_start = loc
    count = 0
    height = len(mat_og)
    width = len(mat_og[0])

    for idy in range(height):
        for idx in range(width):
            if (idx, idy) == loc_start:
                continue  # Can't place obstruction at starting position
            if mat_og[idy][idx] == "#":
                continue  # Skip existing obstacles

            # Place the new obstacle
            mat = [row[:] for row in mat_og]  # Shallow copy is sufficient
            mat[idy][idx] = "#"

            visited_states = set()
            vectors = cycle(VECTORS)
            vec = next(vectors)
            loc = loc_start

            while True:
                state = (loc, vec)
                if state in visited_states:
                    # Loop detected
                    count += 1
                    break
                visited_states.add(state)

                next_loc = (loc[0] + vec[0], loc[1] + vec[1])

                # Check bounds
                if not (0 <= next_loc[0] < width and 0 <= next_loc[1] < height):
                    # Guard leaves the map
                    break

                if mat[next_loc[1]][next_loc[0]] == "#":
                    # Obstacle ahead, turn right
                    vec = next(vectors)
                else:
                    # Move forward
                    loc = next_loc

    print(count)


if __name__ == "__main__":
    main()