from tkinter import *

def btnClick(numbers):
	global operator
	operator = operator + str(numbers)
	text_input.set(operator)


def  btnClearDisplay():
	global operator
	operator = ""
	text_input.set("")	


def  btnEqualsInput():
	global operator
	sumup = str(eval(operator))
	text_input.set(sumup)
	operator = ""


cal = Tk()
cal.title("Calculator")
operator = ""
text_input = StringVar()
command = lambda:btnClick(8)
txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_input,
                   bd=30, insertwidth=4, bg='powder blue', justify='right').grid(columnspan=4)

btn7 = Button(cal, padx=16, bd=8, pady=16, fg='black', font=('arial', 20, 'bold'), text='7', command = lambda:btnClick(7), bg='powder blue').grid(row=1, column=0)
btn8 = Button(cal, padx=16, bd=8, pady=16, fg='black', font=('arial', 20, 'bold'), text='8', command = lambda:btnClick(8), bg='powder blue').grid(row=1, column=1)
btn9 = Button(cal, padx=16, bd=8, pady=16, fg='black', font=('arial', 20, 'bold'), text='9', command = lambda:btnClick(9), bg='powder blue').grid(row=1, column=2)
addition = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='+', command = lambda:btnClick('+'), bg='powder blue').grid(row=1, column=3)

#==============================================================================================================================

btn4 = Button(cal, padx=16, bd=8, pady=16, fg='black', font=('arial', 20, 'bold'), text='4', command = lambda:btnClick(4), bg='powder blue').grid(row=2, column=0)
btn5 = Button(cal, padx=16, bd=8, pady=16, fg='black', font=('arial', 20, 'bold'), text='5', command = lambda:btnClick(5), bg='powder blue').grid(row=2, column=1)
btn6 = Button(cal, padx=16, bd=8, pady=16, fg='black', font=('arial', 20, 'bold'), text='6', command = lambda:btnClick(6), bg='powder blue').grid(row=2, column=2)
subtraction = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='-', command = lambda:btnClick('-'), bg='powder blue').grid(row=2, column=3)

#==============================================================================================================================

btn1 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='1', command = lambda:btnClick(1), bg='powder blue').grid(row=3, column=0)
btn2 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='2', command = lambda:btnClick(2), bg='powder blue').grid(row=3, column=1)
btn3 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='3', command = lambda:btnClick(3), bg='powder blue').grid(row=3, column=2)
multiplication = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='x',command = lambda:btnClick('*'), bg='powder blue').grid(row=3, column=3)

#==============================================================================================================================

btn0 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='0', command = lambda:btnClick(0), bg='powder blue').grid(row=4, column=0)
btnClear = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='C', command = lambda:btnClearDisplay(), bg='powder blue').grid(row=4, column=1)
btnEquals = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='=', command = lambda:btnEqualsInput(), bg='powder blue').grid(row=4, column=2)
division = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='/', command = lambda:btnClick('/'), bg='powder blue').grid(row=4, column=3)



cal.mainloop()
