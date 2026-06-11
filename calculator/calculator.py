import tkinter as tk
from tkinter import messagebox

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("390x600")
        self.root.configure(bg="#0b0f17")  
        self.root.resizable(False, False)

        self.expression = ""
        self.history_text = tk.StringVar()
        self.display_text = tk.StringVar()

        # Build UI Elements
        self.create_display()
        self.create_buttons()

    def create_display(self):
        """Creates a modern dual-line stacked readout screen"""
        display_frame = tk.Frame(self.root, bg="#111827", bd=0, highlightthickness=1, highlightbackground="#1f2937")
        display_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx=16, pady=(20, 10))

        
        history_label = tk.Label(
            display_frame, 
            textvariable=self.history_text, 
            font=("Helvetica", 14), 
            bg="#111827", 
            fg="#6b7280",  
            anchor="e", 
            padx=16,
            pady=4
        )
        history_label.pack(fill=tk.X)
        self.history_text.set("")

       
        display_label = tk.Label(
            display_frame, 
            textvariable=self.display_text, 
            font=("Consolas", 32, "bold"), 
            bg="#111827", 
            fg="#06b6d4", 
            anchor="e", 
            padx=16,
            pady=10
        )
        display_label.pack(fill=tk.X)
        self.display_text.set("0")

    def format_large_number(self, val_str):
        """Formats limit numbers into E scientific notation if they exceed length constraints"""
        try:
            
            clean_str = val_str.replace('^', '').replace('\\', '')
            if not clean_str.replace('.','',1).isdigit():
                return val_str
                
            num = float(val_str)
            # If length exceeds 11 digits or integer is massive, convert to exponential notation
            if len(val_str) > 11 or num >= 1e11:
                formatted = f"{num:.4E}"
                # Format to normal standard calculator style: replace E+0X with E...
                return formatted.replace("E+", "E")
            return val_str
        except ValueError:
            return val_str

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#0b0f17")
        button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=14, pady=(0, 16))

        
        button_layout = [
            ['C', '^', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '\\', '=']
        ]

        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.columnconfigure(j, weight=1)

        for row_idx, row in enumerate(button_layout):
            for col_idx, char in enumerate(row):
                
                if char == '=':
                    bg_color = "#d946ef"  
                    fg_color = "#ffffff"
                    active_bg = "#f472b6"
                elif char in ['C', '^', '%', '/', '*', '-', '+', '\\']:
                    bg_color = "#1f2937"  
                    fg_color = "#38bdf8"  
                    active_bg = "#374151"
                else:
                    bg_color = "#141b2b" 
                    fg_color = "#f3f4f6" 
                    active_bg = "#1e293b"

                btn = tk.Button(
                    button_frame, 
                    text=char, 
                    font=("Helvetica", 18, "bold"),
                    bg=bg_color, 
                    fg=fg_color, 
                    activebackground=active_bg,
                    activeforeground=fg_color,
                    bd=0, 
                    relief="flat",
                    command=lambda x=char: self.on_button_click(x)
                )
                btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=4, pady=4)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.history_text.set("")
            self.display_text.set("0")
        
        elif char == '=':
            try:
                if not self.expression:
                    return
                
                
                self.history_text.set(self.expression + " =")
                
             
                expr_to_eval = self.expression.replace('^', '**').replace('\\', '//')
                result = eval(expr_to_eval)
                
               
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                
               
                final_output = self.format_large_number(str(result))
                
                self.display_text.set(final_output)
                self.expression = str(result)  
                
            except ZeroDivisionError:
                messagebox.showerror("Math Error", "Cannot divide by zero")
                self.expression = ""
                self.display_text.set("0")
                self.history_text.set("")
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.display_text.set("0")
                self.history_text.set("")
                
        else:
            
            if self.display_text.get() == "0" and char not in ['^', '%', '/', '*', '-', '+', '\\']:
                self.expression = char
            else:
                self.expression += char
            
           
            active_view = self.format_large_number(self.expression)
            self.display_text.set(active_view)

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()