def remove_strip(string, word):
    newstr = string.replace(word,'')
    return newstr.strip()


print(remove_strip('     sagar is smart and handsome      boy', 'boy'))