def mySqrt(x):
    l = 0
    r = x
    while abs(l-r) > 1e-10:
        mid = (l+r)/2
        print(l, r, mid)
        if mid > x/mid:
            r = mid-1
        elif mid < x/mid:
            l = mid+1
        else:
            return mid
    return l


if __name__ == "__main__":
    t = mySqrt(8)
    print(t)
