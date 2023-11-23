import tkinter as tk
from tkinter import messagebox
from random import randint

class RandomNumberGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("AI소프트웨어학과 경품 추첨기")
        self.master.geometry("1000x300")

        # GUI 요소 초기화
        self.init_gui()

        # RandomNumberGenerator 인스턴스 생성
        self.rng = RandomNumberGenerator()

    def init_gui(self):
        self.label_max_number = tk.Label(self.master, text="최대 숫자:")
        self.label_max_number.pack()

        self.entry_max_number = tk.Entry(self.master)
        self.entry_max_number.pack()

        self.bottom_space_label = tk.Label(self.master, text="")
        self.bottom_space_label.pack()

        self.result_label = tk.Label(self.master, text="", font=("Helvetica", 120))
        self.result_label.pack()

        self.generate_button = tk.Button(self.master, text="랜덤 숫자 생성", command=self.on_generate_button_click)
        self.generate_button.pack()

    def on_generate_button_click(self):
        try:
            max_number = int(self.entry_max_number.get())
            if max_number < 1:
                raise ValueError("최대 숫자는 1 이상이어야 합니다.")

            random_number = self.rng.generate_random_number(max_number)
            self.result_label.config(text=f"당첨 번호 : {random_number}")
        except ValueError as e:
            messagebox.showerror("에러", str(e))

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

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberGeneratorApp(root)
    root.mainloop()
