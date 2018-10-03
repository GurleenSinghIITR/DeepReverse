#This code is to reverse the list and the list present within it.

def deep_reverse(L):
  L.reverse()			# We reverse the List
  for l in L:			# We iterate through the List
    l.reverse()		# We reverse each item which is a list too
  return L 			# We return it
print(deep_reverse([[1, 2], [3, 4], [5, 6, 7]]))
