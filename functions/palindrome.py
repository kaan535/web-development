def pal(st):
    left = 0
    right = len(st)-1
    while right >= left:
        if not st[left]== st[right]:
            return False
        left += 1
        right -= 1
    return True
print(pal("racecar"))