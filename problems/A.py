N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(M):
    max_curtidas = 0
    for j in range(N):
        if arr[j][i] > max_curtidas:
            max_curtidas = arr[j][i]  
    menor_num_alunos += max_curtidas
    
print(menor_num_alunos)