def margeSort(x) :
    if len(x) > 1 :
        mid = len(x)//2
        colx, rowx = x[:mid], x[mid:]
        # 재귀함수를 사용해 colx와 rowx에 각각 요소가 1개만 남도록
        margeSort(colx)
        margeSort(rowx)

        # 초기 인덱스 설정
        coli, rowi, i = 0, 0, 0
        while coli < len(colx) and rowi < len(rowx) :
            # 인덱스 값이 요소 갯수 보다 크면 스탑
            if colx[coli] < rowx[rowi] :
                # 만약 뒤에 있는 값이 더 크면, 앞의 값을 i번째로 할당
                x[i] = colx[coli]
                coli += 1
            else :
                # 만약 앞에 있는 값이 더 크면, 뒤의 값을 i번째로 할당
                x[i] = rowx[rowi]
                rowi += 1
            i += 1
        # x 에 들어가지 못한 가장 큰 값 삽입
        x[i:] = colx[coli:] if coli != len(colx) else rowx[rowi :]


x = [5, 2, 8, 6, 1, 9, 3, 7]
margeSort(x)
print(x)
