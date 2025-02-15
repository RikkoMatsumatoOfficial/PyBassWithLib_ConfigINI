import PyBass.bass as x
import configparser as zt
import os
import ctypes
from time import sleep
readc = zt.ConfigParser()
kernel32_dll = ctypes.CDLL("Kernel32.dll")

def GetCurrentDevice_PYBASS():
    return -1
def ReadConfig():
    return readc.read(filenames=os.getcwd() + "\\configur.ini")
def SetConsoleTitle(title : str):
    return kernel32_dll.SetConsoleTitleW(title)
def Main():
    ReadConfig()
    SetConsoleTitle("PyBass_ConfigINI by RikkoMatsumatoOfficial")
    ex_mp3 = readc['Config']['Output']
    x.BASS_INIT(device=-1, freq=48000, flags=0, win=0, dsguid=0)
    x.BASS_START()
    print(ex_mp3)
    bnrb = x.BASS_StreamCreateFile(mem=0, filename=bytes(ex_mp3, "utf-8"), offset=0, length=0, flags=0x4)
    x.BASS_ChannelPlay(bnrb, False)
    while True:
        sleep(4000)

if __name__ == "__main__":
    Main()