from automata.fa.nfa import NFA
from automata.fa.dfa import DFA

def q2a():
    return "00010100111110"

# based on the graph A given in the assignment
def dfa_A():
    a = DFA(
        states={'q0', 'q1', 'q2'},
        input_symbols={'1', '0'},
        transitions={
            'q0': {'1': 'q2', '0': 'q1'},
            'q1': {'1': 'q2', '0': 'q0'},
            'q2': {'0': 'q2', '1': 'q2'}
        },
        initial_state='q0',
        final_states={'q2'}
    )
    return a

# based on the graph B given in the assignment

from automata.fa.nfa import NFA
from automata.fa.dfa import DFA

def q2a():
    return "00010100111110"

# based on the graph A given in the assignment
def dfa_A():
    a = DFA(
        states={'q0', 'q1', 'q2'},
        input_symbols={'1', '0'},
        transitions={
            'q0': {'1': 'q2', '0': 'q1'},
            'q1': {'1': 'q2', '0': 'q0'},
            'q2': {'0': 'q2', '1': 'q2'}
        },
        initial_state='q0',
        final_states={'q2'}
    )
    return a

# based on the graph B given in the assignment
def dfa_B():
    b = DFA(
        states={'q3', 'q4', 'q5'},
        input_symbols={'1', '0'},
        transitions={
            'q3': {'1': 'q4', '0': 'q5'},
            'q4': {'1': 'q3', '0': 'q5'},
            'q5': {'0': 'q5', '1': 'q5'}
        },
        initial_state='q3',
        final_states={'q5'}
    )
    return b

def q2b(a, b):
    # method learnt from the given website 
    # https://caleb531.github.io/automata/migration/?h=dfa+nfa#converting-dfa-to-nfa
    # convert dfa to nfa
    # nfa = NFA(dfa)
    # nfa = NFA.from_dfa(dfa)
    # Convert DFA a and b to NFAs
    nfa_A = NFA.from_dfa(a)
    nfa_B = NFA.from_dfa(b)
    
    NFA_q2b = nfa_A.union(nfa_B)
    
    return NFA_q2b
