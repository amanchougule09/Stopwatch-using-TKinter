import tkinter as tk
import time

# ====== Stopwatch Class ======
class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Stopwatch")
        self.root.geometry("420x350")
        self.root.config(bg="#101820")

        # Variables
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # ====== Title ======
        self.title_label = tk.Label(root, text="Stopwatch",
                                    font=("Segoe UI", 16, "bold"), bg="#101820", fg="#FEE715")
        self.title_label.pack(pady=20)

        # ====== Time Display ======
        self.time_label = tk.Label(root, text="00:00:00", font=("Digital-7", 42, "bold"),
                                   bg="#1B263B", fg="#FEE715", width=10, height=1, relief="flat", bd=4)
        self.time_label.pack(pady=25)

        # ====== Button Frame ======
        self.button_frame = tk.Frame(root, bg="#101820")
        self.button_frame.pack(pady=10)

        # ====== Buttons ======
        self.start_btn = self.create_button("▶ Start", self.start, "#2ECC71")
        self.stop_btn = self.create_button("⏸ Stop", self.stop, "#E74C3C")
        self.reset_btn = self.create_button("🔁 Reset", self.reset, "#3498DB")

        self.start_btn.grid(row=0, column=0, padx=10, ipadx=8, ipady=5)
        self.stop_btn.grid(row=0, column=1, padx=10, ipadx=8, ipady=5)
        self.reset_btn.grid(row=0, column=2, padx=10, ipadx=8, ipady=5)

        # ====== Footer ======
        footer = tk.Label(root, text="Designed by Aman", font=("Segoe UI", 9),
                          bg="#101820", fg="#FEE715")
        footer.pack(side="bottom", pady=10)

    # ====== Custom Button Function ======
    def create_button(self, text, command, color):
        btn = tk.Button(self.button_frame, text=text, command=command,
                        font=("Segoe UI", 11, "bold"), bg=color, fg="white",
                        activebackground="#FEE715", activeforeground="#101820",
                        relief="flat", bd=0, width=9, cursor="hand2")
        btn.bind("<Enter>", lambda e: btn.config(bg="#FEE715", fg="#101820"))
        btn.bind("<Leave>", lambda e: btn.config(bg=color, fg="white"))
        return btn

    # ====== Timer Functions ======
    def update_timer(self):
        if self.running:
            current_time = time.time()
            self.elapsed_time = current_time - self.start_time
            minutes, seconds = divmod(int(self.elapsed_time), 60)
            hours, minutes = divmod(minutes, 60)
            self.time_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.after(1000, self.update_timer)

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_timer()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")


# ====== Run App ======
if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
