# bitwise operation needed for sha256
# NIST Standard section 4.1.2

# bitwise operation in python
# and         &
# or          |
# xor         ^
# not         ~
# left shift  <<
# right shift >>

# Ch(x, y, z)
def Ch(x, y, z):
    return ( x & y) ^ ( ~x & z ) 

# Maj(x, y, z)
def Maj(x, y, z):
    return (x & y) ^ ( x & z) ^ (y & z)

# w is the bits for the word
w = 32

# Right rotation n bits
def RotR(x, n):
    return (x >> n) | (x << w - n)

# Left rotation n bits
def RotL(x, n):
    return (x << n) | (x >> w - n)


# Right shift n bits
def ShR(x, n):
    return x >> n