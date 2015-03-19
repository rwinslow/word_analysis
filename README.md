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

To determine the median at any point a that set of data, the two conditions were that the data be sorted (usually in ascending order if it's numeric as in this case) and that the number of values present in the data be known. Because the median is simply the middle value in a set of numbers, the index of that value is the length of the values divided by 2.

For an even set of numbers, two indexes are required in order to find the average between two middle values; the one found from the initial division and the next value. For example, the median of the following data is found by taking the average the two marked results. Because there are 10 numbers, 10/2 = 5. So the index of the first number is 5 and the second number is 6. An example for a set like this is shown below with a median of 2.5.

<table>
	<tr>
		<td>0</td><td>0</td><td>1</td><td>1</td><td>2</td><td>3</td><td>4</td><td>4</td><td>5</td><td>5</td>
	</tr>
	<tr>
		<td> </td><td> </td><td> </td><td> </td><td>X</td><td>X</td><td> </td><td> </td><td> </td><td> </td>
	</tr>
</table>

For an odd set of numbers, only one index needs to be found. After dividing the number of values by 2, 0.5 needs to be added to select the correct index. Therefore the index of the median is 9/2 + 0.5 = 5. An example with a median of 2 is shown below:

<table>
	<tr>
		<td>0</td><td>0</td><td>1</td><td>1</td><td>2</td><td>3</td><td>4</td><td>4</td><td>5</td>
	</tr>
	<tr>
		<td> </td><td> </td><td> </td><td> </td><td>X</td><td> </td><td> </td><td> </td><td> </td>
	</tr>
</table>

From these principles, the median from a dataset of any length can be found as long as we know the number of times an element exists and the data is organized.

Similar to the implementation of the Word Count algorithm, the Running Median also uses a dictionary. After the number of words in a given line becomes the key in the dictionary while the number of times that result were found becomes the value. As an example with the dataset with an even number of values above, the resulting dictionary would look like this:

| Value | Occurrences |
| --- | ----- |
| 0 | 2 |
| 1 | 2 |
| 2 | 1 |
| 3 | 1 |
| 4 | 2 |
| 5 | 2 |

All we need to do to find the median is sum the number of occurrences up until the total equals or exceeds the index or indexes we found above. Then we can read the corresponding value and we've found our median.
