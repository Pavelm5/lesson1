def get_summ(one, two, delimiter=' & '):
    one = str(one)
    two = str(two)
    result_get_summ = (one + delimiter + two).upper()  
    print(result_get_summ)

get_summ('Learn', 'python')