Word Analysis
=============

Submission for Insight Data Engineering coding challenge.

File Read
---------

Using Python's built-in os module, the class navigates through a given directory to create an alphabetized list all of the non-hidden files. It also moves down the tree in the event that additional subdirectories are present.

Word Count
----------

To obtain the list of words and their associated counts as quickly as possible, the dictionary data structure was used. The key was defined as the word and the associated value is the number of times that word was found. As an example, the word 'bottle' was found 5 times, the word 'power' was found 2 times, and the word 'this' was found 12 times in a given passage. The resulting dictionary is shown below:

| Key | Value |
| --- | ----- |
| bottle | 5 |
| power | 2 |
| this | 12 |

It is highly unlikely that the data will be sorted upon entry into the dictionary, but sorting must only occur once on output. The algorithm uses the built-in sorting function sorted() that uses the Timsort algorithm. It was derived from merge sort and insertion sort and had worst
case performance of O(n log n) and best case performance of O(n). Already very quick!

Running Median
--------------

Similar to the implementation of the Word Count algorithm, the Running Median also uses a dictionary. After the number of words in a given line becomes the key in the dictionary while the number of times that result were found becomes the value. As an example, for a given set of data with 86 lines, 5 words comprised 25 of the lines, 7 words comprised 42 of the lines, and 10 words comprised the remaining 19 lines. The resulting dictionary is shown below:

| Key | Value |
| --- | ----- |
| 5 | 25 |
| 7 | 42 |
| 10 | 19 |

To determine the median at any point a that set of data, the two conditions were that the data be sorted (usually in ascending order if it's numeric as in this case) and that the number of values present in the data be known. Because the median is simply the middle value in a set of numbers, the index of that value is the length of the values divided by 2.

For an even set of numbers, two indexes are required in order to find the average between two middle values; the one found from the initial division and the next value. For example, the median of the following data is found by taking the average the two marked results.

|0|0|1|1|2|3|4|4|4|4|5|5|
|-|-|-|-|-|-|-|-|-|-|-|-|
| | | | |X|X| | | | | | |


