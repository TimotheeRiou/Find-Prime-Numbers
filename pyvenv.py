#FIND THE PRIME NUMBERS

n=int(input("Enter a positive number n: "))
start = 1
end = n
for val in range(start, end + 1):

    if val > 1:
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            print(val)