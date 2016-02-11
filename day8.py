strings = open('input8').read().splitlines()
print(len(eval('+'.join(strings))) - sum(map(len, strings)))
