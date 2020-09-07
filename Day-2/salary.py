#Clean the Messy salary

salary = '$876,001' 


s = salary[1:]         
s1 = s.split(',')
s2 = "".join(s1)
s3 = int(s2)
print(s3)

# Using the Chaining Concept
print(int("".join(salary[1:].split(','))))