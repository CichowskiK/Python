def sum_seq(sequence): 
    result =0
    for i in range(len(sequence)):
        if isinstance(sequence[i] , (list, tuple)) :
            result += sum_seq(sequence[i])
        else:
            result += sequence[i]
    return result

sekwencja= [1,2,[3,4,[5,6,[7,8]],9],10]

print(sekwencja)

print("po sumowaniu:", sum_seq(sekwencja))
