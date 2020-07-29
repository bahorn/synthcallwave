import fileinput

import mido
import math

port = mido.open_output('FLUID Synth (3589726):Synth input port (3589726:0) 128:0')


def play(f):
    print(f)
    messages = []
    for syscall, count in f.items():
        note = int((((syscall) % 512)/512)*127)
        time = math.log(count + 2, 1.5) / 10
        messages.append(mido.Message(
            'note_on', note=note, time=time, velocity=note
        ))

    for message in messages:
        port.send(message)

batch = {}
for line in fileinput.input():
    if line == '{\n':
        batch = {}
        continue
    if line == '}\n':
        play(batch)
        continue

    try:
        line = line.replace('@syscall[', '')
        line = line.replace(']:', '')
        syscall, count = line.split(' ')
        batch[int(syscall)] = int(count)
    except Exception as err:
        continue
