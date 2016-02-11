strings = open('input8').read().splitlines()
print(sum(map(len, strings)) - len(eval('+'.join(strings))))
