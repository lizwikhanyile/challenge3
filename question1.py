
### START FUNCTION
def remove_adjacent(nums):
    
    # Empty list to store a new list
    removed = []
    
    # Check if are there elements in a given list
    if len(nums) > 0:
        
        # store the first element
        removed = [nums[0]]
        
        # use for loop and range function through the entire list and compare
        # the previous and next element on a list
        # append removed if the condition is true 
        for element in range(len(nums)-1):
            if nums[element] != nums[element + 1]:
                removed.append(nums[element + 1])
                
    return removed 
### END FUNCTION
print(remove_adjacent([9, 7, 14, 7, 7]))
      