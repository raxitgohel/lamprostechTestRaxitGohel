arr = [int(x) for x in input().split(' ')]  # Input Format numbers separated by white spaces
k = int(input()) # Get value of k
hmap = {} # Initialize a dictionary that will store frequency of elements

# Loop through array to populate dictionary
for ele in arr:
    hmap[ele] = hmap.get(ele, 0) + 1

# Sort the dictionary by its values i.e. frequency of elements in descending order
hmap_list = sorted(hmap, key=lambda x: hmap[x], reverse=True) 

print(hmap_list[:k]) # Print the top k most frequent elements