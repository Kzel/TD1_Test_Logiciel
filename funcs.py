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
    return -1