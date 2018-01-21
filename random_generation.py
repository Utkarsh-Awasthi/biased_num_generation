from time import time
import time as t
 
def values():
    v1 = v2 = 0
    while not v1 and not v2:
        try:
            v1, v2 = int(str(time() - int(time()))[-1]), int(str(time() - int(time()))[-2])
        except ValueError:
            values()
    return v1, v2
 
def rel(modulus, increment):
    r = 0
    while not r:
        multiplier, seed = values()
 
        r = 0 <= increment < modulus and 0 <= seed < modulus and multiplier in [1, 3, 7, 9]
 
    return multiplier, seed

def g_val(modulus, increment):
    multiplier, seed = rel(modulus, increment)
    output = [seed]
    current_iteration = -1 
    switch = False
 
         
    while current_iteration != seed and current_iteration != 0:
        if not switch:
            current_iteration = (seed * multiplier) + increment
            switch = True
        else:
            current_iteration = (current_iteration * multiplier) + increment
            if current_iteration > modulus:
                current_iteration %= modulus
            output.append(current_iteration)
 
         
    result = int(str(''.join([str(i) for i in output]))[-1])
    return result
start=t.ctime().split(" ")[3]
maxv=[]
minv=[]
m=10
i=0
loop=True
times=100
while loop:
    t.sleep(0.00000000000001)
    num=g_val(m,i)
    #print num
    if num >= 5:
        if len(maxv)<73:
            maxv.append(num)
    else:
        if  len(minv)<27:
            minv.append(num)
    if len(maxv)==73 and len(minv)==27:
        loop=False
end=t.ctime().split(" ")[3]
print(start,end)
print(len(minv),len(maxv))
print(minv)
print(maxv)
