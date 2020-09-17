#string index

selfish = 'me me me!'
          #012345678
print(selfish[0],"\n")

print(selfish)

#string slicing
# [start:stop]
num = '123456789'
print(num[2:8])

# [start:stop:stepover]
print(num[2:8:2])

print(num[1:]) #start with 1 and end at end of sting

print(num[:5])

print(num[-2]) #negative index means it start form end

print(num[::-1]) #print reverse string