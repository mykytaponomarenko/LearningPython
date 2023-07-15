#1 Use underscore to ignore a value returned by a function. 

#2 Never use underscore as an input to a function or operation. 
If you need to track a variable, take the time to give it a descriptive name.

#3 If you are the author of a class:

    a. Provide a “get” method for each local variable you intend consumers of your class to read.
    b. Use underscore to indicate that variables should be considered private.

#4 If you are the consumer of a class someone else has written:

    a. Avoid accessing class local variables directly if possible.
    b. Absolutely avoid accessing class variables prepended by an underscore directly at all costs. The author put that underscore (or pair of underscores) there for a reason.

#5 Avoid importing a function that has been marked as private.