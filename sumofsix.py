def sol(lst):
    new_list=range(min(lst),max(lst)+1)
    sum_list=[]
    for i in new_list:
        if i%6 == 0:
            sum_list.append(i)
    return sum(sum_list)
