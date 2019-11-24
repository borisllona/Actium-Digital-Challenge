digits = []

def result(filei):
    with open(filei) as f:
            for line in f:
                for n in line:
                    if n != '\n':
                        if digits == []: digits.append(n)
                        elif n not in digits: digits.insert(findPosition(n,filei),n)
    return digits

def findPosition(n,filei):
    for j in digits:
        with open(filei) as f:
            for line in f:
                if j in line and n in line:
                    if line.index(j) > line.index(n): return digits.index(j)
    return len(digits)        


if __name__ == "__main__":    
    print("La combinació és: ", end ='')
    for i in ['1.txt','2.txt','3.txt']:
        for j in result(i): print(j, end='')
        digits = []
    print('')