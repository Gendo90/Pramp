# input: n - a positive integer representing the grid size.
# output: number of valid paths from (0,0) to (n-1,n-1).

function numOfPathsToDest(n):
    if (n == 1):
        return 1

    lastRow = []
    for i from 1 to n-1:
        lastRow[i] = 1 # base case - the first row is all ones

    currentRow = []

    for j from 1 to n-1:
        for i from j to n-1:
            if (i == j):
                # case along the diagonal
                currentRow[i] = lastRow[i]
            else:
                # currentRow[i-1] represents the # of paths to the space
                # immediately west, and lastRow[i] represents # of paths to
                # the space immediately south
                currentRow[i] = currentRow[i-1] + lastRow[i]
        # replaces the last row with the current row, then moves up a row
        # as the for loop iterates
        lastRow = currentRow

    return currentRow[n-1]
