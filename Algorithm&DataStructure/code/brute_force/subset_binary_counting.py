arr = [2, 3, 4, 5]
n = len(arr)

for i in range(1 << n):
    for j in range(n):
        if i & 1 << j:
            print(arr[j], end="")
    print()