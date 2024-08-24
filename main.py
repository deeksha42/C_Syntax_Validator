from lexer import lexer
from parser1 import parser


try:
    with open("input.txt", "r") as file: #give your filename
        data = file.read()
        print("File Content:")
        print(data)
        parser.parse(data, lexer=lexer)
    
except Exception as e:
    print(f"Error during parsing: {e}")
