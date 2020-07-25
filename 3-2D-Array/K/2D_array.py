def fibonacciloop(l, i):  
    if i != 0:
        l.append(l[-1] + l[-2])
        fibonacciloop(l, i-1)
    
def get_non_perfect_nums(nums):
    nonperfect_l = list()
    for i in range(1, nums+1):
        sumdiv = 0
        for a in findalldivs(i):
            sumdiv = a + sumdiv
        if sumdiv != i:
            nonperfect_l.append(i)
    return nonperfect_l       
        
def findalldivs(num):
    l_s = list()
    for x in range(1,num):
        if num % x == 0:
            l_s.append(x)
    return l_s

fibonacci_list_cal = [0, 1]
fibonacciloop(fibonacci_list_cal, 19)
non_perfect_list = get_non_perfect_nums(22)

productlist = list()
for n1, n2 in zip(non_perfect_list, fibonacci_list_cal):
    p = n1 * n2
    productlist.append(p)

outputlist = [non_perfect_list, fibonacci_list_cal, productlist]

print(outputlist)







       


        

       
