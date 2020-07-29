import fileinput

import mido

port = mido.open_output('FLUID Synth (3589726):Synth input port (3589726:0) 128:0')

for i in range(0, 127):
    port.send(
        mido.Message('note_off', note=i)
    )
