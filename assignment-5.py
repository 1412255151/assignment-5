class SquareSumCalculator:
    def __init__(self):
        self.total_sum = 0
    def add_square(self, num):
        square = num ** 2
        self.total_sum += square
    def get_total(self):
        return self.total_sum
calculator = SquareSumCalculator()
numbers_input = input("Enter a list of numbers = ")
numbers = [int(num.strip()) for num in numbers_input.split(',')]
for number in numbers:
    calculator.add_square(number)
total_sum_of_squares = calculator.get_total()
print(f"Sum of squares: {total_sum_of_squares}")