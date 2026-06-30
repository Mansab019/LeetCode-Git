def numJewelsInStones(jewels, stones):
    jewel_set = set(jewels)
    count = 0
    for stone in stones:
        if stone in jewels:
            count +=1
    return count

jewels = "zz"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))  