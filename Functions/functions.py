marks1 = [80,80,80,80]
marks2 = [80,80,80,80,80,80]

def percent(marks):
    return (sum(marks)/(len(marks)*80))*100

print(f'{percent(marks1)}%')
print(f'{percent(marks2)}%')

