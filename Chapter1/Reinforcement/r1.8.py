def result(s, k):
    j = negative_to_positive_index(s, k)
    print("s["+str(j)+"]="+s[j]+" and k["+str(k)+"]="+s[k]+"")

def negative_to_positive_index(s, k):
    n = len(s)
    return n + k if k < 0 else k

 
result("hello", -3)
result("hello", 0)
result("python", -1)
result("python", -5)

# Outputs
# s[2]=l and k[-3]=l
# s[0]=h and k[0]=h
# s[5]=n and k[-1]=n
# s[1]=y and k[-5]=y