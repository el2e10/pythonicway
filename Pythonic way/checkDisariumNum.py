# Python program to check whether a number is Disarium or not
import math 
 
# Method to check whether a number is disarium or not
def check(n):
 
    # Count digits in n.
    count_digits = len(str(n))
      
    # Compute sum of terms like digit multiplied by
    # power of position
    sum = 0  # Initialize sum of terms
    x = n
    while (x!=0):
 
        # Get the rightmost digit
        r = x % 10
          
        # Sum the digits by powering according to
        # the positions
        sum = (int) (sum + math.pow(r, count_digits))
        count_digits = count_digits - 1
        x = x/10
        
    # If sum is same as number, then number is
    if sum == n:
        return 1
    else :
        return 0
       
# Driver method
n = 135
if (check(n) == 1):
    print("Disarium Number")
else:
    print("Not a Disarium Number")