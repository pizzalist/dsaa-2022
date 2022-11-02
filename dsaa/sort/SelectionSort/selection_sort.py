A = [64, 25, 12, 22, 11]

for i in range(len(A)):

    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]

    print(A)


# [11, 25, 12, 22, 64]
# [11, 12, 25, 22, 64]
# [11, 12, 22, 25, 64]
# [11, 12, 22, 25, 64]
# [11, 12, 22, 25, 64]

# selection 과 insertion 의 차이점 
# selection은 무조건 비교를 다 해야 하고, insrtion은 작은 값이 나오면 비교 안해도 된다