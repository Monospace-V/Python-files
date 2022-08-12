# Sum of inverted primes, any given amount of terms
# OK. To take n:
s=0
n=int(input("How many prime terms you want: "))
primeCount=1 # Counter of primes
TestedValue=1 # Value we're testing. Actual pH.
while primeCount<=n:
    pFlag=True # Enter PrimeFlag in here or it'll never change. Always re-initialize within loop
    TestedValue+=1 # This converts it from 1 to 2 for the first number tested. 2 is prime but one is just "?"
    if TestedValue>3:
        TestedValue+=1 # Will be even at this stage. Adds 1.
    UL=int(((TestedValue**0.5)//1)+1)
    for i in range(2,UL):
        if TestedValue%i==0:
            pFlag=False
            break
    if pFlag==True:
        s+=(1/TestedValue)
        primeCount+=1
    if pFlag==False:
        continue
print(s)
# For 2: 0.8333333333333333
# For 3: 1.0333333333333332
# For 5: 1.2670995670995668
# For 1000000: 3.1 something something.
