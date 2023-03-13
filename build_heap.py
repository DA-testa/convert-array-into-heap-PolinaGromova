# python3


def build_heap(data):

    swaps = []
    size=len(data)
    
    for i in range((size//2)-1,-1,-1):
        j=i
        while True:
            right=2*j+2
            left=2*j+1
            
            #finding smallest
            if left<size and data[left]<data[j]:
                j=left
            if right<size and data[right]<data[j]:
                j=right
            
            #is i a leaf node
            if i!=j:
                data[i], data[j]=data[j],data[i]
                swaps.append((i,j))
                i=j
            else: break    

    if len(swaps)>4*len(data):
        raise Exception("The number of swaps is greater than 4n")        

    return swaps


def main():

    # TODO : add input and corresponding checks
    text=input("Enter I or F: ")
    if "F" in text:
        filename = input("Enter file name: ") 
        with open(filename) as f:
                n=int(f.readline())
                data=list(map(int,f.readline().split()))
        

    elif "I" in text:
        n= int(input())
        data=list(map(int,input().split()))



    else: print("Input error")
    
    assert len(data) == n
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    


    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
