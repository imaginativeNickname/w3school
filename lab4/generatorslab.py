n = int(input())

#1 task
def square(n):
    for i in range(n):
        yield i**2

print(list(square(n)))

print()

#2 task
def printing_even(n):
    for i in range(n+1):
        if i % 2 == 0 and i !=0:
            yield str(i)

vowels_str = ", ".join(printing_even(n))
print(vowels_str)

print()

#3 task
def divisible_by_4_and_3(n):
    for i in range(n):
        if i % 12 == 0:
            yield i

print(list(divisible_by_4_and_3(n)))

print()

#4 task
m = int(input())
def squares(n,m):
    for i in range(n,m+1):
        yield i**2

print(list(squares(n,m)))

print()

#5 task
def rewind(n):
    for i in range(n, -1, -1):
        yield i

print(tuple(rewind(n)))
