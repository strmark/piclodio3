import alsaaudio


class SoundManager(object):

    try:
        # m = alsaaudio.Mixer()
        # usb device with speaker,  microphone etc more info through alsamixer -c 1 
        m = alsaaudio.Mixer('Speaker', cardindex=1)
    except alsaaudio.ALSAAudioError:
        # no master, we are on a Rpi
        m = alsaaudio.Mixer("PCM")

    @classmethod
    def set_volume(cls, volume_level):
        cls.m.setvolume(int(volume_level))

    @classmethod
    def get_volume(cls):
        vol = cls.m.getvolume()
        return int(vol[0])
