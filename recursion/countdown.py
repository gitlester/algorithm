def countdown(i):
    print(i)
    if i<= 1:
        return 0
    else:
        countdown(i-1)

print(countdown(5))
