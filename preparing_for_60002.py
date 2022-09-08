
import numpy
import pandas
import scipy
import sklearn
# Charles Thomas Wallace Truscott Watters
# Massachusetts Institute of Technology
# Thank you Eric Grimson, John Guttag and Ana Bell
# Thank you edX.org for allowing me to sit 6.0001 and 6.0002 from the Massachusetts Institute of Technology
# Decimal to Binary Conversion for Postive Signed Integers up to 2^63
def return_binary(integer_n):
    binary_string = ""
    if integer_n // 9223372036854775808 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 9223372036854775808
    else:
        binary_string += str(0)
    if integer_n // 4611686018427387904 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 4611686018427387904
    else:
        binary_string += str(0)
    if integer_n // 2305843009213693952 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 2305843009213693952
    else:
        binary_string += str(0)
    if integer_n // 1152921504606846976 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 1152921504606846976
    else:
        binary_string += str(0)
    if integer_n // 576460752303423488 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 576460752303423488
    else:
        binary_string += str(0)
    if integer_n // 288230376151711744 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 288230376151711744
    else:
        binary_string += str(0)
    # 2 ^ 58
    if integer_n // 144115188075855872 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 144115188075855872
    else:
        binary_string += str(0)
    if integer_n // 72057594037927936 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 72057594037927936
    else:
        binary_string += str(0)
    if integer_n // 36028797018963968 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 36028797018963968
    else:
        binary_string += str(0)
    if integer_n // 18014398509481984 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 18014398509481984
    else:
        binary_string += str(0)
    if integer_n // 9007199254740992 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 9007199254740992
    else:
        binary_string += str(0)
    if integer_n // 4503599627370496 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 4503599627370496
    else:
        binary_string += str(0)
    if integer_n // 2251799813685248 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 2251799813685248
    else:
        binary_string += str(0)
    if integer_n // 1125899906842624 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 1125899906842624
    else:
        binary_string += str(0)
    if integer_n // 562949953421312 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 562949953421312
    else:
        binary_string += str(0)
    if integer_n // 281474976710656 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 281474976710656
    else:
        binary_string += str(0)
    if integer_n // 140737488355328 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 140737488355328
    else:
        binary_string += str(0)
    if integer_n // 70368744177664 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 70368744177664
    else:
        binary_string += str(0)
    if integer_n // 35184372088832 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 35184372088832
    else:
        binary_string += str(0)
    if integer_n // 17592186044416 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 17592186044416
    else:
        binary_string += str(0)
    if integer_n // 8796093022208 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 8796093022208
    else:
        binary_string += str(0)
    if integer_n // 4398046511104 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 4398046511104
    else:
        binary_string += str(0)
    if integer_n // 2199023255552 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 2199023255552
    else:
        binary_string += str(0)
    if integer_n // 1099511627776 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 1099511627776
    else:
        binary_string += str(0)
    if integer_n // 549755813888 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 549755813888
    else:
        binary_string += str(0)
    if integer_n // 274877906944 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 274877906944
    else:
        binary_string += str(0)
    if integer_n // 137438953472 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 137438953472
    else:
        binary_string += str(0)
    if integer_n // 68719476736 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 68719476736
    else:
        binary_string += str(0)
    if integer_n // 34359738368 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 34359738368
    else:
        binary_string += str(0)
    if integer_n // 8589934592 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 8589934592
    else:
        binary_string += str(0)
    if integer_n // 8589934592 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 8589934592
    else:
        binary_string += str(0)
    if integer_n // 4294967296 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 4294967296
    else:
        binary_string += str(0)
    if integer_n // 2147483648 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 2147483648
    else:
        binary_string += str(0)
    if integer_n // 1073741824 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 1073741824
    else:
        binary_string += str(0)
    if integer_n // 536870912 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 536870912
    else:
        binary_string += str(0)
    if integer_n // 268435456 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 268435456
    else:
        binary_string += str(0)
    if integer_n // 134217728 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 134217728
    else:
        binary_string += str(0)
    if integer_n // 67108864 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 67108864
    else:
        binary_string += str(0)
    if integer_n // 33554432 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 33554432
    else:
        binary_string += str(0)
    if integer_n // 16777216 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 16777216
    else:
        binary_string += str(0)
    if integer_n // 8388608 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 8388608
    else:
        binary_string += str(0)
    if integer_n // 4194304 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 4194304
    else:
        binary_string += str(0)
    if integer_n // 2097152 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 2097152
    else:
        binary_string += str(0)
    if integer_n // 1048576 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 1048576
    else:
        binary_string += str(0)
    if integer_n // 524288 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 524288
    else:
        binary_string += str(0)
    if integer_n // 262144 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 262144
    else:
        binary_string += str(0)
    if integer_n // 131072 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 131072
    else:
        binary_string += str(0)
    if integer_n // 65536 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 65536
    else:
        binary_string += str(0)
    if integer_n // 32768 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 32768
    else:
        binary_string += str(0)
    if integer_n // 16384 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 16384
    else:
        binary_string += str(0)
    if integer_n // 8192 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 8192
    else:
        binary_string += str(0)
    if integer_n // 4096 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 4096
    else:
        binary_string += str(0)
    if integer_n // 2048 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 2048
    else:
        binary_string += str(0)
    if integer_n // 1024 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 1024
    else:
        binary_string += str(0)
    if integer_n // 512 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 512
    else:
        binary_string += str(0)
    if integer_n // 256 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 256
    else:
        binary_string += str(0)
    if integer_n // 128 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 128
    else:
        binary_string += str(0)
    if integer_n // 64 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 64
    else:
        binary_string += str(0)
    if integer_n // 32 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 32
    else:
        binary_string += str(0)
    if integer_n // 16 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 16
    else:
        binary_string += str(0)
    if integer_n // 8 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 8
    else:
        binary_string += str(0)
    if integer_n // 4 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 4
    else:
        binary_string += str(0)
    if integer_n // 2 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 2
    else:
        binary_string += str(0)
    if integer_n == 1:
        binary_string += str(1)
    else:
        binary_string += str(0)

    print(binary_string[::])

def main():
    return_binary(93)
    print("\n")
    return_binary(187649984473770)
    """ 0000000000000000000000000000000000000000000000000000000001011101


0000000000000000101010101010110010101010101010101010101010101010
The thread 'MainThread' (0x1) has exited with code 0 (0x0).
The program 'python.exe' has exited with code 0 (0x0).
"""

if __name__ == "__main__":main()