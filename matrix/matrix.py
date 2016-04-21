class Matrix:
    def __init__(self, input):
        self.rows = []
        self.columns = []
        input_rows = input.split("\n")
        for row_num, row in enumerate(input_rows):
            row_columns = row.split(" ")
            for col_num, value in enumerate(row_columns):
                if len(self.rows)-1 < row_num:
                    self.rows.append([0 for i in range(0, len(row_columns))])
                self.rows[row_num][col_num] = int(value)
                if len(self.columns)-1 < col_num:
                    self.columns.append([0 for i in range(0, len(input_rows))])
                self.columns[col_num][row_num] = int(value)
