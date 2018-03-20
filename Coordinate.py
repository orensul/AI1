#Coordinate class simply represents a location on the board. Used to simplify storage of locations
class Coordinate:
    def __init__(self, row,column):
        self.row=row
        self.column=column

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def __str__(self):
        message='Row,Column: '+str(self.column)+' '+str(self.row)
        return message
