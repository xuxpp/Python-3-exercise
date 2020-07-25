nums = int(input("Enter range :"))

def getfectnum(nums):
    for i in range(1, nums+1):
        sumdiv = 0
        for a in findalldivs(i):
            sumdiv = a + sumdiv
        if sumdiv == i:
            print(i)
        
        
def findalldivs(num):
    ls = list()
    for x in range(1,num):
        if num % x == 0:
            ls.append(x)
    return (ls)

getfectnum(nums)             


        

       
