import tkinter as tk
import time


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.text_area = tk.Text(root, height=10, width=50)
        self.text_area.pack(pady=20)
        # Added a keypress event to start the timer
        self.text_area.bind('<KeyPress>', self.start_timer)

        self.time_label = tk.Label(root, text="Time: 0s")
        self.time_label.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_test, width=10)
        self.reset_button.pack(padx=5, pady=5)

        # Added a keypress event to stop the timer
        self.start_time = None
        self.end_time = None
        self.typing_started = False


    def start_timer(self, event):
        if not self.typing_started:
            self.start_time = time.time()
            self.typing_started = True
            self.update_timer()


    def update_timer(self):
        if self.typing_started:
            elapsed_time = int(time.time() - self.start_time)
            self.time_label.config(text=f"Time: {elapsed_time}s")
            self.root.after(1000, self.update_timer)


    # Added a method to calculate the typing speed in terms of Words Per Minut (WPM)
    def calculate_wpm(self):
        typed_text = self.text_area.get("1.0", tk.END)
        words = typed_text.split()
        num_words = len(words)
        elapsed_time = time.time() - self.start_time
        wpm = (num_words / elapsed_time) * 60
        return round(wpm, 2)


    def reset_test(self):
        self.typing_started = False
        self.text_area.delete("1.0", tk.END)
        self.time_label.config(text="Time: 0s")
        self.result_label.config(text="")
        self.start_time = None
        self.end_time = None


    # Added a method to stop the timer and display the typing speed
    def stop_timer(self):
        self.end_time = time.time()
        wpm = self.calculate_wpm()
        self.result_label.config(text=f"Your typing speed is {wpm} Words Per Minute")
        self.typing_started = False


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)

    # Added a button to stop the test
    stop_button = tk.Button(root, text="Stop", command=app.stop_timer, width=10)
    stop_button.pack(padx=5, pady=5)
    
    root.mainloop()
