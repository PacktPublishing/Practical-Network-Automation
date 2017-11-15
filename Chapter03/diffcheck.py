import difflib

file1 = "precheck.txt"
file2 = "postcheck.txt"

diff = difflib.ndiff(open(file1).readlines(),open(file2).readlines())
print (''.join(diff),)
