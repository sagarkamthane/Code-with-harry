with open('log.txt' , 'r') as f:
    a = f.read().lower()             #reads contents of file in lower case
    if 'rsvp' in a:                  #a.lower() also works
        print("python is present")
