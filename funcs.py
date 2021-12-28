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
   return -1