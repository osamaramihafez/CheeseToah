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


#______________________________________________________________________________________________________________________________________________________________________________#
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
        self._tm = TOAHModel(4)
        self._tm.fill_first_stool(number_of_cheeses)

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
        print(' \'from (stool number) to (second stool number)\'')
        print('To exit the game:')
        print(' \"exit\"')
        
        raw_command = ''
        refined_command = []
        exit_requested = False
        
        # While the user hasn't chosen to 
        while exit_requested == False:
            # Outputs string representation of puzzle after move is executed
            print('Current Arrangement:\n')            
            print(self._tm)
            raw_command = input()
            # Tries to firstly refine input for further use.
            if raw_command != 'exit':
                try:
                    raw_command = command.split('/"') #Impractical, since the user doesn't expect to print the slashes as well.
                except InvalidInputError:
                    print('[ERROR: Invalid Input]')
                else:
                    # Else, checks further whether the refined input itself is useable.
                    if ((raw_command[0] + raw_command[2]).isdigit()) or \
                       (not (raw_command[1] + raw_command[3]).isdigit()):
                        raise InvalidInputError('[ERROR: Invalid Input]')
                    # Calls imported move() function to execute move according to given command.
                    move(num(raw_command[0]) - 1, num(raw_command[2]) - 1)    
            elif raw_command == 'exit':
                exit_requested = True
        print("Good Game!", ":)")
#_______________________________________________________________________________________________________________________________________________________________________________#


#Note that I took your code and just modified it a little bit. Hope you don't mind. I left most of your code alone. 
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
            prev_stool = input("which stool would you like to move a cheese block from? ")
            new_stool = input("Where would you like to move it? ")
            try:
                move(self._tm, int(prev_stool) - 1, int(new_stool) - 1)
            except IllegalMoveError:
                print("***\nYou can't do that...\n***")
            
            
            
            # Tries to firstly refine input for further use.
            #try:
                #raw_command = raw_command.split('/"')
            #except InvalidInputError:
                #print('***ERROR: Invalid Input***')
            #else:
                ## Else, checks further whether the refined input itself is useable.
                #if ((raw_command[0] + raw_command[2]).isdigit()) or \
                   #(not (raw_command[1] + raw_command[3]).isdigit()):
                    #raise InvalidInputError('[ERROR: Invalid Input]')
                ## Calls imported move() function to execute move according to given command.
                #move(num(raw_command[0]) - 1, num(raw_command[2]) - 1)



if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.
    print("~Console-Based Version~")
    num_stools = input("How many stools would you like to play with?  ")
    cheese_blocks = input("How many cheese blocks (must have less than {0} blocks)?  ".format("unknown"))
    #note that there should be a limit to the number of cheese_blocks compared to the number of cheese blocks
    game = ConsoleController_Osama(int(cheese_blocks), int(num_stools))
    game.play_loop()
    