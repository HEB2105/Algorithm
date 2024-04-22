# 추가 공부 필요
def Between(x, start, ranges) :
    for target in range(start + ranges, len(x), ranges) :
        # target 에 2분할 한 뒤에 그룻의 값이 할당 
        val = x[target]
        i = target

        while i > start :
            print(x)
            if x[i-ranges] > val :
                x[i] = x[i - ranges]
            else :
                break
            i -= ranges
        x[i] = val

def shellSort(x) :
    ranges = len(x)//2
    while ranges > 0 :
        # 자료를 2분할 하여 반복 
        for start in range(ranges) :
            Between(x, start, ranges)
            print('----', x)
        ranges = ranges//2

x = [ 5, 2, 8, 6, 1, 9, 3, 7]
shellSort(x)
print(x)
