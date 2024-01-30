grammar Expr;

program: expressions*;

//! ----- EXPRESSIONS -----
expressions
    :   if_statement
        | while_loop
        | write_val
        | read_var
        | assignment
    ;

if_statement: IF LEFTPREN bool_value RIGHTPREN block_statement;

while_loop  : WHILE LEFTPREN bool_value RIGHTPREN block_statement;

block_statement : LEFTBRACK expressions* RIGHTBRACK;

write_val
    : WRITE LEFTPREN (numeric_value | bool_value) RIGHTPREN;
    
read_var
    : READ LEFTPREN NUM_VAR  RIGHTPREN
    | READ LEFTPREN BOOL_VAR RIGHTPREN
    ;

assignment
    : NUM_VAR  ASS numeric_value
    | BOOL_VAR ASS bool_value
    ;

bool_value
    : (TRUE | FALSE)                                                
    | BOOL_VAR                                                      
    | NOT bool_value                                                
    | numeric_value (EQ  | NEQ | LE | LEQ | GE | GEQ) numeric_value
    | bool_value (AND | OR) bool_value                              
    | LEFTPREN bool_value RIGHTPREN                                
    ;

numeric_value
    : NUMBER                                                        
    | NUM_VAR                                                      
    | SUB numeric_value                                             
    | numeric_value (MUL | DIV) numeric_value                    
    | numeric_value (ADD | SUB) numeric_value                       
    | LEFTPREN numeric_value RIGHTPREN                              
    ;


WS: [ \t\r\n]+ -> skip;

LEFTPREN: '(';
RIGHTPREN: ')';
LEFTBRACK: '{';
RIGHTBRACK: '}';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

ASS: '=';

EQ: '==';
NEQ: '!=';
LE: '<';
LEQ: '<=';
GE: '>';
GEQ: '>=';

AND: '&&';
OR: '||';
NOT: '!';

TRUE: 'True';
FALSE: 'False';

IF: 'if';
WHILE: 'while';

WRITE: 'write';
READ: 'read';

NUMBER: [0-9]+ ('.' [0-9]+)?;
NUM_VAR: 'X' [0-5];
BOOL_VAR: 'B' [0-5];