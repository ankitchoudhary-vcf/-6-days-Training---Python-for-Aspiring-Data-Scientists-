# salary
salaries = ['$876,001', '$543,903', '$2453,896'] 


# version 1

new_salaries=[]

for salary in salaries:
    s = salary[1:]
    s1 = s.split(',')
    s2 = "".join(s1)
    s3 = int(s2)
    new_salaries.append(s3)
    # Using the Chaining Concept
    #new_salaries.append(int("".join(salary[1:].split(','))))
print(new_salaries)    



# version 2
salaries = ['$876,001', '$543,903', '$2453,896'] 
new_salaries=[]

for salary in salaries:
    new_salaries.append(int("".join(salary[1:].split(','))))

print(new_salaries)    