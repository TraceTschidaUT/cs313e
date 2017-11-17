#  File: sumMaze.py
#  Description: Solves a maze recursively 
#  Student's Name: Trace Tschida
#  Student's UT EID: TRT729
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 11/11/2017
#  Date Last Modified: 11/11/2017

import copy
class State():

    def __init__(self, grid, history, rowStart, colStart, rowEnd, colEnd, _targetSum, _sum, numRows, numCols):

        self.grid = grid
        self.history = history
        self.rowStart = rowStart
        self.colStart = colStart
        self.rowEnd = rowEnd
        self.colEnd = colEnd
        self.targetSum = _targetSum
        self.sum = _sum
        self.numRows = numRows
        self.numCols = numCols

    def __str__(self):

        string = "\nProblem is now:\n\tGrid:\n"

        for row in self.grid:
            string += "\t  "
            for element in row:
                if element == None:
                    element = "X"
                str_element = str(element)
                spaces = ""
                if len(str_element) == 1:
                    spaces = "   "
                elif len(str_element) == 2:
                    spaces = "  "
                else:
                    spaces = " "
                string += str_element + spaces
            string += "\n"

        string += "\n\thistory: " + str(self.history)
        string += "\n\tstart point: ({:},{:})".format(self.rowStart, self.colStart)
        string += "\n\tsum so far: {:}".format(self.sum)

        return string

def isValid(grid, num_rows, num_cols, start_row, start_col):

    # return false if:
    # moving outside grid boundary
    # of if already visited
    if start_row > num_rows or start_col > num_cols or grid[start_row][start_col] == None:
        return False
    
    #  else return true
    else:
        return True

def solve(state):
    
    # state = State instance
    
    # base case state is end state
    # target sum is reached and at the end point
    # at the end point
    # sum matches the target sum
    print("\nIs this a goal state?")
    if state.sum == state.targetSum and state.rowStart == state.rowEnd and state.colStart == state.colEnd:
        print("Yes! Solution found")
        return state.history

    # else check to see if sum is greater than target sum
    # return None
    elif state.sum > state.targetSum:
        print("No. Target exceeded:  abandoning path")
        return None
    
    # else -> the sum is still less than the target sum
    else:

        print("No. Can I move right?")
        # check if move right is valid
        if isValid(state.grid, state.numRows, state.numCols, state.rowStart, state.colStart + 1):

            print("Yes! Moving Right")
            print("Paused...")

            # create a new state instance
            newState = State(copy.deepcopy(state.grid), \
                copy.deepcopy(state.history), state.rowStart, \
                state.colStart + 1, state.rowEnd, state.colEnd, \
                state.targetSum, state.sum, state.numRows, state.numCols)
            
            # update the sum
            newState.sum += newState.grid[newState.rowStart][newState.colStart]

            # update the history
            newState.history.append(newState.grid[newState.rowStart][newState.colStart])
            
            # change the grid to show the move
            # leaves a bread crumb
            newState.grid[newState.rowStart][newState.colStart] = None

            # print the new state
            print(newState)

            # recursively call solve using new instance 
            result = solve(newState)
            if result != None:
                # gets out of the stack
                return result

        # if up is valid
        print("No. Can I move up?")
        if isValid(state.grid, state.numRows, state.numCols, state.rowStart - 1, state.colStart):

            print("Yes! Moving up")
            print("Paused...")

            # create a new start instance
            newState = State(copy.deepcopy(state.grid), copy.deepcopy(state.history), state.rowStart - 1, \
                state.colStart, state.rowEnd, state.colEnd, \
                state.targetSum, state.sum, state.numRows, state.numCols)

            # update the sum
            newState.sum += newState.grid[newState.rowStart][newState.colStart]

            # update the history
            newState.history.append(newState.grid[newState.rowStart][newState.colStart])

            # change the grid to show the move
            # leaves a bread crumb
            newState.grid[newState.rowStart][newState.colStart] = None

            # print the new state
            print(newState)

            # recursively call solve using new instance 
            result = solve(newState)
            if result != None:
                return result            


        # if down is valid
        print("No. Can I move down?")
        if isValid(state.grid, state.numRows, state.numCols, state.rowStart + 1, state.colStart):

            print("Yes. Moving down")
            print("Paused...")

            # create a new start instance
            newState = State(copy.deepcopy(state.grid), copy.deepcopy(state.history), state.rowStart + 1, \
                state.colStart, state.rowEnd, state.colEnd, \
                state.targetSum, state.sum, state.numRows, state.numCols)

            # update the sum
            newState.sum += newState.grid[newState.rowStart][newState.colStart]

            # update the history
            newState.history.append(newState.grid[newState.rowStart][newState.colStart])

            # change the grid to show the move
            # leaves a bread crumb
            newState.grid[newState.rowStart][newState.colStart] = None

            # print the new state
            print(newState)

            # recursively call solve using new instance 
            result = solve(newState)
            if result != None:
                return result

        # if left is valid
        print("No. Can I move left?")
        if isValid(state.grid, state.numRows, state.numCols, state.rowStart, state.colStart - 1):

            print("Yes! Moving left")
            print("Paused...")

            # create a new start instance
            newState = State(copy.deepcopy(state.grid), copy.deepcopy(state.history), \
                state.rowStart, state.colStart - 1, state.rowEnd, \
                state.colEnd, state.targetSum, state.sum, \
                state.numRows, state.numCols)

            # update the sum
            newState.sum += newState.grid[newState.rowStart][newState.colStart]

            # update the history
            newState.history.append(newState.grid[newState.rowStart][newState.colStart])

            # change the grid to show the move
            # leaves a bread crumb
            newState.grid[newState.rowStart][newState.colStart] = None

            # print the new state
            print(newState)

            # recursively call solve using new instance 
            result = solve(newState)
            if result != None:
                return result

        # else -> no moves left, return None
        # other base case
        print("No path works. Backtracking...")
        return None

