from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import locale
import math

class WindowsCalculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()

    def initUI(self):

        locale.setlocale(locale.LC_ALL, '')

        self.parent.title("Windows Calculator")

        self.previous_operand = ""
        self.current_operand = ""

        self.operation = ""


        HEIGHT = 450
        WIDTH = 351

        canvas = Canvas(self.parent, height=HEIGHT, width=WIDTH, bg='#2c3031')
        canvas.pack()

        BUTTON_HEIGHT = 55
        BUTTON_WIDTH = 85

        previous_operand_font = Font(family="Helvetica", size=10, weight='bold')
        self.previous_operand_lbl = Label(canvas, text='', fg='grey', bg='#2c3031', anchor='e', font=previous_operand_font)
        self.previous_operand_lbl.place(relx=.5, rely=.04, height=25, relwidth=.95, anchor='n')


        current_operand_font = Font(family="Halvetica", size=28, weight='bold')
        self.current_operand_lbl = Label(canvas, text='', fg='white', bg='#2c3031', anchor='e', font=current_operand_font)
        self.current_operand_lbl.place(relx=.5, rely=.12, height=35, relwidth=.95, anchor='n')


        # sixth row

        my_font = Font(family="Helvetica", size=14)

        sixth_row_rely = 0.373

        # self.percent_btn = Button(canvas, text='%', bg='#131313', fg='white', font=my_font, command=lambda: self.percent())
        # self.percent_btn.place(relx=.134, rely=sixth_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        # self.percent_btn.bind("<Enter>", self.percent_btn_change_bg_color)
        # self.percent_btn.bind("<Leave>", self.percent_btn_change_bg_color_back)

        self.clear_entry_btn = Button(canvas, text='CE', bg='#131313', fg='white', font=my_font, command=lambda: self.clear_entry())
        self.clear_entry_btn.place(relx=.26, rely=sixth_row_rely, height=BUTTON_HEIGHT, width=172, anchor='s')
        self.clear_entry_btn.bind("<Enter>", self.clear_entry_btn_change_bg_color)
        self.clear_entry_btn.bind("<Leave>", self.clear_entry_btn_change_bg_color_back)

        self.clear_btn = Button(canvas, text='C', bg='#131313', fg='white', font=my_font, command=lambda: self.clear())
        self.clear_btn.place(relx=.623, rely=sixth_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.clear_btn.bind("<Enter>", self.clear_btn_change_bg_color)
        self.clear_btn.bind("<Leave>", self.clear_btn_change_bg_color_back)

        self.backspace_btn = Button(canvas, text='⌫', bg='#131313', fg='white', font=my_font, command=lambda: self.backspace())
        self.backspace_btn.place(relx=.869, rely=sixth_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.backspace_btn.bind("<Enter>", self.backspace_btn_change_bg_color)
        self.backspace_btn.bind("<Leave>", self.backspace_btn_change_bg_color_back)


        # fifth row

        fifth_row_rely = 0.496

        self.inverse_btn = Button(canvas, text='1/x', bg='#131313', fg='white', font=my_font, command=lambda: self.inverse())
        self.inverse_btn.place(relx=.134, rely=fifth_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.inverse_btn.bind("<Enter>", self.inverse_btn_change_bg_color)
        self.inverse_btn.bind("<Leave>", self.inverse_btn_change_bg_color_back)

        self.square_btn = Button(canvas, text='x²', bg='#131313', fg='white', font=my_font, command=lambda: self.choose_operation("x²"))
        self.square_btn.place(relx=.379, rely=fifth_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.square_btn.bind("<Enter>", self.square_btn_change_bg_color)
        self.square_btn.bind("<Leave>", self.square_btn_change_bg_color_back)

        self.square_root_btn = Button(canvas, text='√', bg='#131313', fg='white', font=my_font, command=lambda: self.sqrt())
        self.square_root_btn.place(relx=.623, rely=fifth_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.square_root_btn.bind("<Enter>", self.square_root_btn_change_bg_color)
        self.square_root_btn.bind("<Leave>", self.square_root_btn_change_bg_color_back)

        self.division_btn = Button(canvas, text='÷', bg='#131313', fg='white', font=my_font, command=lambda: self.choose_operation("÷"))
        self.division_btn.place(relx=.869, rely=fifth_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.division_btn.bind("<Enter>", self.division_btn_change_bg_color)
        self.division_btn.bind("<Leave>", self.division_btn_change_bg_color_back)


        # fourth row

        fourth_row_rely = 0.619

        self.num_seven_btn = Button(canvas, text='7', bg='#060606', fg='white', font=my_font, command=lambda: self.append_number("7"))
        self.num_seven_btn.place(relx=.134, rely=fourth_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.num_seven_btn.bind("<Enter>", self.num_seven_btn_change_bg_color)
        self.num_seven_btn.bind("<Leave>", self.num_seven_btn_change_bg_color_back)

        self.num_eight_btn = Button(canvas, text='8', bg='#060606', fg='white', font=my_font, command=lambda: self.append_number("8"))
        self.num_eight_btn.place(relx=.379, rely=fourth_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.num_eight_btn.bind("<Enter>", self.num_eight_btn_change_bg_color)
        self.num_eight_btn.bind("<Leave>", self.num_eight_btn_change_bg_color_back)

        self.num_nine_btn = Button(canvas, text='9', bg='#060606', fg='white', font=my_font, command=lambda: self.append_number("9"))
        self.num_nine_btn.place(relx=.623, rely=fourth_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.num_nine_btn.bind("<Enter>", self.num_nine_btn_change_bg_color)
        self.num_nine_btn.bind("<Leave>", self.num_nine_btn_change_bg_color_back)

        self.multiply_btn = Button(canvas, text='*', bg='#131313', fg='white', font=my_font, command=lambda: self.choose_operation("*"))
        self.multiply_btn.place(relx=.869, rely=fourth_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.multiply_btn.bind("<Enter>", self.multiply_btn_change_bg_color)
        self.multiply_btn.bind("<Leave>", self.multiply_btn_change_bg_color_back)


        # third row

        third_row_rely = 0.742

        self.num_four_btn = Button(canvas, text='4', bg='#060606', fg='white', font=my_font, command=lambda: self.append_number("4"))
        self.num_four_btn.place(relx=.134, rely=third_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.num_four_btn.bind("<Enter>", self.num_four_btn_change_bg_color)
        self.num_four_btn.bind("<Leave>", self.num_four_btn_change_bg_color_back)

        self.num_five_btn = Button(canvas, text='5', bg='#060606', fg='white', font=my_font, command=lambda: self.append_number("5"))
        self.num_five_btn.place(relx=.379, rely=third_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.num_five_btn.bind("<Enter>", self.num_five_btn_change_bg_color)
        self.num_five_btn.bind("<Leave>", self.num_five_btn_change_bg_color_back)

        self.num_six_btn = Button(canvas, text='6', bg='#060606', fg='white', font=my_font, command=lambda: self.append_number("6"))
        self.num_six_btn.place(relx=.623, rely=third_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.num_six_btn.bind("<Enter>", self.num_six_btn_change_bg_color)
        self.num_six_btn.bind("<Leave>", self.num_six_btn_change_bg_color_back)

        self.minus_btn = Button(canvas, text='-', bg='#131313', fg='white', font=my_font, command=lambda: self.choose_operation("-"))
        self.minus_btn.place(relx=.869, rely=third_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.minus_btn.bind("<Enter>", self.minus_btn_change_bg_color)
        self.minus_btn.bind("<Leave>", self.minus_btn_change_bg_color_back)


        # second row

        second_row_rely = 0.865

        self.num_one_btn = Button(canvas, text='1', bg='#060606', fg='white', font=my_font, command=lambda: self.append_number("1"))
        self.num_one_btn.place(relx=.134, rely=second_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.num_one_btn.bind("<Enter>", self.num_one_btn_change_bg_color)
        self.num_one_btn.bind("<Leave>", self.num_one_btn_change_bg_color_back)


        self.num_two_btn = Button(canvas, text='2', bg='#060606', fg='white', font=my_font, command=lambda: self.append_number("2"))
        self.num_two_btn.place(relx=.379, rely=second_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.num_two_btn.bind("<Enter>", self.num_two_btn_change_bg_color)
        self.num_two_btn.bind("<Leave>", self.num_two_btn_change_bg_color_back)

        self.num_three_btn = Button(canvas, text='3', bg='#060606', fg='white', font=my_font, command=lambda: self.append_number("3"))
        self.num_three_btn.place(relx=.623, rely=second_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.num_three_btn.bind("<Enter>", self.num_three_btn_change_bg_color)
        self.num_three_btn.bind("<Leave>", self.num_three_btn_change_bg_color_back)

        self.plus_btn = Button(canvas, text='+', bg='#131313', fg='white', font=my_font, command=lambda: self.choose_operation("+"))
        self.plus_btn.place(relx=.869, rely=second_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.plus_btn.bind("<Enter>", self.plus_btn_change_bg_color)
        self.plus_btn.bind("<Leave>", self.plus_btn_change_bg_color_back)



        # first row

        first_row_rely = 0.988

        self.plus_minus_btn = Button(canvas, text='+/-', bg='#060606', fg='white', font=my_font, command=lambda: self.negate())
        self.plus_minus_btn.place(relx=.134, rely=first_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.plus_minus_btn.bind("<Enter>", self.plus_minus_btn_change_bg_color)
        self.plus_minus_btn.bind("<Leave>", self.plus_minus_btn_change_bg_color_back)

        self.num_zero_btn = Button(canvas, text='0', bg='#060606', fg='white', font=my_font, command=lambda: self.append_number("0"))
        self.num_zero_btn.place(relx=.379, rely=first_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.num_zero_btn.bind("<Enter>", self.num_zero_btn_change_bg_color)
        self.num_zero_btn.bind("<Leave>", self.num_zero_btn_change_bg_color_back)

        self.decimal_btn = Button(canvas, text='.', bg='#060606', fg='white', font=my_font, command=lambda: self.append_number("."))
        self.decimal_btn.place(relx=.623, rely=first_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.decimal_btn.bind("<Enter>", self.decimal_btn_change_bg_color)
        self.decimal_btn.bind("<Leave>", self.decimal_btn_change_bg_color_back)

        self.equals_btn = Button(canvas, text='=', bg='#134369', fg='white', font=my_font, command=lambda: self.compute())
        self.equals_btn.place(relx=.869, rely=first_row_rely, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, anchor='s')
        self.equals_btn.bind("<Enter>", self.equals_btn_change_bg_color)
        self.equals_btn.bind("<Leave>", self.equals_btn_change_bg_color_back)


    def clear_entry(self):
        self.previous_operand = ""
        self.current_operand = ""
        self.operation = ""
        self.update_display()

    def clear(self):
        self.current_operand = ""
        self.update_display()

    def backspace(self):
        self.current_operand = self.current_operand[:-1]
        self.update_display()

    def append_number(self, val):

        self.current_operand = str(self.current_operand)

        if val == ".":
            if "." in self.current_operand:
                return

        if len(self.current_operand) <= 14:
            self.current_operand += val
        else:
            messagebox.showwarning("Too many number.", "Too many numbers bro...")

        self.update_display()


    def choose_operation(self, operation):

        if self.current_operand == "":
            return

        if self.previous_operand != "":
            self.compute()

        self.operation = operation
        self.previous_operand = self.current_operand
        self.current_operand = ""

        self.update_display()


    def percent(self):

        if self.current_operand == "":
            return

        self.operation == "%"

        number = float(self.current_operand)

        computation = number / 100

        self.current_operand = self.strip_zero(computation)
        self.previous_operand = ""
        self.operation = ""

        self.previous_operand_lbl.configure(text=self.operation + str(number) + " =")
        self.current_operand_lbl.configure(text=str(self.current_operand))



    def sqrt(self):

        if self.current_operand == "":
            return

        self.operation = "√"

        number = float(self.current_operand)

        computation = math.sqrt(number)
        computation = round(computation, 12)

        self.current_operand = self.strip_zero(computation)
        self.previous_operand = ""
        self.operation = ""

        self.previous_operand_lbl.configure(text=self.operation + str(number) + " =")
        self.current_operand_lbl.configure(text=str(self.current_operand))


    def inverse(self):

        if self.current_operand == "":
            return

        self.operation = "1/x"

        number = float(self.current_operand)

        computation = 1/number
        computation = round(computation, 12)

        self.current_operand = self.strip_zero(computation)
        self.previous_operand = ""
        self.operation = ""

        self.previous_operand_lbl.configure(text="1/( " + str(number) + " )")
        self.current_operand_lbl.configure(text=str(self.current_operand))


    def negate(self):

        if self.current_operand == "":
            return

        self.current_operand = self.strip_zero(-float(self.current_operand))
        self.update_display()


    def compute(self):

        if self.current_operand == "":
            return

        computation = 0

        if self.previous_operand == "":
            pass
        else:
            prev = float(self.previous_operand)

        current = float(self.current_operand)

        if self.operation == "+":
            computation = prev + current
        elif self.operation == "-":
            computation = prev - current
        elif self.operation == "*":
            computation = prev * current
        elif self.operation == "÷":
            computation = prev / current

        elif self.operation == "√":
            computation = math.sqrt(current)
        elif self.operation == "x²":
            computation = current ** 2
        elif self.operation == "1/x":
            computation = 1/current
        elif self.operation == "%":
            computation = current / 100


        self.current_operand = self.strip_zero(computation)
        self.operation = ""
        self.previous_operand = ""
        self.update_display()


    def strip_zero(self, num):
        string = str(num)               # strips the .0 from the
        if string[-2:] == ".0":
            return string[0:-2]
        else:
            return num



    def update_display(self):

        if self.current_operand != "":
            if self.get_num_of_digits_after_decimal(self.current_operand) > 14:
                num = round(float(self.current_operand), 12)
                self.current_operand_lbl.configure(text=num)
            else:
                self.current_operand_lbl.configure(text=self.current_operand)
        else:
            self.current_operand_lbl.configure(text=self.current_operand)

        if self.operation != "":
            self.previous_operand_lbl.configure(text=str(self.previous_operand) + " " + self.operation)
        else:
            self.previous_operand_lbl.configure(text=self.previous_operand)



    def get_num_of_digits_after_decimal(self, x):
        s = str(x)
        if not '.' in s:
            return 0
        return len(s) - s.index('.') - 1


    # First Row

    def plus_minus_btn_change_bg_color(self, e):
        self.plus_minus_btn.config(bg='grey')

    def plus_minus_btn_change_bg_color_back(self, e):
        self.plus_minus_btn.config(bg='#060606')

    def num_zero_btn_change_bg_color(self, e):
        self.num_zero_btn.config(bg='grey')

    def num_zero_btn_change_bg_color_back(self, e):
        self.num_zero_btn.config(bg='#060606')

    def decimal_btn_change_bg_color(self, e):
        self.decimal_btn.config(bg='grey')

    def decimal_btn_change_bg_color_back(self, e):
        self.decimal_btn.config(bg='#060606')

    def equals_btn_change_bg_color(self, e):
        self.equals_btn.config(bg='#2888d7')

    def equals_btn_change_bg_color_back(self, e):
        self.equals_btn.config(bg='#134369')


    #Second Row Mouse Events

    def num_one_btn_change_bg_color(self, e):
        self.num_one_btn.config(bg='grey')

    def num_one_btn_change_bg_color_back(self, e):
        self.num_one_btn.config(bg='#060606')

    def num_two_btn_change_bg_color(self, e):
        self.num_two_btn.config(bg='grey')

    def num_two_btn_change_bg_color_back(self, e):
        self.num_two_btn.config(bg='#060606')

    def num_three_btn_change_bg_color(self, e):
        self.num_three_btn.config(bg='grey')

    def num_three_btn_change_bg_color_back(self, e):
        self.num_three_btn.config(bg='#060606')

    def plus_btn_change_bg_color(self, e):
        self.plus_btn.config(bg='grey')

    def plus_btn_change_bg_color_back(self, e):
        self.plus_btn.config(bg='#131313')


    # Third Row Mouse Events

    def num_four_btn_change_bg_color(self, e):
        self.num_four_btn.config(bg='grey')

    def num_four_btn_change_bg_color_back(self, e):
        self.num_four_btn.config(bg='#060606')

    def num_five_btn_change_bg_color(self, e):
        self.num_five_btn.config(bg='grey')

    def num_five_btn_change_bg_color_back(self, e):
        self.num_five_btn.config(bg='#060606')

    def num_six_btn_change_bg_color(self, e):
        self.num_six_btn.config(bg='grey')

    def num_six_btn_change_bg_color_back(self, e):
        self.num_six_btn.config(bg='#060606')

    def minus_btn_change_bg_color(self, e):
        self.minus_btn.config(bg='grey')

    def minus_btn_change_bg_color_back(self, e):
        self.minus_btn.config(bg='#131313')


    # Fifth Row Mouse Events

    def num_seven_btn_change_bg_color(self, e):
        self.num_seven_btn.config(bg='grey')

    def num_seven_btn_change_bg_color_back(self, e):
        self.num_seven_btn.config(bg='#060606')

    def num_eight_btn_change_bg_color(self, e):
        self.num_eight_btn.config(bg='grey')

    def num_eight_btn_change_bg_color_back(self, e):
        self.num_eight_btn.config(bg='#060606')

    def num_nine_btn_change_bg_color(self, e):
        self.num_nine_btn.config(bg='grey')

    def num_nine_btn_change_bg_color_back(self, e):
        self.num_nine_btn.config(bg='#060606')

    def multiply_btn_change_bg_color(self, e):
        self.multiply_btn.config(bg='grey')

    def multiply_btn_change_bg_color_back(self, e):
        self.multiply_btn.config(bg='#131313')


    # Fifth Row Mouse Events

    def inverse_btn_change_bg_color(self, e):
        self.inverse_btn.config(bg='grey')

    def inverse_btn_change_bg_color_back(self, e):
        self.inverse_btn.config(bg='#131313')

    def square_btn_change_bg_color(self, e):
        self.square_btn.config(bg='grey')

    def square_btn_change_bg_color_back(self, e):
        self.square_btn.config(bg='#131313')

    def square_root_btn_change_bg_color(self, e):
        self.square_root_btn.config(bg='grey')

    def square_root_btn_change_bg_color_back(self, e):
        self.square_root_btn.config(bg='#131313')

    def division_btn_change_bg_color(self, e):
        self.division_btn.config(bg='grey')

    def division_btn_change_bg_color_back(self, e):
        self.division_btn.config(bg='#131313')


    # Sixth Row Mouse Events

    def percent_btn_change_bg_color(self, e):
        self.percent_btn.config(bg='grey')

    def percent_btn_change_bg_color_back(self, e):
        self.percent_btn.config(bg='#131313')

    def clear_entry_btn_change_bg_color(self, e):
        self.clear_entry_btn.config(bg='grey')

    def clear_entry_btn_change_bg_color_back(self, e):
        self.clear_entry_btn.config(bg='#131313')

    def clear_btn_change_bg_color(self, e):
        self.clear_btn.config(bg='grey')

    def clear_btn_change_bg_color_back(self, e):
        self.clear_btn.config(bg='#131313')

    def backspace_btn_change_bg_color(self, e):
        self.backspace_btn.config(bg='grey')

    def backspace_btn_change_bg_color_back(self, e):
        self.backspace_btn.config(bg='#131313')


root = Tk()
WindowsCalculator(root)
root.mainloop()
