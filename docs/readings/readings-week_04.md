# Readings: Week 04

This week we focus on functions and conditional statements. A function is a _named_ series of statements (a code block) that performs a computation whenever the function is invoked by a caller. Parameters can be declared in a function definition in order to permit the processing of input values (i.e., arguments). Functions typically, though not always, compute a result to be returned to the caller.

You will also begin writing conditional statements. You will learn how to employ `if-elif-else` logic to evaluate expressions that determine the execution path that your code will follow.

The expressions you write will employ a variety of operators. Python operators are organized into groups. We've touched on arithmetic operators and assignment operators. Starting this week you will begin using other operators when writing conditional statements, especially comparison, logical, identity, and membership operators.

The readings also include an article on string formatting, a topic introduced last week, as well as an important article discussing exceptions and tracebacks. The traceback is an error report the Python Interpreter sends to the terminal whenever your code raises an exception.

:warning: To access readings on the O'Reilly Learning Platform you need a "school" account.  See [instructions](./readings-oreilly_learning_platform.md) on how to create and activate your account.

## Functions

**Charles Severance, [Python for Everybody. Exploring data in Python 3](https://www.py4e.com/book) (CreateSpace, 2016).**

:bulb: Entry point for the beginner.

Read Chapter 4 “Functions”.

Chuck discusses a few of the Python Standard Library's "built-in" functions and then turns his attention to custom functions that you can write using the `def` keyword. After reading Chuck proceed to Eric's chapter and Lisa's article.

**Eric Matthes, [Python Crash Course](https://learning.oreilly.com/library/view/python-crash-course/9781492071266/), 2nd Edition (No Starch Press, 2019).**

Read Chapter 8 ["Functions"](https://learning.oreilly.com/library/view/python-crash-course/9781492071266/xhtml/ch08.xhtml#ch08), limiting your reading to the following sections and sub-sections _only_:

* Defining a Functions
  * Passing Information to a Function
  * Arguments and Parameters
* Passing Arguments
  * Positional Arguments
  * Keyword Arguments
  * Default Values
  * Equivalent Function Calls
  * Avoiding Argument Errors
* Return Values
  * Returning a Simple Value
  * Making an Argument Optional

**Lisa Tagliaferri, ["How to Define Functions in Python 3"](https://www.digitalocean.com/community/tutorials/how-to-define-functions-in-python-3) (Digital Ocean, June 2016).**

Lisa is quick out of the starting block in her discussion of functions. It's a faster read than Eric's chapter. In particular, have a look at her section titled "Using main() as a Function". She discusses the purpose of the `main()` function and why including it in the programs you write provides you with greater control over code execution while also enhancing modularity and readability.

## Functions Cheat Sheet

Eric Matthes, ["Beginner’s Python Cheat Sheet - Functions"](https://github.com/ehmatthes/pcc_2e/blob/master/cheat_sheets/beginners_python_cheat_sheet_pcc_functions.pdf)

## Conditional Statements

**Charles Severance, [Python for Everybody. Exploring data in Python 3](https://www.py4e.com/book) (CreateSpace, 2016).**

:bulb: Entry point for the beginner.

Read Chapter 3, "Conditional Execution".

Chuck discusses boolean expressions, logical operators, conditional execution, chained/nested conditionals, and try/except blocks.  Start here and then read Lisa Tagliaferri's article and/or Eric Matthes chapter.

**Lisa Tagliaferri, ["How to Write Conditional Statements in Python 3"](https://www.digitalocean.com/community/tutorials/how-to-write-conditional-statements-in-python-3-2) (Digital Ocean, June 2016).**

Lisa provides a useful introduction on how to craft `if-elif-else` conditional statements.

**Lisa Tagliaferri, ["Understanding Boolean Logic in Python 3"](https://www.digitalocean.com/community/tutorials/understanding-boolean-logic-in-python-3)**

Lisa discusses booleans, comparison operators, logical operators, truth values, and using expressions that return `True` or `False` for control flow, introduced in the last lecture.

__or__

**Eric Matthes, [Python Crash Course](https://learning.oreilly.com/library/view/python-crash-course/9781492071266/), 2nd Edition (No Starch Press, 2019).**

Read chapter 5 [“If statements”](https://learning.oreilly.com/library/view/python-crash-course/9781492071266/xhtml/ch05.xhtml#ch05).

Eric discusses conditional tests, `if` statements, using `if` statements with lists. Note that there are a couple of examples involving lists that refer to a `for` loop.  We cover loops next week.

## Conditional Statements Cheat Sheet

Eric Matthes, ["Beginner’s Python Cheat Sheet - If Statements and While Loops"](https://github.com/ehmatthes/pcc_2e/blob/master/cheat_sheets/beginners_python_cheat_sheet_pcc_if_while.pdf).

## Operators

**w3schools, ["Python Operators"](https://www.w3schools.com/python/python_operators.asp).**

Handy reference. Start getting to know the following operator groups:

* Arithmetic operators
* Assignment operators
* Comparison operators
* Logical operators (`and`, `or`, `not`)
* Identity operators (`is`, `is not`)
* Membership operators (`in`, `not in`)
* Bitwise operators (out of scope for SI 506)

**John Sturtz, ["Operators and Expressions in Python"](https://realpython.com/python-operators-expressions/) (Real Python, nd).**

An overview of how to employ the various operators available to you when crafting expressions and statements.

## Exceptions

**Chad Hansen, ["Understanding the Python Traceback"](https://realpython.com/python-traceback/) (RealPython, 2019).**

Chad discusses the "traceback", an error report issued by the Python Interpreter whenever the code you write triggers an exception. I will reference this article frequently in the weekly readings. For this week read the following sections:

* What is a Python Traceback?
* How do you Read a Python Trackback?
* What are some Common Tracebacks in Python?
* (following exceptions _only_)
  * AttributeError
  * IndentionError
  * NameError
  * SyntaxError
  * TypeError

## String Formatting

**Joanna Jablonski, ["Python 3's f-Strings: An Improved String Formatting Syntax (Guide)"](https://realpython.com/python-f-strings/) (RealPython, nd).**

Last week I highlighted three ways to format strings. Johanna's article provides a written summary, emphasisizing in particular the new formatted string literal approach, a.k.a "f-strings".

## Canvas Files

:exclamation: C. Severance, [Python for Everybody](https://www.py4e.com/book) EPUB and PDF versions are available in Canvas Files. Chuck's book has been translated into several languages and is available in various formats (i.e., HTML, PDF, EPUB, Mobi) at [https://www.py4e.com/book](https://www.py4e.com/book). All Tagliaferri articles are republished in L. Tagliaferri, [How to Code in Python 3](https://www.digitalocean.com/community/books/digitalocean-ebook-how-to-code-in-python) (Digital Ocean, Feb 2018). [PDF](https://do.co/python-book-pdf) and [EPUB](https://do.co/python-book-epub) versions are also available in Canvas Files.

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
