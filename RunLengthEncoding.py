def encode(arr):
    p=arr[0]
    pc=0
    fs=""
    for i in arr:
        if p==i:
            pc+=1
        else:
            fs+=p+str(pc)
            p=i
            pc=1
    fs+=p+str(pc)
    return fs
