import collections

# breadth-first search graph algorithm solution - too slow for n>15,
# problem specification was n<=100
# O(2^n) time complexity according to this method from problem description

# Tried this method upon not implementing the depth-first search correctly
# at first, to get a working, "naive" solution (breadth-first is essentially
# brute-force)

# Have polished the implementation since first trying it out, so it is accurate
# but the slowest...
def isValidMove(i, j, n):
    if(i<=n-1 and j<=n-1 and i>=j):
        return True
    else:
        return False

def num_of_paths_to_dest(n):
    if(n<1):
      return 0
    if(n==1 or n==2):
      return 1

    #will contain found, valid paths
    path_dict = {}
    #will contain found, partial paths (no repeats)
    path_partial_dict = {}
    #queue for creating paths
    path_array = collections.deque()
    path_array.append("E")

    l = 0
    while(path_array):
        l+=1
        first_item = path_array.popleft()
        i = first_item.count("E")
        j = first_item.count("N")
        if(i==j==(n-1)):
            if(first_item not in path_dict):
                path_dict[first_item] = True
        else:
            if(isValidMove(i+1, j, n)):
                if((first_item+"E") not in path_partial_dict):
                    path_partial_dict[first_item+"E"] = True
                    path_array.append(first_item+"E")
            if(isValidMove(i, j+1, n)):
                if((first_item+"N") not in path_partial_dict):
                    path_partial_dict[first_item+"N"] = True
                    path_array.append(first_item+"N")

    # prints the number of loop iterations
    print(l)
    return len(path_dict)

# prints the number of valid paths
print(num_of_paths_to_dest(15))
