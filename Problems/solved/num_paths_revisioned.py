import collections

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

    #print(path_dict)
    print(l)
    return len(path_dict)

print(num_of_paths_to_dest(15))
