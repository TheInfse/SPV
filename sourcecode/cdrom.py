import ctypes
import time

# ctypes.windll.WINMM.mciSendStringW(u"open E: type cdaudio alias e_drive", None, 0, None)
# ctypes.windll.WINMM.mciSendStringW(u"set e_drive door open", None, 0, None)

ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
