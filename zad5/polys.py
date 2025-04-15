def remove_trailing_zeros(lst):
    while lst and lst[-1] == 0:
        lst.pop()
    return lst

def add_poly(poly1, poly2):
    if len(poly1) < len(poly2):
        poly1.extend([0] * (len(poly2) - len(poly1)))
    elif len(poly1) > len(poly2):
        poly2.extend([0] * (len(poly1) - len(poly2)))
    
    result = [poly1[i] + poly2[i] for i in range(len(poly1))]
    
    return remove_trailing_zeros(result)


def sub_poly(poly1, poly2):
    if len(poly1) < len(poly2):
        poly1.extend([0] * (len(poly2) - len(poly1)))
    elif len(poly1) > len(poly2):
        poly2.extend([0] * (len(poly1) - len(poly2)))
    
    result = [poly1[i] - poly2[i] for i in range(len(poly1))]
    
    return remove_trailing_zeros(result)

def mul_poly(poly1, poly2):
    result=[0]*(len(poly1)+len(poly2))
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i+j] += poly2[j]*poly1[i]
    return remove_trailing_zeros(result)

def is_zero(poly):
    for i in range(len(poly)):
        if poly[i] !=0:
            return False
    return True

def eq_poly(poly1,poly2):
    poly1=remove_trailing_zeros(poly1)
    poly2=remove_trailing_zeros(poly2)
    for i in range(len(poly1)):
        if poly1[i]!=poly2[i]:
            return False
    return True

def eval_poly(poly, x0):
    result = 0
    for iteam in reversed(poly):
        result = result * x0 + iteam
    return result

def pow_poly(poly, n):
    result = poly
    if(n==0):
        return [1]
    for i in range(n-1):
        result = mul_poly(result, poly)
    return remove_trailing_zeros(result)

def combine_poly(poly1, poly2):
    result= [0]*(len(poly1)*len(poly2)-1)
    for i in range(len(poly1)):
        pow_poly2 = pow_poly(poly2,i)
        for j in range(len(pow_poly2)):
            result[j] += poly1[i] * pow_poly2[j]
    return remove_trailing_zeros(result)

def diff_poly(poly):
    result=[0]*(len(poly)-1)
    for i in range(len(poly)-1):
        result[i] = poly[i+1]*(i+1)
    return remove_trailing_zeros(result)
    