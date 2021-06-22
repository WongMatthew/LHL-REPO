# Lecture Notes w/ Socorro Dominguez

## Python Basics
==========================

* What is Python?
    * Dynamically typed
    * expressive
        * can make it shape into different languages
        * python works w/ C
    * Free and open source
        * anyone can use it, everyone shares code
    * Interpreted
    * High-level
    * portable
    * object oriented
    * GUI programming
    * dynamically typed
    * interpreted
    * embeddable
    * extensible

* Why python for data sci?
    * simple programming language
    * python has an active community w/ a vast selection of libraries and resources
    * professionals in data sci dont want to be bogged down w/ complicating programmign requirements
        * would use languages like python/ruby to perform tasks 

* Jupyter
    * Provides python environment
    * Working w/ notebooks
        * **Code Cells**
        * **Markdown Cells**
        * Defaults to code cells 

* Libraries in the python ecosystem
    * pandas
    * jupyter
    * NumPy
    * Matplotlib
    * Cython

* Built in data types - values & objects
    * working w/ values
    * int
    * float
    * str
        * string "verbs"
            * diff methods to extract info from string
            * example: 
            ```python
            string = Joe
            len(string)
            # 3
            string.lower()
            # joe
            ```
    * bool
    * list
    * sets
    * tuples
    * dict

* Numerical data types & casting
    * numerical data type --> int
    * casting 
        * int to str --> str(lenght)
        * float to str --> str(x)


* Lists
    * sequence of elements w/ a particular order
    * identified by their square brackets
    * can use .split() to slice a list
    * slicing
        * can slice with []; the start is inclusive and the end is exclusive
        * string_list[1:3] will get elements 1, 2
        * gets the 2nd and 3rd elements in the list

    * list comprehension
        * we can manipulate a hwole list using list comprehension
        ``` python
        new_list = [0,3,4,5,6,7,8,3,3,7,9,5]
        other_new_list = []
        for i in new_list:
            x = i+5
            other_new_list.append(x)
        print(other_new_list)
        # other_new_list = [0,3,4,5,6,7,8,3,3,7,9,5]
        ```
    
* Tuples
    * data structures v similar to lists but with two main differences
    * represented w/ parentheses instead of square brackets
    * immutable
    * Note: cannot be sliced

* Sets
    * unordered
    * values are unique - no duplicates
    * uses curly brackets

* Dictionaries
    * Dictionaries are unordered pairs of keys and corresponding values

    ``` python
    acc = {'name': 'jack', 'acc type': 'checking', 'branch': 'vancouver','age': 32}
    acc['name']
    # jack
    acc['age']
    # 32
    acc.keys() # can be casted into a list
    list(acc.keys())
    # ['name', 'acc type', 'branch', 'age']
    acc.values()
    acc.items()
    ```

    * dictionaires can have labels or keys associated with a value where as a list only has an index
        * in a list, order matters
        * in a dictionary, order doesnt matter

* Handling date and time in python
    ```
    from datetime import datetime
    ```


