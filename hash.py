###expected is the value to get reversed
expected = 930846109532517


letters = "acdegilmnoprstuw"
## final answer required in reverse
ans = ''
while 1:
    if expected==7:
        break
    for i in range(16):
        if (expected-i)%37==0:
            ans += letters[i]
            expected -=i
            expected/=37
            break


print ans[::-1]


