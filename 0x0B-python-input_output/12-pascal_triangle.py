#!/usr/bin/python3
"""
    ...
    ...
"""
def pascal_triangle(n):
    """
        pascal tr
    """
    fList = [] 

    sList = []
    for i in range(1,n+1):
        sList.clear()
        for j in range(0,i):
            try :
                if len(fList) > 0 :
                    sList.append( sumList(fList[i-2][j-1:j+1]) ) 
                else:
                    sList.append(1)
            except :
                sList.append(1)
        
        
        if not i < n :
            break
        fList.append(sList.copy())
    
    
    if len(sList) > 0:
         fList.append(sList)
         
    return fList
    
    
def sumList(list):
    
    if len(list) == 2 :
        return list[0] + list[1]
    
    return 1
    

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(8))