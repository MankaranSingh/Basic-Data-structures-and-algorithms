lst=eval(input('Enter list: '))
element=int(input('Enter element to be searched: '))
mini=0
maxi=len(lst)-1
middle=int((mini+maxi)/2)

while maxi>=mini:
    if element>lst[middle]:
        mini=middle+1
        
        middle=int((mini+maxi)/2)
    elif element==lst[middle]:
        print('element found at index: ', middle)
        break
    else:
        maxi=middle-1
        
        middle=int((mini+maxi)/2)
        
    
