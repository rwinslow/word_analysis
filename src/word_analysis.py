import os
import re
import sys


class word_analysis(object):

    """Conduct analysis on the word count in files contained in a directory

    :param str args[0]: Path to read directory
    :param str kwargs['words_file']: Location to output word count analysis
    :param str kwargs['median_file']: Location to output median analysis
    :returns: None
    """

    def __init__(self, *args, **kwargs):
        # Initialize output dictionary
        self.words = {}
        self.median = {}
        self.num_lines = 0

        # Set parameters based on initial arguments
        try:
            self.set_write_words(kwargs['words_file'])
        except:
            self.set_write_words(None)

        try:
            self.set_write_median(kwargs['median_file'])
        except:
            self.set_write_median(None)

        # Save read directory and read file contents
        try:
            self.set_read_dir(args[0])
            try:
                self.read_files(args[1])
            except IndexError:
                self.read_files()
        except IndexError:
            print('No read directory defined')

        return None

    def set_read_dir(self, read_dir):
        """Setter for instance read directory

        :param str read_dir: Path to read directory
        :returns: Read directory path
        :rtype: str
        """
        self.read_dir = read_dir
        return self.read_dir

    def set_write_words(self, words_file):
        """Setter for location of dictionary output file

        :param str words_file: Path to file to output dictionary
        :returns: Words file path
        :rtype: str
        """
        self.words_file = words_file
        return words_file

    def set_write_median(self, median_file):
        """Setter for location of running median output file

        :param str median_file: Path to file to output running median
        :returns: Running median file path
        :rtype: str
        """
        self.median_file = median_file
        return median_file

    def add_word(self, word):
        """Add word to instance dictionary 'words'

        :param str word: Word to insert into dictionary or increment
        :returns: Word added
        :rtype: str
        """
        word = word.lower().replace('-', '')
        word = word.replace('_', '')
        if word:
            try:
                self.words[word] += 1
            except KeyError:
                self.words[word] = 1
        return word

    def add_median(self, word_count):
        """Add word count to instance list of medians 'median'

        :param int word_count: Number of words found in line
        :returns: Word count added to instance list of medians
        :rtype: int
        """
        try:
            self.median[str(word_count)] += 1
        except KeyError:
            self.median[str(word_count)] = 1
        return word_count

    def read_files(self):
        """Read all files within the read directory

        Open documents and scan through line-by-line without putting the entire
        file into memory.

        Uses a regular expression to identify all line segments composed of
        alphanumeric characters then places them into output dictionary.

        Sorts files alphabetically first before processing.

        :returns: Confirms successful execution
        :rtype: bool
        """
        file_list = []

        # Walk through directory tree and alphabetize within each directory
        for root, directories, files in os.walk(self.read_dir):
            files = [f for f in files if not f[0] == '.']
            files = sorted(files)
            file_list.extend([os.path.join(root, f) for f in files])

        # Open the median file for writing if one is specified
        if self.median_file:
            mf = open(self.median_file, 'w')

        # Loop through all files in directory and analyze
        for f in file_list:
            print('Reading: ' + f)
            try:
                with open(f) as lines:
                    for line in lines:
                        read_words = re.findall('([\w\-]+)', line)

                        # Add words in line to dictionary for counting
                        for word in read_words:
                            self.add_word(word)

                        # Add number of words in line to median array
                        num_words = len(read_words)
                        self.num_lines += 1
                        self.add_median(num_words)

                        if self.median_file:
                            self.output_current_median(file_handle=mf)
                        else:
                            self.output_current_median()
            except:
                e = sys.exc_info()[0]
                print('There was a problem reading the file: ' + str(f))
                print('Error: ' + str(e))
                raise

        # Close median file for writing
        if self.median_file:
            mf.close()

        return True

    def output_word_counts(self):
        """Sort keys in word dictionary and output

        Utilizes Python's built-in sorting function that uses the Timsort
        algorithm, which is derived from merge sort and insertion sort. Worst
        case performance is O(n log n) with a best case scenario of O(n).

        :returns: Confirms successful execution
        :rtype: bool
        """

        # Open words file for writing dictionary output
        if self.words_file:
            wf = open(self.words_file, 'w')

        # Run through each word in dictionary and output
        for k in sorted(self.words):
            tab_string = "\t\t"
            if len(k) > 7:
                tab_string = "\t"
            output_string = k + tab_string + str(self.words[k])

            if self.words_file:
                wf.write(output_string + "\n")
            else:
                print(output_string)

        # Close words file for writing
        if self.words_file:
            wf.close()

        return True

    def output_current_median(self, file_handle=None):
        """Calculate and output formatted median

        :returns: Confirms successful execution
        :rtype: bool
        """
        current_median = self.calculate_current_median()
        if file_handle:
            file_handle.write('{0:.1f}'.format(current_median) + "\n")
        else:
            print('{0:.1f}'.format(current_median))
        return True

    def calculate_current_median(self):
        """Calculates the current median and output

        The number of lines with each word length are already binned in the
        instance dictionary 'median' where the key represents the number of
        words in the line and the value represents how many lines had that
        number of words.

        Knowing how many lines were processed, it is possible to find the index
        of the corresponding median. After sorting the keys of 'median', the
        values are summed until the total equals or surpasses the corresponding
        index. The key is then identified as the median value (or values if an
        average must be computed).

        :returns: Median value
        :rtype: float
        """
        total = 0
        value_high = value_low = 0

        keys = [int(k) for k in self.median.keys()]
        keys = [k for k in sorted(keys)]

        if not self.num_lines % 2:
            index_high = (self.num_lines / 2) + 1
            index_low = index_high - 1

            for key in keys:
                if value_low:
                    value_high = key
                    break
                else:
                    total += self.median[str(key)]

                # Only need to determine if the sum total of indexes is equal
                # to the low index or greater than or equal to the high index.
                if total >= index_high:
                    value_high = value_low = key
                    break
                elif total == index_low:
                    value_low = key

            median_value = (value_high + value_low) / 2
        else:
            index = self.num_lines / 2 + 0.5
            for key in keys:
                total += self.median[str(key)]
                if total >= index:
                    median_value = key
                    break

        return median_value


def run():
    try:
        input_directory = sys.argv[1]
    except:
        input_directory = None

    try:
        words_file = sys.argv[2]
    except:
        words_file = None

    try:
        median_file = sys.argv[3]
    except:
        median_file = None

    wa = word_analysis(
        input_directory, words_file=words_file, median_file=median_file)
    wa.output_word_counts()

if __name__ == '__main__':
    run()
