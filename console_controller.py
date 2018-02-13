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
    pass


class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """
        pass

    class InvalidInputError(ValueError):
        pass 

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
        
        print('~ Console-Based Version ~')
        print('Use the following commands to manually control the puzzle:')
        print('To move a block of cheese from one peg to another:')
        print('    /"from (stool number) to (second stool number/"')
        print('To exit the game:')
        print('    /"exit/"')
        
        raw_command = ''
        refined_command = []
        exit_requested = False
        
        # While the user hasn't chosen to 
        while exit_requested == false:
            raw_command = input()
            # Tries to firstly refine input for further use.
            if raw_command != 'exit':
                try:
                    raw_command = command.split('/"')
                except InvalidInputError:
                    print('[ERROR: Invalid Input]')
                else:
                    # Else, checks further whether the refined input itself is useable.
                    if ((raw_command[0] + raw_command[2]).isdigit()) or \
                       (not (raw_command[1] + raw_command[3]).isdigit()):
                        raise InvalidInputError('[ERROR: Invalid Input]')
                    # Calls imported move() function to execute move according to given command.
                    move(num(raw_command[0]) - 1, num(raw_command[2]) - 1)
                
                # Outputs string representation of puzzle after move is executed
                print('Current Arrangement:\n')
                print(TOAHModel.__str__(self))
                
            elif raw_command == 'exit':
                exit_requested = True 

if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.