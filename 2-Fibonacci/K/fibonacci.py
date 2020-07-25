# fibonacci_list_cal = [0,1]
# i = 0
# sum = 0
# fibonacci_list = list()

# for x in fibonacci_list_cal:
#     sum = sum + x
#     fibonacci_list_cal.append(sum)
#     fibonacci_list.append(sum)
#     i += 1
#     if i == 21:
#         break
# print(fibonacci_list)


def fibonacciloop(l, i):  
    if i != 0:
        l.append(l[-1] + l[-2])
        fibonacciloop(l, i-1)
    

fibonacci_list_cal = [0, 1]
fibonacciloop(fibonacci_list_cal, 19)

print(fibonacci_list_cal)



       


        

       
