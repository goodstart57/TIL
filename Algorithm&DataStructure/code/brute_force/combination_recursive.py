li = [2, 3, 4, 5]

def combination(n, r):
    if r == 0:
        print(memory)
    elif n < r:
        return
    else:
        memory[r - 1] = li[n - 1]
        combination(n - 1, r - 1)
        combination(n - 1, r)


r = 2
memory = [None for _ in range(r)]
combination(len(li), r)