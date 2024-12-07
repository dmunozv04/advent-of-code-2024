from itertools import pairwise
def main():
    part1()
    part2()

def part1():
    with open("day02/real_input.txt") as f:
        reports = [list(map(int, line.split())) for line in f]
    diffs = [[(x-y) for x,y in pairwise(report)] for report in reports]
    valid_diffs = list(filter(lambda x: (all([i>=-3 and i<= -1 for i in x]) or all([i >= 1 and i <=3 for i in x])), diffs))
    print(len(valid_diffs))
    


def part2():
    with open("day02/real_input.txt") as f:
        reports = [list(map(int, line.split())) for line in f]
    count = 0
    for report in reports: # Check if the diff is valid without removing any element
        diff = [(x-y) for x,y in pairwise(report)]
        if all([i>=-3 and i<= -1 for i in diff]) or all([i >= 1 and i <=3 for i in diff]):
            count += 1
            continue
        for i in range(len(report)): # Try removing 1 element and check if the diff is valid
            new_report = report.copy()
            new_report.pop(i)
            diff = [(x-y) for x,y in pairwise(new_report)]
            if all([i>=-3 and i<= -1 for i in diff]) or all([i >= 1 and i <=3 for i in diff]):
                count += 1
                break
    print(count)
    

if __name__ == "__main__":
    main()