## -*- coding: utf-8 -*-

from tkinter import *

class Node():
    """
    A Node object for each box in the GUI to be represented by. Holds a
    x and y value to know the location of the Node.
    """
    x_value = 0
    y_value = 0
    def __init__(self, x, y, x1, y1, x2, y2):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.h = 0
        self.g = 0
        self.parent = None
        self.move_cost = 1

    def set_parent(self, new_node):
        self.parent = new_node

    def increment_g(self):
        self.g += 1

    def get_g(self):
        return self.g

    def set_g(self, new_g):
        self.g = new_g

    def set_h(self, new_h):
        self.h = new_h

    def get_parent(self):
        return self.parent

    def set_parent(self, p):
        self.parent = p

    def get_move_cost(self):
        return self.move_cost

    def __repr__(self):
        """String representation of the Node when called by a print statement."""
        return f"\nGUI Coordinates: ({self.x}, {self.y})"

    def get_x(self):
        """Returns the Node's x"""
        return self.x

    def get_y(self):
        """Returns the Node's y"""
        return self.y

    def get_x1(self):
        return self.x1

    def get_y1(self):
        return self.y1

    def get_x2(self):
        return self.x2

    def get_y2(self):
        return self.y2

    def get_xy():
        """Returns a tuple in format (x, y)"""
        return (self.x, self.y)

    def is_same_xy(self, tupComparison):
        """Compares the instance's i and j values with a given tuple"""
        if self.get_xy() == tupComparison:
            return True
        return False
