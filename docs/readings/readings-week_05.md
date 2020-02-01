# Readings: Week 05

This week we focus on list iteration (i.e., process repetition), looping, and slicing. I've also included an article that discusses execution modes in Python with special emphasis on the `main()` function.

You will learn how to use the `while` statement and manage the number of iterations to perform given some condition with the `continue` and `break` statements. You will also learn how to "loop over" sequences such as lists by employing a `for` loop. In the case of a list, the `for` loop allows you to iterate over the list elements and perform one or more operations on each element. You can also include filtering logic within a `for` loop body in order to constrain or otherwise restrict the tasks you wish to perform to a subset of the list elements encountered.

It is also important to learn how to utilize Python's slicing notation. The list slicing syntax simplifies referencing and/or extracting a subset of list elements. List slicing can result in list traversal performance gains since slicing obviates the need to loop over an entire list in order in order to operate on a targeted subset of elements.

## Iteration

**Charles Severance, [Python for Everybody. Exploring data in Python 3](https://www.py4e.com/book) (CreateSpace, 2016).**

:bulb: Entry point for the beginner.

Read Chapter 5 "Iteration".

Chuck discusses the `while` statement, the control flow statements `break` and `continue`, and the `for` loop.

## Looping

:exclamation: Read the Matthes chapters. Then scan the Tagliaferri articles for additional reinforcement.

**Eric Matthes, [Python Crash Course](https://learning.oreilly.com/library/view/python-crash-course/9781492071266/), 2nd Edition (No Starch Press, 2019).**

Read Chapter 4 ["Working with Lists"](https://learning.oreilly.com/library/view/python-crash-course/9781492071266/xhtml/ch04.xhtml#ch04)

Eric covers looping over a list, the `range()` function, list comprehensions, and slicing. You can skip the comprehensions, tuples and styling sections of the chapter. We cover those topics later.

Read Chapter 7 ["User Input and While Loops"](https://learning.oreilly.com/library/view/python-crash-course/9781492071266/xhtml/ch07.xhtml#ch07)

Eric discusses the built-in function `input()`, the modulo operator, `while` loops, `break` and `continue` statements, and using `while` loops with lists and dictionaries (you can ignore dictionaries for the moment).

**Lisa Tagliaferri, [“How to Construct For Loops in Python 3”](https://www.digitalocean.com/community/tutorials/how-to-construct-for-loops-in-python-3) (Digital Ocean, Sept 2016).**

Lisa's articles provides the right amount of detail in an otherwise compact presentation format.

**Lisa Tagliaferri, ["How to Use Break, Continue, and Pass Statements when Working with Loops in Python 3"](https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3) (Digital Ocean, Jan 2017).**

Read Lisa to deepen your understanding of control flow and how to use `break`, `continue`, and `pass` in your `for` loops.

## List Indexing and Slicing

**Sergii Boiko, ["Python for Machine Learning: Indexing and Slicing for Lists, Tuples, Strings, and other Sequential Types"](https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/) (3 Oct 2018).**

Despite the title, the article limits its examples to list indexing and slicing only. Review the section on indexing, both positive and negative (a subject introduced in week 03 readings). Then read carefully Sergii's "Slice Notation" section. The examples he provides are particular helpful when learning how to slice a list using Python's slicing notation.

## Python Execution Modes and the main() Function

 Bryan Weber, ["Defining Main Functions in Python"](https://realpython.com/python-main-function/) (Real Python, May 2019).

 Bryan discusses the `main()` function, the relevance of `main()` to execution modes in Python, and `main()` function best practices. This article could prove challenging for the novice programmer. Don't worry; we will explore the rationale for writing programs that feature a `main()` function in class.

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.