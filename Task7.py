def move(subject, start, end):
    
    return f"Move {subject} from {start} to {end}"

def push_box(start, end):
   
    return f"Push box from {start} to {end}"

def climb_on_box(location):
    
    return f"Climb on the box at {location}"

def grab_banana(location):

    return f"Grab the banana at {location}"

def plan_actions(initial_state):

    state = initial_state.copy()
    actions = []
    if state['monkey_at'] != state['box_at']:
        actions.append(move('Monkey', state['monkey_at'], state['box_at']))
        state['monkey_at'] = state['box_at']

    if state['box_at'] != state['banana_at']:
        actions.append(push_box(state['box_at'], state['banana_at']))
        state['monkey_at'] = state['banana_at']
        state['box_at'] = state['banana_at']

    if not state['monkey_on_box']:
        actions.append(climb_on_box(state['box_at']))
        state['monkey_on_box'] = True

    if state['monkey_on_box'] and state['monkey_at'] == state['banana_at']:
        actions.append(grab_banana(state['banana_at']))
    else:
        return ["Planning failed due to an unexpected state."]

    return actions
initial_state = {
    'monkey_at': 0,     
    'box_at': 2,         
    'banana_at': 1,      
    'monkey_on_box': False 
}

correct_actions = plan_actions(initial_state)

print("--- Monkey and Banana Plan ---")
if correct_actions:
    for i, action in enumerate(correct_actions, 1):
        print(f"Step {i}: {action}")
else:
    print("No plan could be generated.")
