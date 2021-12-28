def max_int(a,b):
	if a < b :
		return b
	else :
		return a

def min_int(a,b):
    if a < b :
        return a
    else :
        return b

def average(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum / len(a)

def std(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    avg = sum / len(a)
    sum1 = 0
    for i in range(len(a)):
        sum1 += (a[i]- avg)**2
    std = (sum1 / len(a))**0.5
    return round(float(std), 2)

def mediane(a):
    a.sort()
    if len(a)%2 == 1: 
        return a[int(len(a)/2)]
    else:
        return (a[int(len(a)/2)] + a[int(len(a)/2) - 1])/2
    
def arithmetic(a):
    equ = a[1] - a[0]
    for i in range(len(a)-1):
        if a[i+1] - a[i] == equ:
            continue
        else:
            return False
    return True

def geometric(a):
   return -1
