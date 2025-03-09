import time 
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def unmute_all_chrome_windows():
    """解除所有 Chrome 窗口的静音"""
    sessions = AudioUtilities.GetAllSessions()
    muted_count = 0
    for session in sessions:
        if session.Process and "chrome" in session.Process.name().lower():
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            volume.SetMute(0, None)  # 0 = unmute
            muted_count += 1
    if muted_count > 0:
        print(f"Unmuted {muted_count} Chrome window(s) via pycaw")
    else:
        print("No muted Chrome windows found")
    time.sleep(3)
    return muted_count > 0

if __name__ == "__main__":
    unmute_all_chrome_windows()