def radix(order) :
    is_sorted = False
    position = 1  # 일의 자리부터 정렬 시작
    
    while not is_sorted :
        # is_sorted 가  일때 까지
        is_sorted = True
        # 버킷 생성
        queue_list = [ [] for _ in range(10) ]
        
        for num in order :
            digit_number = (int) (num/position) % 10  # 10으로 나눈 나머지 
            queue_list[digit_number].append(num)
            if is_sorted and digit_number > 10 :
                # 버킷이 10개 이상이면
                is_sorted = False
                
        index = 0
        
        # 정리된 버킷을 차례대로 꺼냄
        for numbers in queue_list :
            for num in numbers :
                order[index] = num
                index += 1 
        
        # 다음 자릿수로
        position *= 10 # 자릿수 이동 
        
x = [ 5, 2, 8, 6, 1, 9, 3, 7 ]
radix(x)  # x 자체를 변경, 할당 할 필요 없음    
print(x)
