from LogicGate import *

def full_adder(input):
    a = input[0]
    b = input[1]
    c = 0 if len(input) < 3 else input[2]

    x1 = XOrGate("XOr1", a, b)
    x2 = XOrGate("XOr2",  x1.get_output(), c) # SUM
    sum = x2.get_output()

    a1 = AndGate("A1", a, b)
    a2 = AndGate("A2", x1.get_output(), c)
    o1 = OrGate("O1", a1.get_output() ,a2.get_output()) #CARRY
    carry = o1.get_output()

    print(f'SUM: {sum} | Carry: {carry}')
    return (sum, carry)

def half_adder(input):
    sum = XOrGate("X1", input[0],  input[1]).get_output()
    carry = AndGate("A1",  input[0],  input[1]).get_output()
    print(f'SUM: {sum} | Carry: {carry}')
    return (sum,carry)

#full_adder((a,b,c))
number_one = int(input("Please Enter Number One: "))
bits_one = len(str(bin(number_one)))-2
number_two = int(input("Please Enter Number Two: "))
bits_two = len(str(bin(number_two)))-2

# Get max number of bits to process (pre determining overload)
max_bits = bits_one if bits_one >= bits_two else bits_two
print(f'Adders Required: {max_bits}')

#Convert to binary
#Remove the 0b formatting
bin_num_one = str(bin(number_one))[2:bits_one+2]
bin_num_two = str(bin(number_two))[2:bits_two+2]

#Pad Appropriately
#(If one number contains more bits than the other)
for i in range(max_bits - len(bin_num_one)):
    bin_num_one = "0" + bin_num_one
for i in range(max_bits - len(bin_num_two)):
    bin_num_two = "0" + bin_num_two

#Iterate through adders
bin_final_num = ""
pin_location = max_bits - 1
pin_counter = 1
c = 0
for i in range(max_bits):
    a = int(bin_num_one[pin_location])
    b =int(bin_num_two[pin_location])
    pin_location = pin_location - 1
    # Check to see if first
    if pin_counter == 1:
        res = half_adder((a,b))
    else:
        res = full_adder((a,b,c))
    bin_final_num = str(res[0]) + bin_final_num
    c = res[1]
    if pin_counter == max_bits:
        bin_final_num = str(c) + bin_final_num
    pin_counter = pin_counter + 1

print(f'Final Number Binary ({len(bin_final_num)} bits): {bin_final_num}')
print(f'Final Number Decimal: {int(bin_final_num,2)}')
