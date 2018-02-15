"""
ConsoleController: User interface for manually solving
Anne Hoy's problems from the console.
"""


# Copyright 2014, 2017 Dustin Wehr, Danny Heap, Bogdan Simion,
# Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2018.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.


from toah_model import TOAHModel, IllegalMoveError

def move(model, origin, dest):
    """ Apply move from origin to destination in model.

    May raise an IllegalMoveError.

    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    model.move(origin, dest)

class InvalidInputError(ValueError):
    pass

class ConsoleController_Osama:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """
        self._tm = TOAHModel(number_of_stools)
        self._tm.fill_first_stool(number_of_cheeses)
        self._game_over = False
        
    def game_over(self):
        self._game_over = True
        print("Thanks for Playing :)")
    
    def play_loop(self):
        """ Play Console-based game.

        @param ConsoleController self:
        @rtype: None

        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        """
        print("Good Luck!", ":)")
        # While the user hasn't chosen to 
        while self._game_over == False:
            # Outputs string representation of puzzle after move is executed
            print('Current Arrangement:\n')            
            print(self._tm)
            exit = input("To keep playing, press enter. Otherwise, type \'exit\' then hit enter. ")
            if exit == "exit":
                return self.game_over()           
            prev_stool = input("Which stool would you like to move a cheese block from? ")
            new_stool = input("Where would you like to move it? ")
            try:
                move(self._tm, int(prev_stool) - 1, int(new_stool) - 1)
            except IllegalMoveError:
                print("***\nYou can't do that...\n***")

def value_check(num_stools, cheese_blocks):
    pf = "Pass"
    try:
        x = int(cheese_blocks)
        y = int(num_stools)
    except ValueError:
        pf = "Fail"
    else:
        if x<0 or y<0:
            pf = "Fail"
        else:
            pf = "Pass"
    
    while pf == "Fail":
        print("\nPlease enter a positive integer for stools and cheese blocks\n")
        num_stools = input("How many stools would you like to play with?  ")
        cheese_blocks = input("How many cheese blocks (must have less than {0} blocks)?  ".format("unknown"))
        try:
            x = int(cheese_blocks)
            y = int(num_stools)
        except ValueError:
            pf = "Fail"
        else:
            if x<0 or y<0:
                pf = "Fail"
            else:
                pf = "Pass"            
    return x, y

def run():
    print("~Console-Based Version~")
    num_stools = input("How many stools would you like to play with?  ")
    cheese_blocks = input("How many cheese blocks (must have less than {0} blocks)?  ".format("unknown"))
    #note that there should be a limit to the number of cheese_blocks compared to the number of cheese blocks    
    x, y = num_stools, cheese_blocks
    a, b = value_check(x, y)
    game = ConsoleController_Osama(a, b)
    #Too much inside if name main.
    game.play_loop()    

if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.
    run()