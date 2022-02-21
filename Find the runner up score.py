if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
arr = list(arr)
maxscore = max(arr)
scoreup = -100
for obj in arr:
    if scoreup < maxscore and scoreup < obj and obj < maxscore:
        scoreup = obj
print (scoreup)
