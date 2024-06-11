'''
Leetcode : 202
Problem Statement : https://leetcode.com/problems/happy-number/description/
'''

def is_happy(n):

    def get_next(number):
        # Create a total_sum to keep track of total sum
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit ** 2
            number //= 10
        return total_sum

    # Initialize an empty set to store all the numbers we have encountered.
    seen = set()
    # Using a while loop that continiues as long as n is not 1 and n is not in seen.
    while n!=1 and n not in seen:
        # Inside the while loop add n to seen 
        # and update n to the result of get_next(number)
        seen.add(n)
        n = get_next(n)
    return n == 1
    

#Example usage
print(is_happy(19))
print(is_happy(2))
