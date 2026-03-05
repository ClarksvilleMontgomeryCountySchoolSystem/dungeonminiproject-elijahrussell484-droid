torch_lit = True
if not torch_lit:
    outcome = "Doom: You walk around in the darkness and fall in a pit filled with spikes."
else:
    outcome = "Flicker: You walk arounnd with a light to guide your way and avoid a pit filled with spikes until you get to a locked door."
print(outcome)