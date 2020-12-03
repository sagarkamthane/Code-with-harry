
#file = open('new.txt','r')
#file = open('new.txt')          #by default mode is r
file = open('new.txt','r')
# data = file.read()
data = file.read(6)              #reads first 5 chars
print(data)
file.close()


# r = opens file in read mode
# w = opens file in write mode
# a = opens file in append mode
# + = opens file in read and write mode
#
# rb = binary mode
# rt = txt mode(t by default)