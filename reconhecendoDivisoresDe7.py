n = input()
    
while(int(n)>70 and n[0]!='-'):
    c=2*int(n[-1])
    n=str(int(n[:-1])-c)
print(n,"NO" if int(n)%7 else "YES")




# Here is the trick to check - without a calculator - if a number is divisible by 7:

# Example number = 541926

# 1. Remove the last digit k (=6) from the number, which gives 54192
# 2. Subtract 2*k from the result: 54192 - 2*6 = 54180

# 541926 is divisible by 7 if and only if 54180 is divisible by 7. 54180 is still a large number, so we repeat the process until we get a number, where we can easily see the divisibility by 7.

# 541926, 54180, 5418, 525, 42

# We conclude: 541926 is divisible by 7, because 42 is divisible by 7.

# Your task is to produce for a given input this sequence of numbers and output the first number in this sequence which is 70 or less (because we can then surely recognize, if the number is divisible by 7). Then add a YES or NO to the output, indicating the final decision about the divisiblity by seven.

# For input 541926, the output is:
# 42 YES

# Input
# 71
# Output
# 5 NO