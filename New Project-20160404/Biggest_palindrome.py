def ispal(x):
    x=str(x)
    y=len(x)/2
    a=x[0:y]
    if (len(x)%2==0) :b=x[len(x):y-1:-1]
    else : b=x[len(x):y:-1]
    if a==b : return True
    else: return False

def biggestmulti_for_pal(x,y):
    #input min and max for 2 numbers eg 100,999 to find biggest 3 digits multiplication results which palindrome
    biggest = 0;
    for a in range(x,y+1):
        for b in range(a,y+1):
            if(ispal(a*b)==True and (a*b) >biggest) :
                biggest = a * b
                i=int(a)
                j=int(b)
    print ("biggest pal : %s * %s = %d" %(i,j,biggest))
    return 0
    
biggestmulti_for_pal(100,999)
    
    