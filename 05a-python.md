# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> The similarity is that they are both sequence of objects and they maintain order. The big difference is that Tuples are immuatable while Lists are mutable. Lists will work as values in dictionaries but not as keys. Keys must be immutable, therefore, tuples are used as keys inside a dictionary. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and Sets are both sequence of objects. List keeps the order and can have repeated values, whereas sets will ignore repeated values and just keep one instance of it. Sets require values to be hashable and therefore are quicker. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is another way to create a function. 
>>   There are certain situations where using lambda can make the code a bit shorter. 
   For example: tuples1 = [('st1', 'A', 15, 49),('st2', 'B', 12, 32),('st3', 'B', 10, 56)]
   x = sorted(tuples1, key=lambda tuple: tuple[3])
   print(x)
   In this case, we can use the lambda function along with sort to sort tuple by the third element. 


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a way to express lists in a similar fashion as done in mathematics, without any special syntax. They are also a good tool for transforming one list into another with some conditional statements. 
Here is a comparison between map and filter vs. list comprehenstion, both of which produce the same output. 
numbers = range(1,50,1)
map_filter= map(lambda n: n * 2, filter(lambda n: n % 2 == 1, numbers))
list_comprehension = [n * 2 for n in numbers if n % 2 == 1]
Set comprehensions and dictionary comprehensions work just like list comprehesnsions. Following are examples of set comprehension and dictionary comprehension, respectively. 
x = {i**2 for i in range(10)}
x = {i:i**2 for i in range(10)}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





