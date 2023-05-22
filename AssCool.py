"""

Name: Sahil Desai
Username: sdes541
Student ID: 632014971

Description: A game of connect 4. But the game only ends when the board is full.
Whoever has the most 4 connected counters wins. 

"""


class GameBoard:
    def __init__(self, size):
        
        self.size = size
        self.num_entries = [0] * size
        self.items = [[0] * size for i in range(size)]
        self.points = [0] * 2
        
        
    def num_free_positions_in_column(self, column):
        
        return self.size - self.num_entries[column]
    
        
    def game_over(self):
        
        for element in self.num_entries:
            
            if element != self.size:
                return False
                
        return True

        
    def display(self):
        
        last_element = self.size - 1
        
        for row in range(last_element, -1, -1):

            print(row, end="|") # <--- Cool Code Begins
            
            for column in self.items:
        
                if column[row] == 1:

                    print("o", end="|")

                elif column[row] == 2:

                    print("x", end="|")

                else:
                    print(" ", end="|") # <--- Cool Code Ends
                
            print()
        print("  ", end="")
        print("-" * (self.size * 2 - 1))

        print("  ", end="")
        for x in range(0, self.size):
            
            print(x, end=" ")

        print()
        print("Points player 1:", self.points[0])
        print("Points player 2:", self.points[1])

    
    def add(self, column, player):

        if column < 0 or column >= self.size or self.num_entries[column] >= self.size:

            return False

        else:
            row = self.num_entries[column]
            self.items[column][row] = player
            self.num_entries[column] += 1

            count = self.num_new_points(column, row, player)
            self.points[player - 1] += count
            

            return True
            
            
    def num_new_points(self, column, row, player):

        count = 0
        
        # HORIZONTAL -------------------------------------------------------------------------
        
        horizontal = []
        horizontal_forward = []
        horizontal_backward = []
        
        for column_number in self.items:
            horizontal.append(column_number[row])

        # Horizontal Forward
        
        for element in horizontal[len(horizontal) - 1: column: -1]:

            if element == player:
                horizontal_forward.append(element)
    
            else:
                horizontal_forward = []

        # Checking Length Forward
        
        if len(horizontal_forward) > 3:

            horizontal_forward = 3

        else:

            horizontal_forward = len(horizontal_forward)

        # Horizontal Backward
        
        for element in horizontal[: column]:
    
            if element == player:
                horizontal_backward.append(element)
            else:
                horizontal_backward = []

        
        # Checking Length
        
        if len(horizontal_backward) > 3:

            horizontal_backward = 3

        else:

            horizontal_backward = len(horizontal_backward)

        # Horizontal Calculation
        
        horizontal_final = horizontal_forward + horizontal_backward

        if horizontal_final >= 3:
            horizontal_final = horizontal_final + 1 - 3
        else:
            horizontal_final = 0

        count += horizontal_final

        # VERTICAL -----------------------------------------------------------------------------
        
        vertical = self.items[column]
        vertical_forward = []
        vertical_backward = []
        
        # Vertical Forward
        
        for element in vertical[len(vertical) - 1: row: -1]:

            if element == player:
                vertical_forward.append(element)
    
            else:
                vertical_forward = []

        # Checking Length Forward
        
        if len(vertical_forward) > 3:

            vertical_forward = 3

        else:

            vertical_forward = len(vertical_forward)

        
        # Vertical Backward
        
        for element in vertical[: row]:

            if element == player:
                vertical_backward.append(element)
    
            else:
                vertical_backward = []

        # Checking Length Backward
        
        if len(vertical_backward) > 3:

            vertical_backward = 3

        else:

            vertical_backward = len(vertical_backward)

        # Vertical Calculation
        
        vertical_final = vertical_forward + vertical_backward

        if vertical_final >= 3:
            
            vertical_final = vertical_final + 1 - 3

        else:
            vertical_final = 0
            
        count += vertical_final


        # TOP TO BOTTOM ------------------------------------------------------------------------

        tb = []
        tb_forward = []
        tb_backward = []

        if row + column <= self.size - 1:
            starting_column = 0
            starting_row = row + column

        else:
            starting_column = row + column - (self.size - 1)
            starting_row = self.size - 1

        temp = starting_column # Adjusts the column number. 

        while starting_column <= (self.size - 1) and starting_row != -1:
            
            selected_column = self.items[starting_column]
            tb.append(selected_column[starting_row])
            starting_column += 1
            starting_row -= 1

        column1 = column - temp

        # TB Forward

        for element in tb[len(tb) - 1: column1: -1]:

            if element == player:
                tb_forward.append(element)
            else:
                tb_forward = []
                
        # Checking Length Forward
        if len(tb_forward) > 3:
            tb_forward = 3

        else:
            tb_forward = len(tb_forward)

    
        # TB Backward
        for element in tb[:column1]:

            if element == player:
                tb_backward.append(element)
            else:
                tb_backward = []

        # Checking Length Backward
        if len(tb_backward) > 3:
            tb_backward = 3
        else:
            tb_backward = len(tb_backward)


        # TB Calculation
        
        tb_final = tb_forward + tb_backward

        if tb_final >= 3:
            tb_final = tb_final + 1 - 3
            
        else:
            tb_final = 0
            
        count += tb_final

        
        # BOTTOM TO TOP ------------------------------------------------------------------------

        bt = []
        bt_forward = []
        bt_backward = []


        if row >= column:
            starting_column = 0
            starting_row = row - column

        else:
            starting_column = column - row
            starting_row = 0

        temp = starting_column # Adjusts the column number. 
            
        while starting_column <= (self.size - 1) and starting_row != self.size:
            
            selected_column = self.items[starting_column]
            bt.append(selected_column[starting_row])
            starting_column += 1
            starting_row += 1

        column2 = column - temp
        
        # BT Forward

        for element in bt[len(bt) - 1: column2: -1]:

            if element == player:
                bt_forward.append(element)
            else:
                bt_forward = []
                
        # Checking Length Forward
        if len(bt_forward) > 3:
            bt_forward = 3

        else:
            bt_forward = len(bt_forward)


        # BT Backward
        for element in bt[:column2]:

            if element == player:
                bt_backward.append(element)
            else:
                bt_backward = []


        # Checking Length Backward
        if len(bt_backward) > 3:
            bt_backward = 3
        else:
            bt_backward = len(bt_backward)

        # TB Calculation
        
        bt_final = bt_forward + bt_backward

        if bt_final >= 3:
            bt_final = bt_final + 1 - 3
            
        else:
            bt_final = 0
            
        count += bt_final

        
            
        return count

    def free_slots_as_close_to_middle_as_possible(self):

        free_slots = []
        distances = []
        final_free_slots = []

        middle = (self.size - 1) / 2


        for index in range(0, len(self.num_entries)):

            element = self.num_entries[index]

            if element < self.size:

                free_slots.append(index)

        for index in range(0, len(free_slots)):

            element = free_slots[index]
            distance = abs(element - middle)
            distances.append([distance, element])

        distances.sort()

        for element in distances:

            final_free_slots.append(element[1])


        return final_free_slots

    def column_resulting_in_max_points(self, player):

        coordinates = []
        maximum_points = []
        final = 0

        free_slots = self.free_slots_as_close_to_middle_as_possible()

        for element in free_slots:

            column = element
            row = self.num_entries[column]

            coordinates.append([column, row])
            

        for index in range(0, len(coordinates)):

            element = coordinates[index]
            column = element[0]
            row = element[1]
            points = self.num_new_points(column, row, player)

            maximum_points.append([points, column])


        biggest = 0
        col_number = maximum_points[0][1]
        

        for element in maximum_points:

            if element[0] > biggest:

                biggest = element[0]
                col_number = element[1]

        return col_number, biggest


