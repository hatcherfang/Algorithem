################################
#
# The definition of a Fibonacci sequence is like this:
# - F(0) = 0
# - F(1) = 1
# - F(n) = F(n-1) + F(n-2)
#
# Now let's define G(n) = F(n)/F(n+1).
#
# Golden ratio is the limit of G(n) when n approaches infinity.
#
# With all the above information, we have a way to estimating golden ratio g: 
# 
# Find the first n that matches |G(n+1) - G(n)| < t, where t is the 
# precision threshold, then the corresponding G(n) is considered as 
# the estimated value of golden ratio.
#


def Fibo(n, array):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    i = 2
    f0 = 0
    f1 = 1
    while i <= n:
        f3 = f0 + f1
        f0 = f1
        f1 = f3
        i = i + 1
        array.append(f3)
    return f3


def G(n):
    if array[n+1] == 0:
        return 0
    return float(array[n])/array[n+1]

def estimate_golden_ratio(t):
    n = 0
    while abs(G(n+1) - G(n)) >= t and n <= 50:
        n = n + 1
    return n
        
            
if __name__ == "__main__":
    global array
    array = [0, 1]
    Fibo(50, array)
    print estimate_golden_ratio(1e-6)
    print estimate_golden_ratio(1e-8)
    print estimate_golden_ratio(1e-10)
    print estimate_golden_ratio(1e-12)
