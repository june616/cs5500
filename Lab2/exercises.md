# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping)
   and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL.
   Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

[1] Dictionary: Functions like pop for dictionaries remove a key and return its value, which is a two-action function. It may not be the most intuitive naming convention according to the question's criteria. Functions like keys, values, items, update, and get have intuitive names that describe what they do.

[2] List: Functions like append, remove, and count are quite descriptive of their operations. The function pop for lists, similar to the dictionary, removes the item at a specific position and returns it. According to the description, a more intuitive name might be 'popAndReturn' or 'popAndGet'.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

[1] A dictionary is a mutable, unordered collection of key-value pairs, where each key must be unique. Its underlying data structure is a hash table, allowing for fast key lookups.

[2] A list is a mutable, ordered collection of items, indexed by integers. The underlying data structure of a list is an array (or a dynamic array), enabling efficient indexed access. While lists maintain order, dictionaries prioritize key-based access.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes, a list does allow for random access. We can access any element by its index.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.).
   What do you think are the pros/cons of a library that can work with any data type?

Pros:

[1] Flexibility: Can handle a variety of data without the need for different data structures or methods for each type.

[2] Code Reusability: You don't need to recreate or redefine similar structures or methods for different data types.

[3] Easier Integration: Can easily integrate and work with varied data in a program without much hassle.

Cons:

[1] Performance: Might not be optimized for all data types, possibly leading to inefficiency in certain operations.

[2] Complexity: Handling various data types might make the underlying code more complex and harder to maintain.

[3] Error Potential: Increased risk of unintended behavior or bugs if not all data types are tested or if unexpected data types are introduced.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
   Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

I think the functions/methods in the Requests module appear to be clearly and logically named, making it easy to understand their purpose at a glance. For example:

[1] Standard HTTP Methods: The primary functions are named after standard HTTP methods (get(), post(), put(), patch(), delete(), head()). This makes it clear what type of request is being made. Their naming is both concise and reflective of their purpose.

[2] Exceptions: Exceptions are named descriptively to indicate the type of error (RequestException, ConnectionError, HTTPError, and so on). This makes it easy for developers to understand the type of error that occurred.

[3] Sessions: The Session class and its methods are appropriately named for managing and maintaining persistent settings across requests (get(), post(), and so on within a session).

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

Yes, looking at the requests.Request class, the initializer (i.e., **init** method) includes the following parameters: method, url, headers, files, data, params, auth, cookies, hooks, json. This totals to 10 parameters which is more than the heuristic limit of 5. Similarly, the prepare method in the requests.PreparedRequest class also has the same set of parameters, exceeding the heuristic limit.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?

[1] It is a special syntax in Python that allows passing a variable number of keyword arguments to a function. It allows users to pass any number of keyword arguments which can be represented as a dictionary inside the function.

[2] Good: allow for a more flexible API, new parameters can be added in the future without altering the signature of functions that use them; make extending classes and methods (especially in the context of library code) easier without needing to modify existing method signatures.

[3] Bad: it can become less clear what parameters a function accepts, which can make the API harder to understand for new users; Since type and existence checks on these arguments happen at runtime, it's easier to make mistakes that won't be caught until the code is executed.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text.
   Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

[1] In the Session class, some arguments are set to None by default, implying that these are optional parameters and if not provided, they take the None value. On the other hand, arguments without any default values are typically required arguments and must be provided by the caller.

[2] Yes, arguments can have any default value. It doesn't have to be None. For example, in the request method, the allow_redirects argument has a default value of True.

[3] Setting default values can make the function easier to use in the most common scenarios, as users don't need to specify values for every argument. Also, in evolving libraries, adding new arguments with default values ensures that existing code doesn't break. Users can continue using the function without providing the new argument, and the default value will be used.
