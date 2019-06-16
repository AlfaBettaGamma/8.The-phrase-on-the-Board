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

def combi(element, size):
    if len(element) < size size == 1:
        return element
        
    result = []
    for i, item in enumerate(element):
        for j in combi(element[i + 1:], size - 1):
            result.append(item + j)
    return result