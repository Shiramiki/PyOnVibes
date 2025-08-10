arr= [28078, 19451, 935, 28892, 2242, 3570, 5480, 231]
def getSecondLargest(arr):
        # Code Here
        largest =0
        secLargest = 0
        for item in arr:
            if (item > largest):
                if largest != 0:
                    secLargest = largest
                largest = item
            if (secLargest < item) and (item < largest):
                secLargest = item
                    
        if (secLargest == 0):
            return -1
        else:
            return(secLargest)


ans = getSecondLargest(arr)     
print(ans)