def main():
    part1()
    part2()
    
def part1():
    GOOD_VALUE = "XMAS"
    # vectors in format (x,y)
    VECTORS = [
        (1,0), (-1,0), #horizontal
        (0,1), (0,-1), #vertical
        (1,1), (-1,-1), (1,-1), (-1, 1)#diagonal
    ]
    with open("day04/real_input.txt", "r") as f:
        mat = [list(' ' + i.strip() + ' ') for i in f]
    mat.insert(0, [" "] * len(mat[0]))
    mat.append([" "] * len(mat[0]))
    #print(mat)
    count = 0
    for y in range(len(mat)):
        for x in range(len(mat[0])):
            if mat[y][x] != "X":
                continue
            for vector in VECTORS:
                value = ""
                for i in range(4):
                    char = mat[y+(vector[1]*i)][x+(vector[0]*i)]
                    if char == " ":
                        break
                    value += char
                if value == GOOD_VALUE:
                    count += 1
    print(count)
                
        
    

def part2():
    # vectors in format (x,y)
    with open("day04/real_input.txt", "r") as f:
        mat = [list(' ' + i.strip() + ' ') for i in f]
    mat.insert(0, [" "] * len(mat[0]))
    mat.append([" "] * len(mat[0]))
    count = 0
    for y in range(len(mat)):
        for x in range(len(mat[0])):
            if mat[y][x] != "A":
                continue
            value_1 = mat[y-1][x-1] + mat[y+1][x+1]
            value_2 =  mat[y-1][x+1] + mat[y+1][x-1]
            if ("M" in value_1 and "S" in value_1) and ("M" in value_2 and "S" in value_2):
                count += 1
    print(count)


if __name__ == "__main__":
    main()