#N squirrels found K nuts and decided to divide them equally. Determine how many nuts each squirrel will get.
n = int(input())
k = int(input())
print(int((k - (k % n)) / n))
