from collections import Counter

def uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)
    
    uncommon = list((count1 - count2).elements()) + list((count2 - count1).elements())
    
    return uncommon

list1 = [1, 1, 2]
list2 = [2, 3, 4]
print(uncommon_elements(list1, list2)) 

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(uncommon_elements(list1, list2))  

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
print(uncommon_elements(list1, list2))  
