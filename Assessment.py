
z = [x for x in range(1,101) if x % 10 == 0]    # Assume we are checking for multiples of 10 in order to get 10 numbers
z = list(dict.fromkeys(z))                      # Checking to make sure there are no duplicates in the list 
z.sort(reverse=True)                            # Reversing the list
print(z)