class FourInARow:
    def __init__(self, size):
        self.board=GameBoard(size)
    def play(self):
        print("*****************NEW GAME*****************")
        self.board.display()
        player_number=0
        print()
        while not self.board.game_over():
            print("Player ",player_number+1,": ")
            if player_number==0:
                valid_input = False
                while not valid_input:
                    try:
                        column = int(input("Please input slot: "))       
                    except ValueError:
                        print("Input must be an integer in the range 0 to ", self.board.size)
                    else:
                        if column<0 or column>=self.board.size:
                            print("Input must be an integer in the range 0 to ", self.board.size)
                        else:
                            if self.board.add(column, player_number+1):
                                valid_input = True
                            else:
                                print("Column ", column, "is alrady full. Please choose another one.")
            else:
                # Choose move which maximises new points for computer player
                (best_column, max_points)=self.board.column_resulting_in_max_points(2)
                if max_points>0:
                    column=best_column
                else:
                    # if no move adds new points choose move which minimises points opponent player gets
                    (best_column, max_points)=self.board.column_resulting_in_max_points(1)
                    if max_points>0:
                        column=best_column
                    else:
                        # if no opponent move creates new points then choose column as close to middle as possible
                        column = self.board.free_slots_as_close_to_middle_as_possible()[0]
                self.board.add(column, player_number+1)
                print("The AI chooses column ", column)
            self.board.display()   
            player_number=(player_number+1)%2
        if (self.board.points[0]>self.board.points[1]):
            print("Player 1 (circles) wins!")
        elif (self.board.points[0]<self.board.points[1]):    
            print("Player 2 (crosses) wins!")
        else:  
            print("It's a draw!")
            
game = FourInARow(6)
game.play()        





        
        
