'''
from automata.fa.dfa import DFA

dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    input_symbols={'1', '0'},
    transitions={
        'q0': {'1': 'q0', '0': 'q1'},
        'q1': {'1': 'q0', '0': 'q2'},
        'q2': {'0': 'q1', '1': 'q3'},
        'q3': {'1': 'q3', '0': 'q4'},
        'q4': {'1': 'q3', '0': 'q5'},
        'q5': {'0': 'q4', '1': 'q6'},
        'q6': {'0': 'q6', '1': 'q6'},
    },
    initial_state='q0',
    final_states={'q6'}
)

# Visualize and render the DFA
dfa_graph = visualize_dfa(dfa)
dfa_graph.render('dfa_visualization', view=True)  # This will save and display the DFA as a PNG
#display
display(Image(filename='dfa_visualization.png'))
'''

from automata.fa.dfa import DFA

# function for q1a
def q1a():
    dfa = DFA(
        # set 7 states 
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}, 
        # there are two inputs 0 and 1
        input_symbols={'1', '0'},
        transitions={
            # based on the graph i draw
            'q0': {'1': 'q0', '0': 'q1'},
            'q1': {'1': 'q0', '0': 'q2'},
            'q2': {'0': 'q1', '1': 'q3'},
            'q3': {'1': 'q3', '0': 'q4'},
            'q4': {'1': 'q3', '0': 'q5'},
            'q5': {'0': 'q4', '1': 'q6'},
            'q6': {'0': 'q6', '1': 'q6'},
        },
        initial_state='q0',
        final_states={'q5','q6'}
    )
    
    return dfa

#funciton for q1b
def q1b():
    #*: Kleene star operation, language repeated zero or more times. Ex: a*,(ab)*
    #| for union
    #zo = zero + one
    string_zo = "(0|1)*"
    #string for several one
    String_o = "1*"
    #string for a single one
    Separation = "1"
    #separate even zero, when a 1 appears before a zero
    Even_zero = "00(00)*"
    return string_zo + String_o + Even_zero + Separation + string_zo + Even_zero + string_zo 


