# music_structure-segmentator
A simplification to segment a wav file and get the music form structure.

I was analizing some songs for a personal project and found the [msaf](https://github.com/urinieto/msaf) repository
done by [Oriol Nieto](https://github.com/urinieto). The library seems to be very robust but I needed just a
simple way to give a song and get the boundaries and a simple image.

Here is my simplification (which of course has the original software as dependency),
you just need to specify a path for a wav, and the methods.


change the parameters as you need

Boundary methods: ['example', 'scluster', 'sf', 'vmo', 'olda', 'foote', 'cnmf']
Labeling methods: ['scluster', 'fmc2d', 'vmo', 'cnmf']

audio_file = "path_wav_file.wav"
boundaries_param = "foote"
labels_param = "cnmf"

run like this:
python segmentate.py
