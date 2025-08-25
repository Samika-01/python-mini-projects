import sounddevice as sd
import wavio as wv

freq = 44100

duration = 5

recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
sd.wait()

wv.write("recording1.wav", recording, freq, sampwidth=2)