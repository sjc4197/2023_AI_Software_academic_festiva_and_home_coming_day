import tkinter as tk
from tkinter import messagebox
from random import randint

class RandomNumberGenerator:
    def __init__(self):
        self.generated_numbers = set()

    def generate_random_number(self, max_number):
        available_numbers = set(range(1, max_number + 1)) - self.generated_numbers
        if not available_numbers:
            raise ValueError("더 이상 사용 가능한 숫자가 없습니다.")

        random_number = randint(1, max_number)
        while random_number not in available_numbers:
            random_number = randint(1, max_number)

        self.generated_numbers.add(random_number)
        return random_number

root = tk.Tk()
root.title("AI소프트웨어학과 경품 추첨기")

root.geometry("1000x300")

rng = RandomNumberGenerator()

label_max_number = tk.Label(root, text="최대 숫자:")
label_max_number.pack()

entry_max_number = tk.Entry(root)
entry_max_number.pack()

bottom_space_label = tk.Label(root, text="")
bottom_space_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 120))
result_label.pack()

def on_generate_button_click():
    try:
        max_number = int(entry_max_number.get())
        if max_number < 1:
            raise ValueError("최대 숫자는 1 이상이어야 합니다.")
        
        random_number = rng.generate_random_number(max_number)
        result_label.config(text=f"당첨 번호 : {random_number}")
    except ValueError as e:
        messagebox.showerror("에러", str(e))

generate_button = tk.Button(root, text="랜덤 숫자 생성", command=on_generate_button_click)
generate_button.pack()

root.mainloop()