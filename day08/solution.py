import math
from typing import DefaultDict, NamedTuple, Dict, Set
from itertools import combinations

def main():
    part1()
    part2()

class Node(NamedTuple):
    x: int
    y: int

def part1():
    with open("day08/real_input.txt", "r") as f:
        mat = [list(x.strip()) for x in f]
    nodes: Dict[str, list[Node]] = DefaultDict(list)
    height = len(mat)
    width = len(mat[0])
    
    for idy, row in enumerate(mat):
        for idx, char in enumerate(row):
            if char != ".":
                nodes[char].append(Node(idx, idy))
    antinodes: Set[Node] = set()
    #print(nodes)
    for n in nodes.values():
        for n1, n2 in combinations(n, 2):
            #first always smaller than second
            distx = n2.x - n1.x
            disty = n2.y - n1.y
            assert(disty >0)
            assert(distx !=0)

            antinodes.add(Node(n1.x - distx, n1.y - disty))
            antinodes.add(Node(n2.x + distx, n2.y + disty))
    antinodes = set(filter(lambda node: 0 <= node.x and node.x < width and 0<= node.y and node.y < height, antinodes))
    #print(sorted(antinodes))
    nodes_not_shown = []
    for node in antinodes:
        if(mat[node.y][node.x] == "."):
            mat[node.y][node.x] = "#"
        else:
            nodes_not_shown.append(node)
    for line in mat:
        print("".join(line))
    print(nodes_not_shown)
    print(len(antinodes))

def part2():
    with open("day08/real_input.txt", "r") as f:
        mat = [list(x.strip()) for x in f]
    nodes: Dict[str, list[Node]] = DefaultDict(list)
    height = len(mat)
    width = len(mat[0])
    
    for idy, row in enumerate(mat):
        for idx, char in enumerate(row):
            if char != ".":
                nodes[char].append(Node(idx, idy))
    antinodes: Set[Node] = set()
    #print(nodes)
    for n in nodes.values():
        for n1, n2 in combinations(n, 2):
            #first always smaller than second
            distx = n2.x - n1.x
            disty = n2.y - n1.y
            assert(disty >0)
            assert(distx !=0)
            #Antennas themselves are antinodes
            antinodes.add(n1)
            antinodes.add(n2)
            
            newx = n1.x - distx
            newy = n1.y - disty
            
            while(0 <= newx and newx < width and 0<= newy and newy < height):
                antinodes.add(Node(newx, newy))
                newx -= distx
                newy -= disty
            
            newx = n2.x + distx
            newy = n2.y + disty
            while(0 <= newx and newx < width and 0<= newy and newy < height):
                antinodes.add(Node(newx, newy))
                newx += distx
                newy += disty
    # not needed anymore, bounds check done before
    #antinodes = set(filter(lambda node: 0 <= node.x and node.x < width and 0<= node.y and node.y < height, antinodes))
    #print(sorted(antinodes))
    nodes_not_shown = []
    for node in antinodes:
        if(mat[node.y][node.x] == "."):
            mat[node.y][node.x] = "#"
        else:
            nodes_not_shown.append(node)
    for line in mat:
        print("".join(line))
    print(nodes_not_shown)
    print(len(antinodes))


if __name__ == "__main__":
    main()