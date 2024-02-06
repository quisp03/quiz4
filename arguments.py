import argparse

parser = argparse.ArgumentParser()
parser.add_argument('string', type = str, help = 'Input string')
parser.add_argument('integer', type = int, help = 'Input integer')
parser.add_argument('num_float', type = float, help = 'Input float')

args = parser.parse_args()

my_strings = args.string
my_integers = args.integer
my_floats = args.num_float

print("String:", my_strings)
print("Integer:", my_integers)
print("Float:", my_floats)