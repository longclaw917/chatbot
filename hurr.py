contact = {'kunal':'+918697503203','shruti':'+919748934716','baba':'+919674782833','madhumita':'+916290287808'}
num = input("enter the no:" )
def binary_search(contact, low, high, num):
    if high >= low:
    
        mid = (high + low) // 2
    
        # If element is present at the middle itself
        if contact[mid] == num:
            return mid
    
        # If element is smaller than mid, then it can only
        # be present in left subcontactay
        elif contact[mid] > num:
            return binary_search(contact, low, mid - 1, num)
    
        # Else the element can only be present in right subcontactay
        else:
            return binary_search(contact, mid + 1, high, num)
    
    else:
        # Element is not present in the contactay
        return -1




people = binary_search(contact,0,len(contact),num)

print(contact[people])