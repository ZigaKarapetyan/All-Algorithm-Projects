
def find_match(text, pattern):
 d=len(text)
 k=len(pattern)
 for i in range(d-k+1):
  j=0
  while j<k and text[i+j] == pattern[j]:
   j+=1
  if j==k:
   print("pattern found", i) 
   return i
 return -1 

text = "CDDA DCDD AAA CCD AADD DD AA"
pattern = "ADD"
find_match(text, pattern)