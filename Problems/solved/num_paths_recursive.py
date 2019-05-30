import sys

sys.setrecursionlimit(1000)


# depth-first search graph algorithm solution - too slow for n>15,
# problem specification was n<=100
# O(2^n) time complexity according to this method from problem description

# faster than breadth-first search, first algorithm I thought of and tried,
# since the potential paths are technically a directed acyclical graph,
# and this algorithm fits that data structure well (my Algorithms book agrees!)

# Have polished the implementation since first trying it out, so it is accurate
# but slow...
def isValidMove(i, j, n):
    if(i<=n-1 and j<=n-1 and i>=j):
        return True
    else:
        return False


def num_of_paths_to_dest(n, start_i=0, start_j=0, first_path="", path_array={}):
  if(n<1):
    return 0
  if(n==1 or n==2):
    return 1
  if(n==3):
    return 2

  if(len(path_array)!=0 and start_i==0 and start_j==0):
    return len(path_array)

  if(len(path_array)==0):
    first_path = "E"
    first_path += "NE"*(2*n-6)
    first_path += "N"
    path_dict = {}
    path_dict[first_path] = True
    i, j = n-1, n-1
  else:
    path_dict = path_array

  ways_left = first_path[0:len(first_path)-1]
  last_move = first_path[-1]
  back_path = ways_left
  i, j = ways_left.count("E"), ways_left.count("N")

  #need to traverse the graph better here - missing points!

  paths = []
  if(isValidMove(i+1, j, n) and last_move!="E"):
      paths.append(back_path+"E")
  if(isValidMove(i, j+1, n) and last_move!="N"):
    paths.append(back_path+"N")
    if(i==(j+1)==n-1):
        path_dict[current_path+"N"] = True

  paths_visited = {}

  # shows valid, untraversed paths' "base" - like the "root" of a word
  # shorter/smaller "base" takes longer, more possible valid paths to the
  # endpoint
  print(paths)
  while(paths):
      current_path = paths.pop()
      i = current_path.count("E")
      j = current_path.count("N")
      if(isValidMove(i+1, j, n)):
        paths.append(current_path+"E")
      if(isValidMove(i, j+1, n)):
        if(i==(j+1)==n-1):
            path_dict[current_path+"N"] = True
        else:
            paths.append(current_path+"N")

  return num_of_paths_to_dest(n, start_i=back_path.count("E"), start_j=back_path.count("N"), first_path=back_path, path_array= path_dict)

# prints the number of valid paths
print(num_of_paths_to_dest(15))
