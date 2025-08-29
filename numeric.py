x = 1172.5
# This method represents the float as a fraction, which can be useful for some mathematical calculations

x.as_integer_ratio()
# (2345, 2)
# Checks if the float is an integer value. In this case, 1172.5 is not an integer, so it returns False
x.is_integer()
# False

y = 12345
y.numerator    # For integers, the numerator is the number itself
# 12345
y.denominator    # For integers, the denominator is always 1
# 1
y.bit_length()    # This method tells you the number of bits required to represent the number in binary, which can be useful in bitwise operations
# 14
