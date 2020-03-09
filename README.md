# DN-780R-Interface
 A Python library for serial control of the Denon DN-780R cassette recorder


## Functions
### `__init__`
Accepts a serial port as a string and opens the connection with a baud of 9600, even parity, and runs `status` and `tape_stat`.

### `reset`
Performs a soft reset on the recorder.

### `status`
Gets current system status from recorder.
* `a_loaded` 'True' if a tape is loaded in mecha A, 'False' if not
* `b_loaded` 'True' if a tape is loaded in mecha B, 'False' if not
* `highspeed` 'True' if set to high-speed mode, 'False' if not
* `counter_a` Current counter value for mecha A
* `counter_b` Current counter value for mecha B

### `cpu_vers`
Returns CPU version in the format of a 4-digit string.

### `tape_stat`
Gets current recordability of tapes in both mechas.
* `a_loaded` Same as above
* `b_loaded` Same as above
* `reca_a` True is mecha A side A is recordable
* `reca_b` True is mecha A side B is recordable
* `recb_a` True is mecha B side A is recordable
* `recb_a` True is mecha B side B is recordable

### `established`
Return hardware settings.
TODO

### `id`
Returns recorder model as a string.

### `play`
Accepts a string indicating which mecha, 'A' or 'B', and sets that mecha to play (or record if that is active).

### `stop`
Accepts a string indicating which mecha, 'A' or 'B', and sets that mecha to stop.

### `close`
Ends serial connection to recorder.
