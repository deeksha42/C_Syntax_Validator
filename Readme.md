# Simple C Language Syntax Validator using Lexer and Parser in Python

## Project Overview

This project implements a simple lexer and parser for a C programming language using Python and the PLY (Python Lex-Yacc) library. The lexer and parser are designed to process and validate the syntax of basic C language constructs, including variable declarations, assignments, control flow statements (`if`, `while`, `for`, etc.), and `struct` definitions.

The project includes:

- A **lexer** that tokenizes the input source code into a series of meaningful tokens.
- A **parser** that interprets the sequence of tokens based on the grammar rules to verify syntactical correctness.

## Features

- **Lexical Analysis**: Breaks down the source code into tokens such as keywords, identifiers, operators, and more.
- **Syntax Analysis**: Validates the sequence of tokens against predefined grammar rules to ensure proper code structure.
- **Support for Basic C Constructs**: Handles common C language features such as variable declarations, loops, conditional statements, and structures.

## Concepts

### Lexer

The lexer (lexical analyzer) reads the input source code and converts it into a sequence of tokens. Each token represents a basic language construct, such as a keyword, identifier, operator, or punctuation mark. The lexer uses regular expressions to match patterns in the code and categorize them into different token types.

### Parser

The parser (syntactical analyzer) processes the tokens generated by the lexer. It applies a set of grammar rules to ensure that the token sequence forms a valid syntactical structure according to the rules of the C language. The parser can detect syntax errors and report them.

## Project Structure

```
├── lexer.py          # Contains the implementation of the lexer
├── parser1.py        # Contains the implementation of the parser
├── input.txt         # The input file containing the source code to be parsed
├── invalid.txt       # File containing examples of constructs with syntax errors
├── valid.txt         # File containing examples of constructs without syntax errors
└── main.py           # The main script to run the lexer and parser on the input file
```

## How to Use

### Prerequisites

- Python 3.x
- PLY library (Python Lex-Yacc)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/deeksha42/C_Syntax_Validator.git
   cd your-repo-name
   ```

2. **Install PLY**

   If you haven't installed PLY, you can do so using pip:

   ```bash
   pip install ply
   ```

### Running the Lexer and Parser

1. **Prepare the Input File**:

   - Edit the `input.txt` file and write the C code that you want to parse.

2. **Run the Main Script**:

   - Execute the `main.py` script to run the lexer and parser on your input file:

   ```bash
   python main.py
   ```

3. **View the Output**:

   - The script will print the contents of the input file and display messages indicating the parsing process, including any syntax errors detected.
