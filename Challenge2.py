#matric 1723387
#Billah Syed Mashkur
#Challenge 2
#Challenge 1 Topic -> State Machine of a Vending Machine
#Individual Assignment

from automata.fa.dfa import DFA 

dfa = DFA (
    #Here I am representing the states 
    states = {'st1','st2','st3','st4(trap)','st5','st6','st7','st8','st9(cancel)'},
    #these are my input signs 0=False, 1=True
    input_symbols= {'0','1'},
    
    #Let the transitions begin
    transitions = {
        
        'st1':{'0':'st9(cancel)','1':'st2'}, #st1 is the initial state from where we start
        
        'st9(cancel)':{'0':'st1','1':'st1'}, #st9(cancel) is the cancel state where it cancels the operation when the vending machine is totally empty and goes back to the first state. This is also a final state.
        
        'st2':{'0':'st2','1':'st3'}, # here st2 is the state where the money is inserted
        
        'st3':{'0':'st4(trap)','1':'st5'}, # st3 is the state called validate money where if it is true then it goes to item selection(st5) or if it is false then it goes to eject money state(st4) which is trap state
        
        # trap state
        'st4(trap)':{'0':'st4(trap)','1':'st4(trap)'},
        
        'st5':{'0':'st5','1':'st6'}, # st5 is the state selection of item. If its true then it checks the amount of money which is st6
        
        'st6':{'0':'st5','1':'st7'}, # st6 is the state to check the amount of money. If its true then it proceeds to next state otherwise it goes back to the st5 to select item again.
         
        'st7':{'0':'st5','1':'st8'}, # st7 is the checking availability state. If the item is available then it drops the item which is st8 or final state otherwise it goes back to the st5 to select item again.
         
        'st8':{'0':'st1','1':'st1'}, # st8 is the state where it drops the item and finishes the procedure
        
        
        
        
    },
   initial_state = 'st1',
   final_states ={'st8','st9(cancel)'}

)


# Testing phase...
# U can try many examples you want
if (dfa.accepts_input('1011111')): # here I am testing string '1011111' which will be accepted but if we try '1110' then it will be rejected
    print("Accepted")
    
else:
    print("Rejected")
