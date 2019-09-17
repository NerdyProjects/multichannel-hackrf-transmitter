# Goal
Have an application being able to transmit N channels (N configurable at configuration/application start time or fixed to >=4) of audio on hackrf.
FM channels need to be settable at run time (or at least configuration time).
The convered FM bandwidth needs to be at least 4 MHz (so ~40 possible channels with 200kHz spacing)

# Missing pieces
* Jack input to Gnuradio including resampling: Current jack input is broken for multiple channels (Really? Try first) and does not provide adaptive resampling. Use zita-resampler (and examples by zita-a2j/j2a) to implement a gnuradio jack source that actually works and provides adaptive resampling to link soundcard to sdr.
* Low latency: libhackrf/osmosdr use quite a big buffer size (15x256k), which is 15 blocks of 32ms of IQ samples at ~4 MSps, leading to a minimum delay of ~2 buffer sizes (~64 ms?) or max. 480ms in total. There is (outdated) patches to reduce those by a factor of 16 for ~4ms per buffer or ~62ms in total. Writing down these numbers, I don't feel we would need to act on the buffer size. Let's keep this as a last step
* Control some parameters: XMLRPC Server seems really easy, e.g. usable from python or through other XMLRPC libraries. Allows access to variables and a bit more. By controlling the synthesizers' channel map as well as the SDR tuning frequency, it is very easy to dynamically change all frequencies.

