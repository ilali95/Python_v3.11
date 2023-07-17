import csv

def solve_quadratic_equation_with_csv(func):

    def wrapper(filename):
        
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                numbers = [float(num) for num in row]
                result = func(*numbers)
                print(f"Input: {numbers} - Roots: {result}")

    return wrapper