import fileinput

import mido
import math

port = mido.open_output('FLUID Synth (3589726):Synth input port (3589726:0) 128:0')


def play(f):
    messages = []

    total = sum(map(lambda x: x[1], list(f.items())))
    print(total)

    for syscall, count in f.items():
        note = int((((syscall+10) % 512)/512)*127)
        time = math.log(count + 2, 1.5) / 1000
        velocity = 127-int((count/total)*note)
        messages.append(mido.Message(
            'note_on', note=note, time=time, velocity=velocity
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
