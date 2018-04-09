class Sorts(object):
    def __init__(self):
        pass

    def bubbleSort(self, L):
        # stable sort
        print 'before bubbleSort:', L
        if not L or not isinstance(L, list):
            return
        i = 0
        length = len(L)
        while i < length:
            j = 0
            switchFlag = False
            while j + 1 < length-i:
                if L[j] > L[j+1]:
                    switchFlag = True
                    L[j], L[j+1] = L[j+1], L[j]
                j = j + 1
            if not switchFlag:
                # already ordered
                break
            i = i + 1
        print 'after bubbleSort:', L

    def insertSort(self, L):
        # stable sort
        print 'before insertSort:', L
        if not L or not isinstance(L, list):
            return
        length = len(L)
        i = 1
        while i < length:
            j = i
            tmp = L[i]
            while j > 0 and L[j-1] > L[j]:
                L[j-1], L[j] = L[j], L[j-1]
                j = j-1
            L[j] = tmp
            i = i + 1
        print 'after insertSort:', L

    def selectSort(self, L):
        # not stable sort
        print 'before selectSort:', L
        if not L or not isinstance(L, list):
            return
        length = len(L)
        for i in xrange(length):
            min_index = i
            for j in range(i+1, length):
                if L[min_index] > L[j]:
                    min_index = j
            if min_index != i:
                L[i], L[min_index] = L[min_index], L[i]
        print 'after selectSort:', L

if __name__ == '__main__':
    cs = Sorts()

    L = [3, 2, 4, 7, 1, 5]
    cs.bubbleSort(L)
    print
    L = [3, 2, 4, 7, 1, 5]
    cs.insertSort(L)
    print
    L = [3, 2, 4, 7, 1, 5]
    cs.selectSort(L)
    print
