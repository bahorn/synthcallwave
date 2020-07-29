# synthcall wave

what if we made music based on what syscalls are running on our system

## Usage

* Install [bpftrace](https://github.com/iovisor/bpftrace)
* Setup the virtual enviroment:
  * virtualenv -p python3 .venv
  * source .venv/bin/activate
  * pip install -r requirements.txt
* Setup a midi synthesizer
  * I used fluidsynth.
  * Follow this [guide](https://wiki.archlinux.org/index.php/FluidSynth) and get it into ALSA daemon mode.
* `sudo ./get_syscalls.bt | python ./synthcall.py`
* If the music does not stop, run `python ./stop.py`
