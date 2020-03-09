# DN-780R-Interface
 A Python library for serial control of the Denon DN-780R cassette recorder


## Functions
### `__init__`
Accepts a serial port as a string and opens the connection with a baud of 9600, even parity, and runs `all_stat`.

### `reset`
Performs a soft reset on the recorder.

### `all_stat`
Runs `status`, `tape_stat`, and `established`

### `status`
Gets current system status from recorder.
* `a_stat` Byte.
* `b_stat` Byte.
  * 'A' No tape
  * 'B' Stop
  * 'C' Play
  * 'D' Record Pause
  * 'E' Record
  * 'F' Record Mute
  * 'G' Fast Forward
  * 'H' Rewind
  * 'I' Cue
  * 'J' Review
  * 'K' Play Mute
* `highspeed` Boolean. 'True' if set to high-speed mode, 'False' if not
* `counter_a` Integer. Current counter value for mecha A
* `counter_b` Integer. Current counter value for mecha B
* `sys_status` Integer.

### `cpu_vers`
Returns CPU version in the format of a 4-digit string.

### `tape_stat`
Gets current recordability of tapes in both mechas.
* `a_stat` Same as above
* `b_stat` Same as above
* `reca_a` Boolean. True if mecha A side A is recordable
* `reca_b` Boolean. True if mecha A side B is recordable
* `recb_a` Boolean. True if mecha B side A is recordable
* `recb_a` Boolean. True if mecha B side B is recordable

### `established`
Return hardware settings.
* `dup` Integer. Duplication status, 0 if off, 1 if slave, and 2 if master
* `rev` Integer. Reverse status, 0 if single, 1 if loop, 2 if relay, 3 if cascade
* `dolbya` Integer. Mecha A Dolby Noise Reduction. 0 if off, 1 if type B, 2 if type C
* `dira` Boolean. Mecha A play/rec direction. True if forward, False if reverse
* `mema` Boolean. Mecha A memory. True if on, False if off
* `dolbyb` Integer. Mecha A Dolby Noise Reduction. 0 if off, 1 if type B, 2 if type C
* `dirb` Boolean. Mecha A play/rec direction. True if forward (right), False if reverse (left)
* `memb` Boolean. Mecha A memory. True if on, False if off

*Note, direction might be different from panel switch if changed via command*

### `id`
Returns recorder model as a string.

### `play`
Accepts a string indicating which mecha, 'A' or 'B', and sets that mecha to play (or record if that is active).

### `stop`
Accepts a string indicating which mecha, 'A' or 'B', and sets that mecha to stop.

### `rec`
Accepts a string indicating which mecha, 'A' or 'B', and sets that mecha to record.
* Sets to recording standby if mecha status is stop
* Makes a 5sec muted recording if mecha status is record

### `pause_rec`
Accepts a string indicating which mecha, 'A' or 'B', and sets that mecha to paused record.

### `forward`
Accepts a string indicating which mecha, 'A' or 'B', and a boolean indicating if music search is to be used and sets the mecha to fast-forward.

### `rewind`
Accepts a string indicating which mecha, 'A' or 'B', and a boolean indicating if music search is to be used and sets the mecha to rewind.

### `direction`
Accepts a string indicating which mecha, 'A' or 'B', and toggles the direction of that mecha.

### `close`
Ends serial connection to recorder.
