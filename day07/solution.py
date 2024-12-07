from typing import NamedTuple
from itertools import product

def main():
    part1()
    part2()
class Equation(NamedTuple):
    result: int
    values: list[int]
def part1():
    OPERATORS = (True, False) # + *
    with open("day07/real_input.txt", "r") as f:
        equations: list[Equation] = [Equation(int(line.split(":")[0]), list(map(int, line.split(":")[1].split()))) for line in f]
    result = 0
    for equation in equations:
        possible_operators = product(OPERATORS, repeat=len(equation.values) -1)
        for op in possible_operators:
            eq_value = equation.values[0]
            for (x, op_now) in zip(equation.values[1:], op):
                if op_now:
                    eq_value *= x
                else:
                    eq_value += x
            if eq_value == equation.result:
                result += equation.result
                break
    print(result)

def part2():
    OPERATORS = (0, 1, 2) # + *
    with open("day07/real_input.txt", "r") as f:
        equations: list[Equation] = [Equation(int(line.split(":")[0]), list(map(int, line.split(":")[1].split()))) for line in f]
    result = 0
    for equation in equations:
        possible_operators = product(OPERATORS, repeat=len(equation.values) -1)
        for op in possible_operators:
            eq_value = equation.values[0]
            for (x, op_now) in zip(equation.values[1:], op):
                if op_now == 0:
                    eq_value *= x
                elif op_now == 1:
                    eq_value += x
                else:
                    eq_value = int(f"{eq_value}{x}")
            if eq_value == equation.result:
                result += equation.result
                break
    print(result)

if __name__ == "__main__":
    main()