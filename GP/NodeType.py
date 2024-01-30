from enum import StrEnum, auto


class NodeType(StrEnum):
    program = auto()
    expressions = auto()
    if_statement = auto()
    while_loop = auto()
    wrtie_val = auto()
    read_var = auto()
    assignment = auto()
    bool_value = auto()
    numeric_value = auto()

    LEFTPREN = auto()
    RIGHTPREN = auto()
    LEFTBRACK = auto()
    RIGHTBRACK = auto()

    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()

    ASS = auto()

    EQ = auto()
    NEQ = auto()
    LE = auto()
    LEQ = auto()
    GE = auto()
    GEQ = auto()

    AND = auto()
    OR = auto()
    NOT = auto()

    TRUE = auto()
    FALSE = auto()

    IF = auto()
    WHILE = auto()

    WRITE = auto()
    READ = auto()

    NUMBER = auto()
    NUM_VAR = auto()
    BOOL_VAR = auto()




    terminal = auto()