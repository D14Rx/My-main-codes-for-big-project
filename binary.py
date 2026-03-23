def binar_code(sequence, item): #creating a function
    start = 0 #the main count(starts with 0 number)
    end = len(sequence) - 1 #end variable is a length or max index of a "sequence" variable(-1 because counting starts from 0)

    while start <= end: #while "start" variable is lower or equal to end variable
        mid_num = start + (end - start) // 2 #finding index(position) of a mid element 
        mid_num_value = sequence[mid_num] #creating a "mid_num_value" variable that is equal to "sequence" variable which contains the "mid_num" variable specific value
        if mid_num_value == item: #if "mid_num_value" numbers is equal to "item" variable it will got to you a "mid_num" variable number
            return mid_num
        
        elif item < mid_num_value: #if item number is lower than "mid_num_value" numbers it will "end" will be equal to "mid_num" number
            end = mid_num - 1
        else:
            start = mid_num + 1 #else if "item" is bigger than "mid_num_value" and then when algorythm makes his action it will start again until it finds a number that need to be founded
    return None
    
sequence_a = [2,4,6,8,10,12,14] #creating a variable for test
item_a = 10 #a number that need to find

print(binar_code(sequence_a, item_a)) #print from "binar_code" function a "sequence_a", "item_a" results