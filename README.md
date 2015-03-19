Word Analysis
=============

Submission for Insight Data Engineering coding challenge.

File Read
---------

Using Python's built-in os module, the class navigates through a given directory to create an alphabetized list all of the non-hidden files. It also moves down the tree in the event that additional subdirectories are present.

Word Count
----------

To obtain the list of words and their associated counts as quickly as possible, the dictionary data structure was used. The key was defined as the word and the associated value is the number of times that word was found. As an example:

| Key | Value |
| --- | ----- |
| bottle | 5 |
| power | 2 |
| this | 12 |

