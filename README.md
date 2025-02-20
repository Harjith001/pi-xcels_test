# pi-xcels_test

## Finding first repeated item in a given list 
## Aproach 
### Brute Force 
In this method, for each item on the list is compared to other elements to find the first repetition of it. If this number is less than the current answer then it is updated 

for i in range(len(arr):
  for j in range(len(arr)):
     ....
Time complexity = O(n^2)

### Optimized Aproach 
In this methode, a hash map is used to store the first occurence of each item. If the item is encountered again then this will be the answer. 

Time complexity = O(n)
