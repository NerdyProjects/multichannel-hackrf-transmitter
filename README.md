# multichannel-hackrf-transmitter

Gnuradio-companion file for a simultaneous, multichannel wideband fm transmitter usable to transmit multiple channels (within the bandwidth of the SDR) at the same time.

### Quickstart
generate some audio files: (32 kHz, 16 bit mono)
```
mpg123 -r32000 -m -s -n 500 -@ http://www.fritz.de/live.m3u > stream1.fifo
mpg123 -r32000 -m -s -n 500 -@ http://www.fritz.de/live.m3u > stream2.fifo
mpg123 -r32000 -m -s -n 500 -@ http://www.fritz.de/live.m3u > stream3.fifo
```

Start gnuradio-companion:
```
gnuradio-companion fm-tx.grc
```

Press the play button.

In the GUI, you can set frequency, for first stream and offsets for second/third stream.

Transmit gain of HackRF can be 0 or +14 dB via RF power and 0dB to 47 dB in 1 dB steps via IF gain. Total output power is in the range of 10 dBm maximum.


### Liability

Transmitting with any SDR is most likely forbidden in most areas of the world. Only operate your SDR with a dummy load for testing purposes, never use this with a real antenna!


### Modifications

The gnuradio flowchart and the settings are highly experimental and for testing. Real world UKW radios operate using slightly different parameters, e.g. most important 75 kHz modulation deviation. Also, the different sample rates might be not optimized.
