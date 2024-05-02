# """
# Operators :
#     Arithmetic : +,-,*,/,%,**,//
#     Assignment : =,+=,-=,*= ,/= ,%= ,//= ,**=
#     Comparison : ==,!=,>,<,>=,<=
#     Logical    : and, or, not
#     Membership : in , not in
#     Bitwise    :  &, |, ^, ~, <<, >>
# """

# print('Arithmetic Operators')

# # Add
# print(1 + 5)   #6

# # Sub
# print(1 - 5)   #-4

# # mul
# print(6 * 5)   #30

# # Float Division
# print(6 / 5)   #1.2

# # Integer Division
# print(6 // 5)   #1

# # mod
# print(6 % 3)   #0

# # Pow
# print(6 ** 2)   #36
# print(0 ** 0)   #1
# print(6 ** 0)   #1

# print('Operator Precedence')
# print(8 - 2 * 3)     #2
# print(8 + 2 / 3)     #8.6
# print(16 / 2 ** 3)   #2.0
# print(16 // 2 ** 3)  #2
# print(2**2**3)       #256
# print((2**2)**3)     #64

# print('Augmented Assignment Operator')
# x = 4
# x += 1      # x = x + 1
# print(x)    #5

# x = 4
# x -= 1      # x = x - 1
# print(x)    #3

# x = 4
# x /= 3      # x = x / 3
# print(x)    #1.33

# x = 4
# x //= 3      # x = x // 3
# print(x)     #1

# x = 4
# x %= 3      # x = x % 3
# print(x)    #1

# x = 4
# x **= 3      # x = x ** 3
# print(x)     #64

# print('Comparison Operators')

# print(2 == 2)   #True
# print(2 != 2)   #False
# print(2 < 2)    #False
# print(2 <= 2)   #True

# print('Logical Operators')

# print(1 < 3 and 4 > 5)   #False
# print(1 < 3 or 4 > 5)    #True
# print(not 1 < 3)         #False

