def KMP_table(pattern) :
    # 최장 겹치는 길이를 저장하는 테이블 
    lp = len(pattern) 
    tb = [ 0 for _ in range(lp)]  # 테이블 인덱스

    pidx = 0
    for idx in range(1, lp) : # 패턴의 인덱스 접근
        while pidx > 0 and pattern[pidx] != pattern[idx] :
            pidx = tb[pidx-1]

        if pattern[idx] == pattern[pidx] :
            pidx += 1
            tb[idx] = pidx # 해당위치에 얼마나 일치 했는지 저장 
    
    return tb

def KPM(wrd, pattern) :
    table = KMP_table(pattern)

    result = []
    pidx = 0

    for idx in range(len(word)) :
        while pidx > 0 and word[idx] != pattern[pidx] :
            # 만약 값이 다른경우 달랐던 만큼 돌아 갈 수 있게 만들어 줌 
            pidx = table[pidx-1]

        if word[idx] == pattern[pidx] :
            if pidx == len(pattern)-1 :
                result.append(idx - len(pattern)+1)
                pidx = table[pidx]
            else :
                pidx += 1
    return result


