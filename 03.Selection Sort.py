def change(x, i, j) :
    x[i], x[j] = x[j], x[i]

def selectionSort(x) :
    for size in range(len(x)) :
        # x의 요소 갯수 만큼 순회
        min_i = size
        for i in range(size, len(x)) :
            if x[i] < x[min_i] :
                # 가장 작은 값의 인덱스를 min_i 에 저장
                min_i = i

        # 가장 작은 값이 리스트의 size 자리에 위치하도록
        change(x, min_i, size)


x = [ 5, 2, 8, 6, 1, 9, 3, 7]
selectionSort(x)
print(x)




# 책에 있는 코드
def selectionSort(x) :
    for size in reversed(range(len(x))) :
        # x의 요소 갯수 만큼 순회
        max_i = 0
        for i in range(1, 1+size) :
            if x[i] > x[max_i] :
                # 가장 작은 값의 인덱스를 min_i 에 저장
                max_i = i
        print(x)

        # 가장 작은 값이 리스트의 size 자리에 위치하도록
        change(x, max_i, size)
