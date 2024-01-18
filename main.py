# n = int(input("Enter n: "))
# a = int(input("Enter a: "))

# sum = 0

# for i in range(n):
#     temp = i + 1
#     val = ((temp**temp)/(a**i))
#     sum = sum + val
#     print(val)

# print(sum)

def print_series(n):
    sum_of_series = 0
    for i in range(1, n+1):
        term = i**4 - 4
        print(term, end = " ")
        sum_of_series += term
    print("\nSum of series:", sum_of_series)

# Test the function
print_series(5)