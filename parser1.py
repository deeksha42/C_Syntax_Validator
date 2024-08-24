import ply.yacc as yacc
from lexer import tokens, lexer


def p_main(p):
    '''main : Statements'''
    #print("Syntax is Correct.")

def p_Statements(p):
    '''Statements : var_declaration Statements
                  | assignment Statements
                  | while_loop Statements
                  | expression Statements
                  | initialization Statements
                  | do_while_loop Statements
                  | if_else_if_else Statements
                  | for_loop Statements
                  | structure Statements
                  | '''
                      

def p_var_declaration(p):
    '''var_declaration : TYPE list_var SEMI_COLON 
                       | TYPE list_var SEMI_COLON var_declaration'''
    print("Valid declaration.")
    pass
    

def p_list_var(p):
    '''list_var : ID
                | ID COMMA list_var
                '''
    pass
def p_list_var_init(p):
    ''' list_var_init : ID EQUAL expression 
                      | ID EQUAL expression COMMA list_var_init
                      | ID PLUS PLUS
                      | ID MINUS MINUS'''

def p_assignment(p):
    '''assignment : ID EQUAL expression SEMI_COLON
                  | ID EQUAL expression COMMA assignment'''
    print("Valid assignment.")


def p_initialization(p):
    '''initialization : TYPE ID EQUAL expression SEMI_COLON 
                      | TYPE ID EQUAL expression SEMI_COLON initialization
                      | TYPE ID EQUAL expression COMMA list_var_init SEMI_COLON initialization'''
    print("Valid initialization.")
    
                        

def p_while_loop(p):
    'while_loop : WHILE L_PARENTHESIS condition R_PARENTHESIS L_CBRACES Statements R_CBRACES '
    print("Valid while loop.")
   
    
def p_do_while_loop(p):
    'do_while_loop : DO L_CBRACES Statements R_CBRACES WHILE L_PARENTHESIS condition R_PARENTHESIS  SEMI_COLON '
    print("Valid do while loop.")
    

def p_if_else_if(p):
    '''if_else_if_else : IF L_PARENTHESIS condition R_PARENTHESIS L_CBRACES Statements R_CBRACES else_if'''
    print("Valid if else if.")
                 

def p_else_if(p):
    ''' else_if : ELSE IF L_PARENTHESIS condition R_PARENTHESIS L_CBRACES Statements R_CBRACES  else_if
                | ELSE L_CBRACES Statements R_CBRACES
                | '''

def p_for_loop(p):
    ''' for_loop : FOR L_PARENTHESIS initialization  condition SEMI_COLON list_var_init R_PARENTHESIS L_CBRACES Statements R_CBRACES '''

def p_struct(p):
    ''' structure : TYPEDEF STRUCT ID L_CBRACES var_declaration R_CBRACES ID SEMI_COLON 
                  | STRUCT ID  L_CBRACES var_declaration R_CBRACES ID SEMI_COLON 
                  | TYPEDEF STRUCT ID L_CBRACES  initialization  R_CBRACES ID SEMI_COLON  
                  | STRUCT ID  L_CBRACES initialization R_CBRACES ID SEMI_COLON
                  | STRUCT ID  L_CBRACES var_declaration R_CBRACES  SEMI_COLON'''
    print("Valid structure definitiion")

def p_condition(p): 
    '''condition : ID rel ID
                | ID rel NUMBER
                | NUMBER rel NUMBER
                | expression rel expression'''
    print("Valid condition.")
   

def p_rel(p):
    '''rel : GOE 
           | LOE 
           | GREAT 
           | LESS 
           | EQ 
           | NEQ
           '''
    pass

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | expression TIMES term
                  | expression DIVIDE term
                  | expression MOD term
                  | term'''
    pass

def p_term(p):
    '''term : NUMBER
            | ID
            | L_PARENTHESIS expression R_PARENTHESIS
            '''
    pass			



def p_error(p):
    print("Syntax error!")
    #quit()

parser = yacc.yacc()

# added pass to every function
# changed grammar
# added some print statements