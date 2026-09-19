import keyboard
from pycaw.pycaw import AudioUtilities

def main ():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == "chrome.exe":
            if muted:
                volume.SetMute(0, None)
            else:
                volume.SetMute(1, None)

muted = False
while True:
    keyboard.wait('insert')
    main()
    muted = not muted
