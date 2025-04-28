#first import NPDA
from automata.pda.npda import NPDA

# NPDA which matches palindromes consisting of 'a's and 'b's
# (accepting by final state)
# this is the template from website given in the assignment automata.pda.npda.NPDA.

# for q3a
def q3a():
    npda = NPDA(
        # q0 reads the first half , q1 the other half, q2 accepts state.
        states={'q0', 'q1', 'q2'},
        # input A and B
        input_symbols={'a', 'b'}, 
        # A for input a, B for input b, and "#" for the initial state
        stack_symbols={'A', 'B', '#'}, 

        # for transitions
        transitions={
            #for state q0
            'q0': {
                # when input a is read
                # when it is # which is the initial state and a is read,push A to the stack
                # when it is A  and a is read,push A to the stack as well
                'a': {
                    '#': {('q0', ('A', '#'))},  
                    'A': {('q0', ('A', 'A'))},  
                },

                # when input b is read and 'A' change state into q1 and pop 'A'
                # e.g AAAB ---> AAB ---> AB etc.
                'b': {
                    'A': {('q1', '')}  # Pop 'A' from stack when reading 'b' and move to q1
                }
            },

            # for state q1
            'q1': {
                # when input b is read and is 'A' so keep state in q1 continue popping A
                # e.g AAAB ---> AAB ---> AB etc.  
                'b': {
                    'A': {('q1', '')} 
                },
                # when there is no input which means the stack is empty (every input is read)
                # change state into q2 
                '': {  
                    '#': {('q2', '#')}  # If stack is empty and input is done, accept with '#' at the top
                }
            }
        },
        initial_state='q0', # initial state q0 (first half)
        initial_stack_symbol='#',  # initial stae symbol
        final_states={'q2'}, # accept state
        acceptance_mode='final_state' 
    )
    return npda

#for q3b
def q3b():
    grammar = [
        ('S', ['aSb', 'A']),
        ('A', [''])
    ]
    
    return grammar

