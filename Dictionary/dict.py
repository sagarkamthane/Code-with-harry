dict = {"sagar" : "samudra",
        "neha" : "love",
        "marks" : [70, 67, 98, 90],
        "anotherdict" : {'bro' : 'bhau'}
        "x" : 3,
        1 : 2}

# dict['marks'][2] = '94'
# print(dict['sagar'],":", dict["marks"][2] , '\n',dict['neha'],":", dict["marks"][2], '\n', dict['anotherdict']['bro'])

#methods
print(dict.keys())          #prints keys of dict
print(dict.values())        #prints values of dict
print(type(dict))           #prints type of dict
print(list(dict.keys()))    #prints keys of dict in list format
print(list(dict.items()))   #prints contents(key value pair) of dict in list format

updatedict = {'om' : 'hindu chant', 'sagar' : 'ocean' }         #overrides samudra with ocean

dict.update(updatedict)     #adds uddate dict dictionaries contents to dict
print(dict)

print(dict.get('sagar'))
print(dict.get('sagar2'))   #Returns None if key not present
#print(dict["sagar2"])       #throws error if key not present
