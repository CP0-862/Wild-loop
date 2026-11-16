#n=int(input("Enter a number:"))
#i=1
#while i<=30:
#    print(n*i)
#    i +=1

#list
#nums = [1,4,9,16,25,35,49,64,81,100]
#idx=0
#while idx < len(nums):
#    print(nums[idx])
#    idx += 1

#nums =(1, 4 ,9 ,16 ,25 ,36 ,49)
#x = 36
#i = 0
#while i< len (nums):
#    if (nums[i]==x):
#        print("Found")
#    i += 1

nums =(1, 4 ,9 ,16 ,25 ,36 ,49)
x=36

i=0
while i < len (nums):
    if(nums[i]==x):
     print("found at idx", i)
    else:
       print("finding..")
    i += 1