i = 0
with open('log.txt', 'r') as f:
    while f.readline():
        a = f.readline()
        i+=1
        if 'rsvp' in a:
            print(f"rsvp is present at {i}")
