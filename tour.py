"""
functions to run TOAH tours.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
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
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "__main__":'

import time, math
from toah_model import TOAHModel


def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    @rtype: None
    """
    
    num_of_cheeses = model.get_number_of_cheeses()

    if animate:
        print(model)
        time.sleep(delay_btw_moves)
        # animate_solve_four_stool function will go here
    else:
        solve_four_stool_model(model, num_of_cheeses, 0, 1, 2, 3)


def solve_three_stool_model(model, num_of_cheese_stacks, from_stool,
                            temp_stool, to_stool):

    if num_of_cheese_stacks == 1:
        model.move(from_stool, to_stool)
    else:
        solve_three_stool_model(model, num_of_cheese_stacks - 1, from_stool, to_stool, temp_stool)
        model.move(from_stool, to_stool)
        solve_three_stool_model(model, num_of_cheese_stacks - 1, temp_stool, from_stool, to_stool)

def evaluate_min_moves(num_of_cheeses, current_i_value):
    if current_i_value == 0 or num_of_cheeses < 0:
        return 10000000
    if num_of_cheeses == 0:
        return 0
    if num_of_cheeses == 1:
        return 1
    elif num_of_cheeses > 1:
        return (2 * (evaluate_min_moves(num_of_cheeses - current_i_value, current_i_value))) + 2 ** current_i_value - 1

def i_value(num_of_cheeses, current_i_value):
    
    if num_of_cheeses == 1:
        return 0
    
    if current_i_value > 0:
        prev_min_moves = evaluate_min_moves(num_of_cheeses, current_i_value - 1)
        new_min_moves = evaluate_min_moves(num_of_cheeses, current_i_value)
    else:
        return 10000000
    
    print(prev_min_moves, new_min_moves)
    if new_min_moves < prev_min_moves:
        return current_i_value
    
    return i_value(num_of_cheeses, current_i_value + 1)

def solve_four_stool_model(model, num_of_cheeses, from_stool,
                           first_temp, second_temp, to_stool):
    
    # Following line found sub_puzzle_num (i-value) using illegal formula:
    # sub_puzzle_num = num_of_cheeses - math.ceil(math.sqrt((num_of_cheeses * 2) + 0.25) - 0.5)

    # Index by which to split the model is found with helper function
    sub_puzzle_num = i_value(num_of_cheeses, 1)
    print(sub_puzzle_num)
    new_cheeses_num = num_of_cheeses - sub_puzzle_num 
    
    if num_of_cheeses == 1 or num_of_cheeses == 2: 
        # First case in which there are 1 or 2 cheeses, directly call the previous funtion
        solve_three_stool_model(model, num_of_cheeses, from_stool, first_temp, to_stool)
    else:
        # Combines recursion with directly calling previous function to solve four stool model
        solve_four_stool_model(model, sub_puzzle_num, from_stool, to_stool, second_temp,
                               first_temp)
        solve_three_stool_model(model, new_cheeses_num, from_stool, second_temp, to_stool)
        solve_four_stool_model(model, sub_puzzle_num, first_temp, from_stool, second_temp,
                               to_stool)
        
if __name__ == '__main__':
    num_cheeses = 9
    delay_between_moves = 0.5
    console_animate = False

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(num_cheeses)

    tour_of_four_stools(four_stools,delay_between_moves,console_animate)#Idk why delay and animate are switched

    print(four_stools.number_of_moves())
    print(four_stools)