# pre-processing the input message m,
# heavily inspired by pseudocode from wikipedia sha-2
# assume the length of m (in binary format) is l bits, we want to padding it into a multiple of 512(like 512, 1024, 1536, 2048....)
# plan:
# 1. append a single "1" bit. 2. append k "0" bits, where k is the minimum number >= 0 s.t. l + 1 + k + 64 is a multiple of 512,
# in other word, k = n * 512 - 64 - 1 - l where n is the minimum positive integer possible to make k a non negative number.
# 3. append l as a 64-bit big-endian integer.
# after padding, it is <m of length l> + "1" + <k zeors> + < l as 64 bit integer>, and the length = l + 1 + k + 64 = a multiple of 512 

def padding(m):
    # only work for string. other type may incur error.
    if isinstance(m, str):
        m = bytearray(m, 'ascii')
    else:
        raise TypeError
    
    # l = len of bits = len of bytes * 8
    l = len(m) * 8
    # append a single "1", here we actually append 0x80 which is "10000000", "1" followed by 7 "0" 
    m.append(0x80)
    return m






