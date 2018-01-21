Step 1:- Start

Step 2:- importing the library "time" using import 'time' and import 'time' as 't'.

Step 3:- generate random numbers using v2 = int(str(time() - int(time()))[-1]), int(str(time() - int(time()))[-2])
 and return the random numbers generated.

Step 4:- ensure the relationship fits that of an lcg and return the "random" result, and then check the validity of the relation using 
   r = 0 <= increment < modulus and 0 <= seed < modulus and multiplier in [1, 3, 7, 9]. which returns a boolean value.

Step 5:- create a list with the first element as seed and generate random numbers and append them into the output.

Step 6:- convert the integer into string after iterating them and join them as a single string after aking a list. using  result = int(str(''.join([str(i) for i in output]))[-1])
 
Step 7:- taking two variables maxv=[] and minv=[] for returning the biased output after generating the random numbers.

Step 8:- implementing conditions for values greater than and less than the iddle value with the biasedness of 73% to the higher value. using 
            if len(maxv)<73:
            maxv.append(num)
Step 9:- Then finally printing the desired output value which is, the minv and the maxv values.

Step 10:- Stop
