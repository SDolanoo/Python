from bank_gui import MainPage, LoggedInUser
from file_operator import FileOperator

file_op = FileOperator()
gui = MainPage(file_op)
logged_in = LoggedInUser(file_op, "Test")
