num = int(input("enter a number: "))
divisors = []
# rough step
# for n in range(1, num+1):
#     if num % n == 0:
#         divisors.append(n)
# print(divisors)

for n in range(1, int(num / 2)):
    if num % n == 0:
        divisors.append(n)
print(divisors)