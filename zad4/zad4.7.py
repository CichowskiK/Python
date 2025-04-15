def flatten(sequence):
    result = []
    for i in range(len(sequence)):
        if isinstance(sequence[i] , (list, tuple)) :
            result.extend(flatten(sequence[i]))
        else:
            result.append(sequence[i])
    return result


seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print("orginalna sekwencja",seq)
print("splaszczona sekwencja",flatten(seq))