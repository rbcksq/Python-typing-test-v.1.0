import time
import random


class TypingTest:

    def __init__(self):
        self.input_text = ''
        self.sentence = ''
        self.time_start = 0
        self.time_stop = 0
        self.time_total = 0
        self.accuracy = 0
        self.results = 'Time: 0, Accuracy: 0, WPM: 0'
        self.file_name = 'text_example.txt'

    def set_sentence(self):
        with open(self.file_name, 'r', encoding='UTF-8') as f:
            example = f.read().split('\n')
        self.sentence = random.choice(example)

    def get_text_from_user(self):
        self.input_text = input('Put down the text:\n').strip()

    def set_time_start(self):
        self.time_start = time.time()

    def set_time_stop(self):
        self.time_stop = time.time()

    def calculate_results(self):
        # Finding total time spent
        self.time_total = self.time_stop - self.time_start

        # Calculating accuracy | If error(not correct char.) or no char. then counter + 0 then next loop
        counter = 0
        for i, char in enumerate(self.sentence):
            try:
                if self.input_text[i] == char:
                    counter += 1
            except:
                pass
        self.accuracy = counter / len(self.sentence) * 100

        # Getting results

        self.results = (f'Time: {round(self.time_total)} s\n'
                        f'Accuracy: {round(self.accuracy)} %\n'
                        f'Quantity of mistakes: {round(len(self.sentence) - counter)}')

    def run(self):
        self.set_sentence()
        print(self.sentence)
        self.set_time_start()
        self.get_text_from_user()
        self.set_time_stop()
        self.calculate_results()
        print(self.results)


if __name__ == "__main__":
    tc = TypingTest()
    tc.run()
