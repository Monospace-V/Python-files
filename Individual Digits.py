# Extract individual digits of a 4 digit number. And add them.
# ToDo: Use len and figure out Python's equivalent of the java array.
# Ideally before it's taught in class, because damn are they fast...
# and yet far too slow.
# Then figure out any-length.
# Also loops. They won't teach it this year, the fools.

# Mainly to check concepts with self. Have I actually learnt anything?

""" Considered taking as string, grabbing index value 0 thru 3 and typecasting
 into integer. Didn't go well with Ma'am. She proceeded, obviously, to make
 an example out of me. Not that I mind, I'm an excellent example. But whatever.
 Using strng and index if you don't know how to floor and mod is
 not very sensible."""

tbc=float(input("Input a four-digit integer: "))
if tbc%1!=0 or tbc<1000 or tbc>9999: # Need POSITIVE, need FOUR DIGIT
    print("Invalid input")
else:
    tbc=int(tbc) # Typecast to integer now as it's obviously valid.
    n1=tbc # Assign: Placeholder Variable
    d4=n1%10 # Final digit
    n1//=10 # Cut off the final digit we just took
    d3=n1%10 # Final digit now, which is third...
    n1//=10
    d2=n1%10
    n1//=10
    d1=n1%10
    """Or just n1, but this allows me to process easier if/when
I eventually learn looping."""
    print("The digits are:",d1,",",d2,",",d3,",",d4,".")
    print("Their sum is:",d1+d2+d3+d4)
    # Might wanna reassign sum to separate variable.
    # How you gonna add all elements of an array? With another loop... i guess.
    """Ideally I'd do d1, d2 instead of d1 , d2 but it's not worth it
making a separator character nothing and then manually adding spaces,
OR typecasting to string then spacelessly concatenating it with +."""
# Holy hell though, it's a lot harder to debug like this. God. I
# swear, if ",d1,",",d2,",",d3,",",d4,"." isn't the ugliest most uncheckable
# thing I've ever seen-

# Also, no, I haven't remembered everything. ToDo: More absurd.
