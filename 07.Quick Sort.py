## 책코드
# def change(x, i, j) :
#     x[i], x[j] = x[j], x[i]

# def Select(x, l, r) :
#     select_val = x[l]
#     select_idx = l

#     while l <= r :
#         while l<= r and x[l] <= select_val :
#             # 선택된 값이 다음(시작일 땐 현재) 값 보다 클 때, l에 그 다음 인덱스 할당  
#             l += 1 
#         while l<=r and x[r] >= select_val :
#             # 선택된 값이 끝에있는 값 보다 작을 때, r에 끝에서 한단계 작은 인덱스 할당
#             r -= 1
#         if l <= r :
#             change(x, l, r)
#             l += 1
#             r -= 1
#     change(x, select_idx, r)
#     return r

# def quickSort(x, pivotMethod = Select ) :
#     def Qsort(x, first, last) :
#         if first < last :
#             splitP = pivotMethod(x, first, last)
#             Qsort(x, first, splitP-1)
#             Qsort(x, splitP+1, last)
#     Qsort(x, 0, len(x)-1)

## 다른코드 : 리스트 추가 방식 활용(메모리 비효율적)
# def quickSort(x) :
#     if len(x) <= 1 :
#         return x
    
#     pivot = x[len(x)//2] # 중간값 할당
#     less_arr, equal_arr, greater_arr = [], [], []
#     for num in x :
#         if num < pivot :
#             # 기준 값보다 작은 값
#             less_arr.append(num)
#         elif num > pivot :
#             # 기준 값보다 큰 값
#             greater_arr.append(num)
#         else :
#             # 기준 값과 동일 한 값
#             equal_arr.append(num)
#     return quickSort(less_arr)+equal_arr+quickSort(greater_arr)

## 다른코드 : 메모리 효율적
def quickSort(x) :
    def sort(low, high) :
        if high <= low :
            return # 종료 시점
    
        mid = partition(low, high) # 여기가 메인
        # 재귀 함수 활용해  퀵 정렬 수행 
        sort(low, mid-1) 
        sort(mid, high)
    
    def partition(low, high) :
        pivot = x[(low+high)//2]
        while low <= high :
            # low와 high 값이 교차 할 때 까지 진행
            while x[low] < pivot :
                low += 1
            while x[high] > pivot :
                high -= 1
            if low <= high :
                # 교차 하지 않았을 경우 두 값의 위치를 바꿔주고 교차 할 때 까지 
                x[low], x[high] = x[high], x[low]
                low, high = low+1, high-1
        return low # 교차했을 때의 low 값
    
    return sort(0, len(x)-1)


x = [ 5, 2, 8, 6, 1, 9, 3, 7]
quickSort(x)
print(x)
