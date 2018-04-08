import re
patterns = ["term1","term2"]
text = "This is a string with term1, not not the other!"
for pattern in patterns:
    print("I'm searching for: "+pattern)
    if re.search(pattern,text):
        print("Match!")
    else:
        print("No match.")

match = re.search('term1',text)
print(match.start())

#split strings
split_symbol = '@'
email = "user@gmail.com"
print(re.split(split_symbol,email))

#find all
print(re.findall('match','test phrase match in match middle'))

#
def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = "sdsd..sssddd..sdddsddd...dsds...dsssssss...sddddd"
test_patterns = ['sd*','sd+s','sd{2}','s[sd]+']
#exclusion
test_patterns2 = ['[^.d]']
#lower case characters: [a-b]
#upper case letters: [A-Z]
#numbers: []
#[r'\d+']
#\d digits, \D non-digits(?), \s spaces \S non-white spaces
multi_re_find(test_patterns,test_phrase)
multi_re_find(test_patterns2,test_phrase)
