
print("hello")
print("goodbye")

#I added this comment in branch_1, added this to the comment
# I added this comment in the main branch
#branch_2 here, hello

def add(num : list) -> float:
    sum = 0
    for i in num:
        sum+= i
    return sum
  
num = [2,3,4,5]

sum = add(num)

print(sum)