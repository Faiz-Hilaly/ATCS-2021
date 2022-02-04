"""
An AI that uses Finite State Machines to solve a maze

@author: Ms. Namasivayam (TODO: replace with your name)
@version: 2022
"""
from fsm import FSM

class MazeBot:
    def __init__(self, maze_file):
        # The location of the bot
        self.x = None
        self.y = None

        # The map of the maze
        self.maze = None

        # The route the bot will take to get to the $
        self.path = None

        # Create an initialize the maze
        self.reset(maze_file)

        # TODO: Create the Bot's finite state machine (self.fsm) with initial state
        self.brain = FSM("SN")
        self.add_state_transitions()

    def add_state_transitions(self):
        """
        Adds all the state transitions to the fsm
        """
        self.brain.add_transition("#", "NB", None, "WB")
        self.brain.add_transition("#", "WB", None, "SB")
        self.brain.add_transition("#", "SB", None, "EB")
        self.brain.add_transition("#", "EB", None, "NB")
        self.brain.add_transition("#", "NN", None, "WN")
        self.brain.add_transition("#", "WN", None, "SN")
        self.brain.add_transition("#", "SN", None, "EN")
        self.brain.add_transition("#", "EN", None, "NN")
       
        self.brain.add_transition("$", "NB", self.move_north, "M")
        self.brain.add_transition("$", "WB", self.move_west, "M")
        self.brain.add_transition("$", "SB", self.move_south, "M")
        self.brain.add_transition("$", "EB", self.move_east, "M")
        self.brain.add_transition("$", "NN", self.move_north, "M")
        self.brain.add_transition("$", "WN", self.move_west, "M")
        self.brain.add_transition("$", "SN", self.move_south, "M")
        self.brain.add_transition("$", "EN", self.move_east, "M")

        self.brain.add_transition(" ", "NB", self.move_north, "NB")
        self.brain.add_transition(" ", "WB", self.move_west, "WB")
        self.brain.add_transition(" ", "SB", self.move_south, "SB")
        self.brain.add_transition(" ", "EB", self.move_east, "EB")
        self.brain.add_transition(" ", "NN", self.move_north, "NN")
        self.brain.add_transition(" ", "WN", self.move_west, "WN")
        self.brain.add_transition(" ", "SN", self.move_south, "SN")
        self.brain.add_transition(" ", "EN", self.move_east, "EN")

        self.brain.add_transition("B", "NN", self.move_north, "NB")
        self.brain.add_transition("B", "WN", self.move_west, "WB")
        self.brain.add_transition("B", "SN", self.move_south, "SB")
        self.brain.add_transition("B", "EN", self.move_east, "EB")
        self.brain.add_transition("B", "NB", self.move_north, "NN")
        self.brain.add_transition("B", "WB", self.move_west, "WN")
        self.brain.add_transition("B", "SB", self.move_south, "SN")
        self.brain.add_transition("B", "EB", self.move_east, "EN")

        self.brain.add_transition("X", "NB", self.move_north, "NB")
        self.brain.add_transition("X", "WB", self.move_west, "WB")
        self.brain.add_transition("X", "SB", self.move_south, "SB")
        self.brain.add_transition("X", "EB", self.move_east, "EB")
        self.brain.add_transition("X", "NN", None, "WN")
        self.brain.add_transition("X", "WN", None, "SN")
        self.brain.add_transition("X", "SN", None, "EN")
        self.brain.add_transition("X", "EN", None, "NN")

        self.brain.add_transition("#", "M", None, "M")
        self.brain.add_transition("$", "M", None, "M")
        self.brain.add_transition(" ", "M", None, "M")
        self.brain.add_transition("B", "M", None, "M")
        self.brain.add_transition("X", "M", None, "M")

    def reset(self, filename):
        """
        Resets the maze bot to have an empty path and sets the maze
        from the given filename. The bot starts at position 1, 1
        :param filename: The name of the file to read the maze in from
        """
        # The bot always starts at the Northwest corner of the maze
        self.x = 1
        self.y = 1

        # The path resets to empty
        self.path = []

        # Read in the maze from the file
        self.maze = []
        with open(filename) as f:
            line = f.readline().strip()
            self.maze.append(line)
            while line:
                line = f.readline().strip()
                self.maze.append(line)

    def move_south(self):
        self.y = self.y+1
        self.path.append("south")

    def move_east(self):
        self.x = self.x+1
        self.path.append("east")

    def move_north(self):
        self.y = self.y-1
        self.path.append("north")

    def move_west(self):
        self.x = self.x-1
        self.path.append("west")

    def get_next_space(self):
        """
        Using the current state of the bot, returns the next space in the maze
            Ex. If the current state has the bot moving south, the next space in the
            maze would be self.maze[self.y+1][self.x]
        :return: The next spot in the maze Ex. "B", "#", " ", "X"
        """

        curr = self.brain.current_state

        if curr == "SB": return self.maze[self.y+1][self.x]
        if curr == "NB": return self.maze[self.y-1][self.x]
        if curr == "WB": return self.maze[self.y][self.x-1]
        if curr == "EB": return self.maze[self.y][self.x+1]
        if curr == "SN": return self.maze[self.y+1][self.x]
        if curr == "NN": return self.maze[self.y-1][self.x]
        if curr == "WN": return self.maze[self.y][self.x-1]
        if curr == "EN": return self.maze[self.y][self.x+1] 
        if curr == "M": return self.maze[self.y][self.x] 

        assert False


    def print_maze(self):
        """
        Prints the 2D array representing the maze
        Prints an 'M' for the current location of the bot in the maze
        """
        for row in range(len(self.maze)):
            curr = ''
            for col in range(len(self.maze[row])):
                if row == self.y and col == self.x:
                    curr += 'M'
                else:
                    curr += self.maze[row][col]
            print(curr)

    def solve_maze(self):
        """
        Calls on the FSM to process the next input symbol from the maze
        in order to transition the bot between states until it reaches the "FIN" state
        """
        # TODO: Implement solve maze
        
        #tell brain next symbol
        #get what the next move is
        #use that move until you get moneys
        while(self.brain.current_state != "M"):
            self.brain.process(self.get_next_space())
            self.print_maze()
        print("Determined the path:")
        print(self.path)



