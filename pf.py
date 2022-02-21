def is_leap(year):
    leap = False 
    nleap = True
    if year % 4 ==0 and year % 400 == 0:
        return nleap
    elif year % 100 ==0:
        return leap
    elif year % 4 ==0:
        return nleap
    else:
        return leap

      
    


year = int(input())
print(is_leap(year))
