def find_rightmost_set_bit(num):
    if num == 0:
        return 0  
    position = 1
    while (num & 1) == 0:
        num >>= 1
        position += 1
    return position

# Main program
num = int(input("Enter number: "))
binary = bin(num)[2:]
print(f"({binary})")
position = find_rightmost_set_bit(num)
print(f"Position of the first set bit: {position}")