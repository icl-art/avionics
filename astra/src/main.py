from external import utime

from state_machine import state, idle

utime.sleep(2)

state = idle()
while state:
    state = state.run()