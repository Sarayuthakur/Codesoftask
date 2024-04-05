import tkinter as tk

class Calcie(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Calculator')

        self.entry_boxA = tk.Entry(self)
        self.entry_boxA.grid(row=0, column=0, padx=10, pady=10)

        self.entry_boxB = tk.Entry(self)
        self.entry_boxB.grid(row=0, column=1, padx=10, pady=10)

        self.ans = tk.StringVar()

        self.label = tk.Label(self, textvariable=self.ans, font=("Arial", 12))
        self.label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.operation_var = tk.StringVar()
        self.operation_var.set('+')

        self.operation_menu = tk.OptionMenu(self, self.operation_var, '+', '-', '*', '/')
        self.operation_menu.grid(row=2, column=0, padx=10, pady=10)

        self.calculate_button = tk.Button(self, text="Calculate", command=self.perform_operation)
        self.calculate_button.grid(row=2, column=1, padx=10, pady=10)

    def perform_operation(self):
        num1 = float(self.entry_box.get())
        num2 = float(self.entry_box2.get())
        operation = self.operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Error! Division by zero is not allowed.'

        self.ans.set(result)

if __name__ == '__main__':
    Calcie = Calcie()
    Calcie.mainloop()