def main():

    # maze data
    maze_data = []
    row_num = 0

    # create a grid with lists
    grid = []

    # open the maze date file
    with open("mazedata.txt") as file:
        
        # read the contents of the file line by line
        for line in file:

            # clean the line
            line = line.strip()

            # create a grid row
            grid_row = line.split(" ")

            # convert each string to an int
            for i in range(len(grid_row)):
                grid_row[i] = int(grid_row[i])

            if row_num == 0:
                maze_data = grid_row
                row_num += 1
            else:
                grid.append(grid_row)
    
    # create a new state with initial informaiton
    # unpack the maze data
    targetValue = int(maze_data[0])
    grid_rows = int(maze_data[1]) - 1
    grid_cols = int(maze_data[2]) - 1
    start_row = int(maze_data[3])
    start_col = int(maze_data[4])
    end_row = int(maze_data[5])
    end_col = int(maze_data[6])

    # print the original problem
    print("Target value: {:}".format(targetValue))
    print("Number of rows: {:}".format(grid_rows))
    print("Number of columns: {:}".format(grid_cols))
    print("Start point: ({:},{:})".format(start_row, start_col))
    print("End point: ({:},{:})".format(end_row, end_col))
    print("Starting point:")

    # create the first state
    # create a new state
    state = State(grid, [], start_row, \
    start_col, end_row, end_col, targetValue, 0,\
    grid_rows, grid_cols)

    print(state)

    print("\nStarting maze:")

    # first steps
    current_sum = grid[start_row][start_col]
    history = [grid[start_row][start_col]]
    grid[start_row][start_col] = None

    # create a new state
    state = State(grid, history, start_row, \
    start_col, end_row, end_col, targetValue, current_sum,\
    grid_rows, grid_cols)

    print(state)

    result = solve(state) # this will be None or the goals state's history

    print()
    if result == None:
        print("No solution exists")
    else:
        print("The solution is: {:}".format(result))

main()