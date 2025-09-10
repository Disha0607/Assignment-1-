#Your program should prompt the user with the message Enter temperature
# in Fahrenheit: .  Note the space at the end of this prompt.  You'll want to store the result in a variable.

#Choose a good name for your variable, i.e., a name that communicates what's being stored. Use snake case!

#You can test your program by running from the command line. The -i command-line 'flag' tells Python to run 
# the program and then drop into an interpreter. You can then inspect
# your program state (the variable where you've stored the user input).


#-------------------------------SOLUTION----------------------------------------

#storing a number , Explicitly converting into float
f = float(input("ENTER THE TEMPERATURE IN FAHRENHEIT= "))
c = (f - 32) * 5 / 9
print("THE TEMPERATURE CELSIUS WILL BE =", c)


