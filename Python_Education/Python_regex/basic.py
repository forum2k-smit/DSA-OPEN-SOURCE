""" 
Regex or regular expression is a way to search string in a text, it is more powerful and flexible than other 
traditional seraching techniques.

"""

""" Uncomment to run codes """
# re = regex = regular expressions 
import re 

""" Use of basic regex search function : re.search(<what to search>, <where to search>) """
# result = re.search(r'viv', 'vivaan')
# print(result)
# Output :: <re.Match object; span=(0, 3), match='viv'>
""" Output of search will return the re.Match object, indexes where it is matching and the match """
# result = re.search(r'aan', 'vivaan')
# print(result)
# Output:: <re.Match object; span=(3, 6), match='aan'>

""" using dot charater """
""" One dot represent any charater and number of dots means that number of charaters """
# result = re.search(r'i..a', 'ViVaAn', re.IGNORECASE)
# print(result)
# Output:: <re.Match object; span=(1, 5), match='ivaa'>


""" Using charater classes to restrict searching for sepecified charater. """
# print(re.search(r'[Pp]ython','python'))
#  Output:: <re.Match object; span=(0, 6), match='python'>

""" Use the dash to set range of values """
# print(re.search(r'2[0-9]','123'))
# Output:: <re.Match object; span=(1, 3), match='23'>

""" Combine the ranges """
# print(re.search(r'23z[a-zA-Z0-9]','1123z099'))
# Output:: <re.Match object; span=(2, 6), match='23z0'>

""" If we want charaters that isnt in the string we can use [^] """
# print(re.search(r'[^a-zA-z ]','Charaters .'))
# Output::<re.Match object; span=(10, 11), match='.'>

""" To search for alternatives. """
# print(re.search(r'cat|dog','I like cats and dog'))
# Output::<re.Match object; span=(7, 10), match='cat'>

""" Use findall to find all matching charaters having '|' symbol """
# print(re.findall(r'c|d', 'I like both cat and dog'))
# Output::['c', 'd', 'd']

""" Use all charater * to find all occurrences of charaters """
# print(re.search(r'v.*a','vivaan'))
# output::<re.Match object; span=(0, 5), match='vivaa'>

# print(re.search(r'g[a-z]* ','goodbody .'))
# output::<re.Match object; span=(0, 9), match='goodbody '>

""" Use of + to find all occurances of charaters before it """
# print(re.search(r'o+l+','wool'))
# <re.Match object; span=(1, 4), match='ool'>

# print(re.search(r'o+[a-z]*l+','boil'))
# Output::<re.Match object; span=(1, 4), match='oil'>

# print(re.search(r'[a-z]*', 'vaan'))

""" Use of ? which finds either one of them present in string or not """
# print(re.search(r'v?aan', 'vi aan'))
# is v before aan if yes then vaan otherwise aan.
