def main():
    part1()
    part2()
        

def part1():
    with open("day05/real_input.txt", "r") as f:
        lines = [l.strip() for l in f]
    cut_idx = lines.index("")
    rules = [list(map(int, l.split("|"))) for l in lines[:cut_idx]]
    updates = [list(map(int, l.split(","))) for l in lines[cut_idx+1:]]
    sums = 0
    for pages in updates:
        good = True
        for page in pages:
            for rule in filter(lambda rule: rule[0] == page, rules):
                if rule[1] in pages:
                    if pages.index(page) > pages.index(rule[1]):
                        good = False
                        break
            if not good: break
        if good:
            sums += pages[int(len(pages)/2):int(len(pages)//2)+1][0]
    print(sums)

                

def part2():
    with open("day05/real_input.txt", "r") as f:
        lines = [l.strip() for l in f]
    cut_idx = lines.index("")
    rules = [list(map(int, l.split("|"))) for l in lines[:cut_idx]]
    updates = [list(map(int, l.split(","))) for l in lines[cut_idx+1:]]
    bad_updates = []
    sums = 0
    for pages in updates:
        good = True
        for page in pages:
            for rule in filter(lambda rule: rule[0] == page, rules):
                if rule[1] in pages:
                    if pages.index(page) > pages.index(rule[1]):
                        good = False
                        break
            if not good: break
        if not good:
            bad_updates.append(pages)
    for pages in bad_updates:
        new_list = []
        for _ in range(len(pages) -1):
            rules_in_effect = list(filter(lambda x: x[0] in pages and x[1] in pages,rules))
            numbers_left = set([rule[0] for rule in rules_in_effect])
            numbers_right = set([rule[1] for rule in rules_in_effect])
            numbers_only_right = list(numbers_right.difference(numbers_left))
            last = numbers_only_right[0]
            new_list.insert(0, last)
            pages.remove(last)
        new_list.insert(0, pages[0])
        sums += new_list[int(len(new_list)/2):int(len(new_list)//2)+1][0]
    print(sums)


if __name__ == "__main__":
    main()