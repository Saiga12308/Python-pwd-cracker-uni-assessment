import itertools

munging_combos = [
    ["a", "@"],
    ["a", "4"],

    ["b", "8"],

    ["e", "3"],
    ["e", "4"],
    ["e", "£"],
    ["e", "€"],

    ["g", "9"],

    ["i", "!"],
    ["i", "1"],

    ["l", "1"],

    ["o", "0"],

    ["p", "9"],

    ["q", "9"],

    ["r", "2"],
    ["r", "7"],

    ["s", "$"],
    ["s", "5"],

    ["t", "7"],

    ["z", "2"]
    ]

for i in range(0, len(munging_combos)+1):
    for subset in itertools.combinations(munging_combos, i):
        print(subset)