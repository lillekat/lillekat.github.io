numberOfWords = int(input())

# num_linjer = input()
# l1 = input()
# l2 = input()
# l3 = input()
# l4 = input()
# l5 = input()
# print(l1)
# print(l3)
# print(l5)

odd = True

while (numberOfWords > 0):
    word = input()
    if (odd):
        print(word)

    odd = not odd
    numberOfWords = numberOfWords - 1

