def array_diff(arr1, arr2):
    result = []
    
    for num in arr1:
        found = False
        
        for exclude in arr2:
            if num == exclude:
                found = True
                break
        
        # --- THE FIX IS HERE ---
        # Only append if 'found' is still False (meaning it was NOT in arr2)
        if not found:
            result.append(num)
            
    return result

# Test cases
print(array_diff([1, 2, 3], [2]))             # Output: [1, 3] (Correct)
print(array_diff([1, 2, 2, 3], [2]))          # Output: [1, 3] (Correct)
# ... all other test cases will now work as expected!