def stringSearch(word, target) :
    word_idx = 0
    target_idx = 0

    while word_idx != len(word) and target_idx != len(target) :
        if word[word_idx] == target[target_idx] :
            word_idx += 1
            target_idx += 1
        else :
            word_idx = word_idx - target_idx + 1 
            target_idx = 0

    return word_idx - target_idx if target_idx == len(target) else -1

if __name__ == '__main__' :
    word = input()
    target = input()

    idx = stringSearch(word, target)

    if idx == -1 :
        print('존재하지 않음')  
    else :
        print('존재')