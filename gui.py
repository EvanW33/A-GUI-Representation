## -*- coding: utf-8 -*-

from tkinter import *
from node import *
from time import sleep

class GUI(Node):
    width = 800
    height = width - 150

    def __init__(self, num_rectangles, sides, length):
        self.start = False
        self.end = False
        self.show_algorithm = False
        self.breakGUI = False

        self.count = 0

        self.num_rectangles = num_rectangles
        self.sides = sides
        self.length = length
        self.increment = self.length / self.num_rectangles
        self.x1 = 0
        self.y1 = 0
        self.x2 = self.increment
        self.y2 = self.increment
        self.canvas_dims = self.num_rectangles * self.sides

        self.gui = Tk()
        self.gui.title("Shortest Path Algorithm")

    def init_checkBox(self):
        self.box = IntVar()
        self.check = Checkbutton(self.gui, text="Show Algorithm", variable=self.box, command=self.checkBox_checked).grid(row=0, column=0)

    def checkBox_checked(self):
        if self.show_algorithm != True:
            self.show_algorithm = True
        else:
            self.show_algorithm = False

    def init_button(self):
        self.button = Button(self.gui, text="Find Shortest Path", fg="green", command=self.start_algorithm)
        self.button.grid(column=0, row=1)

    def create_grid(self):
        """
        Creates the grid in the GUI that's used for the algorithm to
        visually show how the algorithm is working.

        Returns: node_list which is a list holding all of the nodes (rectangles)
        """
        self.node_list = []
        for i in range(self.num_rectangles):
            self.node_list.append([x for x in range(self.num_rectangles)])
        self.canvas = Canvas(self.gui, height=self.length, width=self.length, bg="black")
        self.canvas.bind("<1>", self.clicked)

        for i in range(self.num_rectangles):
            for j in range(self.num_rectangles):
                self.r = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="white")
                self.node_list[i][j] = Node(i, j, self.x1, self.y1, self.x2, self.y2)
                self.x1 += self.increment
                self.x2 += self.increment
            self.y1 += self.increment
            self.y2 += self.increment
            self.x1, self.x2 = 0, self.increment

        self.canvas.grid(row=0, column=1)
        return self.node_list

    def get_rectangle_clicked(self, x, y):
        i = x // self.increment
        j = y // self.increment
        list_index = int(self.num_rectangles * j + i)
        return (i, j, list_index)

    def clicked(self, event):
        i, j, list_index = self.get_rectangle_clicked(event.x, event.y)
        rectangle = self.node_list[int(j)][int(i)]

        if self.start == False:
            self.start = True
            self.r = self.canvas.create_rectangle(rectangle.get_x1(), rectangle.get_y1(), rectangle.get_x2(), rectangle.get_y2(), fill="green")
            self.canvas.grid(row=0, column=1)

            self.start_node = rectangle

        elif self.end == False:
            self.end = True
            self.r = self.canvas.create_rectangle(rectangle.get_x1(), rectangle.get_y1(), rectangle.get_x2(), rectangle.get_y2(), fill="red")
            self.canvas.grid(row=0, column=1)

            self.goal_node = rectangle

        else:
            return

    def get_children(self, current):
        x = current.get_x()
        y = current.get_y()
        children_list = []

        try:
            if x != self.num_rectangles:
                children_list.append(self.node_list[x + 1][y])
        except Exception as e: # Node doesn't exist (border)
            pass

        try:
            if x != 0:
                children_list.append(self.node_list[x - 1][y])
        except Exception as e: # Node doesn't exist (border)
            pass

        try:
            if y != self.num_rectangles:
                children_list.append(self.node_list[x][y + 1])
        except Exception as e: # Node doesn't exist (border)
            pass

        try:
            if y != 0:
                children_list.append(self.node_list[x][y - 1])
        except Exception as e: # Node doesn't exist (border)
            pass

        return children_list

    def find_heuristic(self, open):
        return max(abs(open.x - self.goal_node.x), abs(open.y - self.goal_node.y))

    def find_heuristic_plus_goal(self, open):
        return self.find_heuristic(open) + open.get_g()

    def start_algorithm(self, event=None):
        if self.start != True and self.end != True:
            self.breakGUI = True
            raise ValueError("Start and end points haven't been initialized.")

        wait_time = self.timer()

        current = self.start_node
        goal = self.goal_node

        open = [current]
        closed = []

        cont = True

        while cont:
            current = min(open, key=self.find_heuristic_plus_goal)

            if current == goal:
                cont = False
                path = []
                while current.get_parent():
                    path.append(current)
                    current = current.get_parent()
                path.append(current)
                # answer found
                for i in path[::-1]:
                    #applies the change to the new rectangles in the new path
                    self.r = self.canvas.create_rectangle(i.get_x1(), i.get_y1(), i.get_x2(), i.get_y2(), fill="blue")
                    self.canvas.grid(row=0, column=1)
                    self.gui.update_idletasks()
                    sleep(wait_time)
            if not cont:
                break
            open.remove(current)
            closed.append(current)

            for child in self.get_children(current):
                if child in closed:
                    continue

                if child in open:
                    g = current.get_g() + current.get_move_cost()
                    if child.get_g() > g:
                        child.set_g(g)
                        child.set_parent(current)

                else:
                    child.set_g(current.get_g() + current.get_move_cost())
                    child.set_h(self.find_heuristic(child))
                    child.set_parent(current)
                    open.append(child)


    def timer(self):
        if self.show_algorithm == True:
            return 0.075
        else:
            return 0

    def run(self):
        self.gui.mainloop()
