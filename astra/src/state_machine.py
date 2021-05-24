CONTINUE = -1

from abc import abstractmethod
class state:
    @abstractmethod
    def run(self) -> int:
        pass
class state_machine:
    def __init__(self, states: state, start_state = 0, sequential=True):
        if len(states) == 0:
            raise UserWarning("State machine created with 0 states")
        if len(states) < start_state < 0:
            raise ValueError("Cannot create a state machine with start state {start_state}")

        self.states = states
        self.start_state = start_state
        self.transition_table = {i:set([i+1]) for i in range(len(states)-1)} if sequential else {}

    def add_transition(self, start, end):
        self.transition_table.setdefault(start, set([end])).add(end)

    def run(self):
        state = self.states[self.start_state]
        curr = self.start_state
        while 1:
            next_state = state.run()
            if next_state != CONTINUE:
                if next_state in self.transition_table.get(curr):
                    curr = next_state
                    state = self.states[curr]
                else:
                    break