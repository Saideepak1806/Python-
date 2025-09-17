import itertools
digits=[1,2,3]
combinations=list(itertools.permutations(digits))
for combo in combinations:
    print(*combo)