import tkinter as tk
import random
import time


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.list_of_words = ["fame", "theme", "bargain", "monk", "snuggle", "way", "onion", "patent", "cultivate",
                              "hurl", "mechanism", "referral", "passion", "perceive", "sick", "arrow",
                              "qualification", "guess", "tablet", "discuss", "elect", "citizen", "blind",
                              "accept", "lake", "coach", "earthflax", "grand", "flower", "point", "window",
                              "key", "graphic", "opposed", "product", "recommendation", "late", "elite",
                              "spill", "sketch", "maximum", "replace", "state", "premium", "exact",
                              "linear", "reflect", "new", "recession", "cover", "admit", "federation",
                              "trance", "freshman", "dividend", "discipline", "pledge", "complex",
                              "lung", "thrust", "stroke", "lane", "plot", "particular", "Sunday",
                              "straw", "bake", "professional", "trace", "settle", "flour", "justice",
                              "shape", "graduate", "discover", "rage", "stitch", "pupil", "modest",
                              "agile", "oral", "equation", "mean", "grow", "calorie", "tire", "negative",
                              "reader", "whole", "sheep", "gaffe", "perfume", "deep", "symptom",
                              "budge", "slide", "world", "promote", "golf", "behead", "to", "the"]
        self.create_widgets()
        self.new_test()


    def create_widgets(self):
        self.text_label = tk.Label(self.root, text="Type the following:")
        self.text_label.pack()
        self.text_widget = tk.Text(self.root, height=5, width=50)
        self.text_widget.config(state=tk.DISABLED)  # Make it read-only
        self.text_widget.pack()
        self.entry_label = tk.Label(self.root, text="Type here:")
        self.entry_label.pack()
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack()
        self.entry.bind("<space>", self.check_word)
        self.start_button = tk.Button(self.root, text="Start Typing Test", command=self.start_test)
        self.start_button.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
        self.timer_label = tk.Label(self.root, text="Time left: 60")
        self.timer_label.pack()


    def generate_sample_text(self):
        # Generate a sample text with random words from the list
        return ' '.join(random.choice(self.list_of_words) for _ in range(20))  # Adjust the number of words as needed


    def new_test(self):
        self.sample_text = self.generate_sample_text()
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, self.sample_text)
        self.text_widget.config(state=tk.DISABLED)
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.current_word_index = 0
        self.correct_words = 0
        self.start_time = None


    def start_test(self):
        self.start_button.config(state=tk.DISABLED)  # Disable the button during the test
        self.entry.focus()  # Focus on the entry widget
        self.start_time = time.time()
        self.update_timer()


    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        remaining_time = int(60 - elapsed_time)
        self.timer_label.config(text=f"Time left: {remaining_time}")
        if remaining_time > 0:
            self.root.after(1000, self.update_timer)
        else:
            self.end_test()


    def check_word(self, event):
        typed_word = self.entry.get().strip()
        sample_words = self.sample_text.split()
        if typed_word == sample_words[self.current_word_index]:
            self.correct_words += 1
        else:
            self.text_widget.tag_add("misspelled", f"1.{self.get_word_start_index(self.current_word_index)}", f"1.{self.get_word_end_index(self.current_word_index)}")
            self.text_widget.tag_config("misspelled", foreground="red")
        self.current_word_index += 1
        self.entry.delete(0, tk.END)
        if self.current_word_index >= len(sample_words):
            self.new_test()


    def get_word_start_index(self, index):
        words = self.sample_text.split()
        start_index = sum(len(word) + 1 for word in words[:index])
        return start_index


    def get_word_end_index(self, index):
        words = self.sample_text.split()
        end_index = sum(len(word) + 1 for word in words[:index + 1]) - 1
        return end_index


    def end_test(self):
        self.entry.config(state=tk.DISABLED)  # Disable the entry during result display
        self.result_label.config(text=f"Typing speed: {self.correct_words} WPM")
        self.start_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    typing_speed_test = TypingSpeedTest(root)
    root.mainloop()