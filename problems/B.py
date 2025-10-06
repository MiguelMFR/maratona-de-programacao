N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

k = 0
vistos = set()

while True:

    if A == B:
        print(k)
        break
    elif tuple(A) in vistos:
        print("IMPOSSIVEL")
        break
    elif k > 10**9:
        print("DEMAIS")
        break

    vistos.add(tuple(A))
    A = [A[C[i]-1] for i in range(N)]
    k += 1