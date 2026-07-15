def decimal_to_binary(dec):
    ans=0
    power=1
    while dec>0:
        remainder=dec%2
        dec //=2
        ans += (remainder*power)
        power *=10
    return ans

def binary_to_decimal(bi):
    ans=0
    power=1
    while bi>0:
        remainder=bi%10
        ans += remainder*power
        bi=bi//10
        power *= 2
    return ans