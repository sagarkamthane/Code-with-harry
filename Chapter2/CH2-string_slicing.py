# first = "sagar"
#         #0 1 2 3 4
#         #-5-4-3-2-1
# middle = "sanjeev "
# last = "kamthane"
#
# print(first + middle + last)  #concatination
#
# print(first[0])
#
# #first[0] = "S" --> not supported
#
# print(len(first))
# print(first[0:3]) #including 0 and excluding 3 i.e. 0 to 2 indexes
# print(first[1:4])
# print(first[:4]) #same as [0:4]
# print(first[2:]) #same as [2:last index]
# print('->', first[-5:2])
#
#slicing

sen = "sagar is a good guy, and this guy is very intelligent"
# print(sen[0: :2])  #skips every 2nd character
# print(sen[0:19])

#String functions
print(len(sen))
print(sen.endswith('guy'))
print(sen.count('a'))
print(sen.count('good'))
print(sen.capitalize())
print(sen.find("guy")) #finds first occurrance
print(sen.replace('guy', 'boy')) #replaces all found word

