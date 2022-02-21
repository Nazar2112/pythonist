arr= input().split()
print (arr)
#for obj in arr:
    #print (type(obj))
#    obj=int(obj)
    #print (type(obj))
#for n in range(arr.__len__()):
#    arr[n]=int(arr[n])
#print (arr)



arr=list(map(int,arr))
print (list(arr))  
maxscore = max(arr)
scoreup=0
for obj in arr:
    if scoreup < maxscore and scoreup < obj and obj < maxscore:
        scoreup = obj
print (f"runner-up score is {scoreup}")
