import tkinter as tk
git add .
git commit -m "Added requirements.txt"
git push

# Button layout
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "✔", "="]
]

right_symbols = ["÷", "x", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

# Colors
color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

# Main window
window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tk.Frame(window)
frame.pack()

# Display
display = tk.Entry(frame, font=("Arial", 24), borderwidth=0,
                   justify="right", bg=color_black, fg=color_white)
display.grid(row=0, column=0, columnspan=4, sticky="nsew", ipady=20)

# Function to handle button clicks
def on_button_click(value):
    current = display.get()

    if value == "AC":
        display.delete(0, tk.END)

    elif value == "=" or value == "✔":
        try:
            # Replace symbols for evaluation
            expression = current.replace("x", "*").replace("÷", "/")
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif value == "+/-":
        try:
            if current:
                if current[0] == "-":
                    display.delete(0)
                else:
                    display.insert(0, "-")
        except:
            pass

    elif value == "%":
        try:
            result = float(current) / 100
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            pass

    else:
        display.insert(tk.END, value)

# Create buttons
for row in range(len(button_values)):
    for col in range(len(button_values[row])):
        value = button_values[row][col]

        # Button color logic
        if value in top_symbols:
            bg_color = color_light_gray
            fg_color = color_black
        elif value in right_symbols:
            bg_color = color_orange
            fg_color = color_white
        else:
            bg_color = color_dark_gray
            fg_color = color_white

        button = tk.Button(
            frame,
            text=value,
            font=("Arial", 18),
            bg=bg_color,
            fg=fg_color,
            borderwidth=0,
            command=lambda v=value: on_button_click(v)
        )

        button.grid(row=row + 1, column=col, sticky="nsew", ipadx=20, ipady=20)

# Make grid responsive
for i in range(5):
    frame.rowconfigure(i, weight=1)

for j in range(4):
    frame.columnconfigure(j, weight=1)

window.mainloop()
