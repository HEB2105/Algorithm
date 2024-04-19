def insertionSort(bucket) :
    # bucket(list) 정렬함수 
    for i in range(1, len(bucket)) :
        data = bucket[i]
        j = i-1
        while j >=0 and bucket[j] > min :
            # j 값이 양수(즉 첫번째 요소가 아님) 이며, 앞에 있는 값이 현재갑 보다 크면
            bucket[j+1] = bucket[j]
            j -= 1
        bucket[j+1] = min
    return bucket

def BucketSort(input) :
    '''
    소숫점 첫째자리를 기준으로 한 버킷정렬 함수
    :param input: data
    :return: sort data
    '''
    bucket_size = 10
    bucket_list = [ [] for _ in range(bucket_size) ]

    for data in input :
        # input의 각 값을 버킷에 할당
        index = int(bucket_size*data)
        bucket_list[index].append(data)

    for bucket in range(bucket_size) :
        # 각 버킷을 순서대로 정렬
        bucket_list[bucket] = insertionSort(bucket_list[bucket])

    out_index = 0
    for bucket in range(bucket_size) :
        # 각 버킷을 input에 순서 대로 저장
        for element in bucket_list[bucket] :
            input[out_index] = element
            out_index += 1

    return input
