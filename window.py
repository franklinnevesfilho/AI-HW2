import tkinter as tk
from PIL import Image, ImageTk  # Import from Pillow
from solutions import *



def action_button(button_text, command=lambda: print("button Pressed"), frame=None, pady=0, padx=0):
    """ Helper function to create a button with a command """
    button = tk.Button(frame, text=button_text, command=command)
    button.pack(side=tk.LEFT, pady=pady)


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Artificial Intelligence - HW2')
        self.root.geometry('500x600')

        # Problem 1 default algorithm selection
        self.algorithm = tk.StringVar(value="BFS")
        # problem 2 grid
        self.grid = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

        self.show_main_menu()

    def _clear_window(self):
        """
        Clear the window of all widgets
        :return: void
        """
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        """
        Show the main menu with buttons to navigate to different problems
        :return: display screen
        """
        self._clear_window()

        label = tk.Label(self.root, text='Choose the problem you want to solve:')
        label.pack(pady=20)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        # Example of buttons to navigate to different problems
        action_button('Problem 1: count the islands', self.show_problem_1, button_frame)
        action_button('Problem 2: 8 puzzle game', self.show_problem_2, button_frame)

    def show_problem_1(self):
        """
        Show Problem 1 screen with image and algorithm selection
        :return: problem 1 screen
        """
        self._clear_window()

        # ===============================================
        # Header
        # ===============================================
        title = tk.Label(self.root, text="Problem 1: Number of Islands")
        title.pack(pady=20)
        label = tk.Label(self.root, text="Select Search Algorithm:")
        label.pack()
        # ===============================================

        # ===============================================
        # Dropdown menu to select BFS or DFS
        # ===============================================
        algo_menu = tk.OptionMenu(self.root, self.algorithm, "BFS", "DFS")
        algo_menu.pack(pady=10)

        # ===============================================
        # Display the map image
        # ===============================================
        label = tk.Label(self.root, text="Map:")
        label.pack()
        # Display image from assets folder
        try:
            img = Image.open('assets/map1.png')
            img = img.resize((200, 200))
            img = ImageTk.PhotoImage(img)

            img_label = tk.Label(self.root, image=img)
            img_label.image = img
            img_label.pack(pady=10)
        except Exception as e:
            error_label = tk.Label(self.root, text=f"Error loading image: {e}")
            error_label.pack(pady=10)
        # ===============================================

        # ===============================================
        # Buttons to navigate back or count the islands
        # ===============================================
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        def solution():
            # Get the selected algorithm
            method = self.algorithm.get().lower()
            # Call the count_islands function from solution1.py
            island_count = count_islands(method=method)
            # Show the answer in a new window
            self.show_answer("Island Count", str(island_count))


        action_button('<- Back', self.show_main_menu, button_frame)
        action_button('Count Islands', solution, button_frame)

    def show_problem_2(self):
        """
        Show Problem 2 screen with grid to input values
        :return: problem 2 screen
        """
        self._clear_window()

        # ===============================================
        # Header
        # ===============================================
        label = tk.Label(self.root, text="Problem 2: 8 - Puzzle Game")
        label.pack(pady=20)
        # ===============================================

        # ===============================================
        # Create the grid as entry fields
        # ===============================================
        grid_frame = tk.Frame(self.root)
        grid_frame.pack()

        entry_widgets = []  # Store entry widgets to access them later
        for i, row in enumerate(self.grid):
            row_frame = tk.Frame(grid_frame)
            row_frame.pack()

            row_entries = []  # Store the row's entries

            for j, cell_value in enumerate(row):
                cell_frame = tk.Frame(row_frame, width=50, height=50)
                cell_frame.pack(side=tk.LEFT, padx=5, pady=5)

                # Create an entry field for each cell
                entry = tk.Entry(cell_frame, width=5, justify='center')
                entry.insert(0, str(cell_value))  # Insert the initial value
                entry.pack()

                # Append the entry widget to the row's entry list
                row_entries.append(entry)

            entry_widgets.append(row_entries)
        # =================================

        # Add a button to save the grid changes
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        action_button('<- Back', self.show_main_menu, button_frame)
        action_button('Try to Solve', lambda: self.solve_puzzle(entry_widgets), button_frame)

    def solve_puzzle(self, entry_widgets=None):
        """ Save the updated grid values back to the grid variable """
        # Iterate through the entry widgets and update the grid with new values
        for i, row_entries in enumerate(entry_widgets):
            for j, entry in enumerate(row_entries):
                try:
                    # Try to convert the input value to an integer
                    self.grid[i][j] = int(entry.get())
                except ValueError:
                    print(f"Invalid value in cell ({i},{j}): '{entry.get()}'")

        # Call the solve_puzzle function from solution2.py
        solved = solve_puzzle(self.grid)
        # Show the answer in a new window
        if solved is not None:
            self.show_answer("Minimum Moves", str(solved))
        else:
            self.show_answer("No Solution", "No solution found")

        # Optionally print the updated grid to the console to check values
        print("Updated grid:", self.grid)

    def show_answer(self, text: str, answer: str):
        # show a new window with the answer
        answer_window = tk.Toplevel(self.root)
        answer_window.title('Answer')
        answer_window.geometry('200x100')
        label = tk.Label(answer_window, text=f'{text}: {answer}')
        label.pack(pady=20)
        action_button('Close', answer_window.destroy, answer_window)


    def run(self):
        self.root.mainloop()
