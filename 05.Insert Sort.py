def insertSort(x) :
    for size in range(1, len(x)) :
        # x의 길이 만큼 순환
        val = x[size]  # 여기가 포인트 현재 인덱스에 해당하는 값을 저장 하는 용도
        i = size      

        while i > 0 and x[i-1] > val :
            # 인덱스 값이  0 보다 크고, 이전 값이 더 큰 경우 값 교체
            x[i] = x[i-1]
            i -= 1
        
        # 알맞은 위치에 현재 값 저장
        x[i] = val

x = [ 5, 2, 8, 6, 1, 9, 3, 7]
insertSort(x)
print(x)
