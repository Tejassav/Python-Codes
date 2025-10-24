from sys import *


if len(argv) < 2:
    exit("Please provide your name as a command-line argument.")
else:
    print(f'Hello, {argv[1]}, this code is executed in a file called {argv[0]}')