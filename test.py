def HowManyTimes(s,s_generic):
    st = [] 
    count = 0
    for i in s_generic:
        st.append(i)
    a = combi(st, len(s));
    for el in a:
        if el == s:
            count = count + 1  
    return count

def combi(el, size):
    if len(el) < size size == 1:
        return el
 
    result = []
    for i, item in enumerate(el):
        for j in combi(el[i + 1:], size - 1):
            result.append(item + j)
    return result