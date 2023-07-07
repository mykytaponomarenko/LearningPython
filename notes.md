0. #!/usr/local/bin/python

1. Python:
a) dynamically typed (it keeps track of types for you automatically instead of requiring declaration code)
b) strongly typed (you can perform on an object only operations that are valid for its type)
c) has garbage collection: cleans up unused memory by reclaiming space as soon as the last reference to an object is removed


2.  xdg-open   #Detect the default appropriate viewer and open the file with it (bash)

3. Use dir(object) function to return a list of all attributes available for given object

Names with underscores in received list represent the implementation of the object and are available to support customization. 
In general, leading and trailing double underscores is the naming pattern Python uses for implementation
details. The names without the underscores are the callable methods on particular object.

4. Empty Dir() gives methods' names. Use help() to ask what they do. For example help(dir) or help(spam.replace)

5. Nesting allows to build up complex information structures directly and easily. Use it!

6. After Python 3.0 types are classes and vice versa

7. Variables:
• are created when they are first assigned values.
• are replaced with their values when used in expressions.
• must be assigned before they can be used in expressions.
• refer to objects and are never declared ahead of time.

8. Check current Python implementation:
```
>>> import platform
>>> print(platform.python_implementation())
```

9. gc module is for garbage collection management 
Read more: https://stackify.com/python-garbage-collection/#:~:text=Reference%20counting%20in%20CPython&text=At%20a%20very%20basic%20level,for%20the%20object%20is%20deallocated

