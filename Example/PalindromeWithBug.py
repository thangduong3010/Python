def isPal(L):
    temp = L[:]
    temp.reverse()

    if temp == L:
        return True
    else:
        return False

def silly(x):
    result = []
    for i in range(x):
        e = input("Enter element: ")
        result.append(e)
    #print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')

silly(int(input('How many character do you want to fit in? ')))