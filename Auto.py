import pygetwindow as gw
import pyautogui
import time
import os
# from PIL import Image
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from win32process import GetWindowThreadProcessId

def set_window_state(window_title):
    """将窗口置顶并调整为普通大小"""
    windows = [w for w in gw.getWindowsWithTitle(window_title)]
    if not windows:
        print(f"No window found with title containing '{window_title}'.")
        return None
    
    win = windows[0]
    print(f"Window: title='{win.title}', left={win.left}, top={win.top}, width={win.width}, height={win.height}")
    
    if win.isMinimized:
        win.restore()
    if win.isMaximized:
        win.restore()
    win.activate()
    time.sleep(3) 
    
    win.resizeTo(1280, 720)
    win.moveTo(0, 0)
    print(f"Window adjusted to size (1280, 720) at (0, 0)")

    return win

def locate_image(image_file, region=None, confidence=0.9):
    """查找图像并返回中心坐标"""
    try:
        pos = pyautogui.locateOnScreen(image_file, region=region, confidence=confidence)
        if pos:
            center_x = pos.left + pos.width // 2
            center_y = pos.top + pos.height // 2
            print(f"Found {image_file} at screen ({pos.left}, {pos.top}), center ({center_x}, {center_y})")
            return center_x, center_y, pos.width, pos.height
        return None
    except Exception as e:
        print(f"Error locating {image_file}: {e}")
        return None

def scroll_to_bottom(win):
    """滑动窗口到底部"""
    pyautogui.moveTo(win.left + win.width // 2, win.top + win.height // 2)
    pyautogui.scroll(-10000)
    time.sleep(3) 
    print("Scrolled to bottom")

def scroll_to_top(win):
    """滑动窗口到顶部"""
    pyautogui.moveTo(win.left + win.width // 2, win.top + win.height // 2)
    pyautogui.scroll(10000)  # 正值表示向上滚动
    time.sleep(3) 
    print("Scrolled to top")

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

def mute_chrome_process(win):
    """使用 pycaw 静音 Chrome 进程"""
    if not win:
        print("No current window provided for muting")
        return False
    
    # _, pid = GetWindowThreadProcessId(win._hWnd)
    # print(f"Current window PID: {pid}, Title: {win.title}")

    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and "chrome" in session.Process.name().lower():
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            volume.SetMute(1, None)  # 1 = mute
            print(f"Muted Chrome session with PID {session.Process.pid} (most recent active)")
            time.sleep(3)
            return True
    
    print("No Chrome audio sessions found for muting")
    return False
    # chrome_sessions = []
    # for session in sessions:
    #     if session.Process and "chrome" in session.Process.name().lower():
    #         chrome_sessions.append(session)
    #         print(f"Found Chrome session with PID: {session.Process.pid}")
    
    # if not chrome_sessions:
    #     print("No Chrome audio sessions found")
    #     return False

    # for session in chrome_sessions:
    #     if session.Process.pid == pid:
    #         volume = session._ctl.QueryInterface(ISimpleAudioVolume)
    #         volume.SetMute(1, None)  # 1 = mute
    #         print(f"Muted Chrome window with matching PID {pid}")
    #         time.sleep(3)
    #         return True
        
    # print("No exact PID match found, muting the first Chrome session as fallback")
    # volume = chrome_sessions[0]._ctl.QueryInterface(ISimpleAudioVolume)
    # volume.SetMute(1, None)
    # print(f"Muted Chrome session with PID {chrome_sessions[0].Process.pid} (fallback)")
    # time.sleep(3)
    # return True

def play_and_mute_window(win, region):
    """点击 on.png 播放视频，然后使用 pycaw 静音 Chrome"""
    on_button = os.path.join("loc", "on.png")
    
    # 点击 on.png 播放视频
    on_pos = locate_image(on_button, region)
    if on_pos:
        center_x, center_y, _, _ = on_pos
        pyautogui.click(center_x, center_y)
        print("Clicked on.png to play video")
        # time.sleep(5)  
    else:
        print("on.png not found, skipping play step")
        return False
    
    # 使用 pycaw 静音 Chrome
    if mute_chrome_process(win):
        return True
    return False

def main():
    window_title = "Google Chrome"
    image_dir = "loc"
    yellow_flag = os.path.join(image_dir, "yellow_flag.png")  # 普通标志
    task_com = os.path.join(image_dir, "Task_com.png")       # 视频完成标志
    next_button = os.path.join(image_dir, "next_button.png") # 点击按钮
    # on_button = os.path.join(image_dir, "on.png")            # 播放按钮
    notice_flag = os.path.join(image_dir, "notice_flag.png") # 弹窗标志
    tip_flag = os.path.join(image_dir, "tip_flag.png")
    
    while True:
        # 1. 调整 Chrome 窗口
        win = set_window_state(window_title)
        if not win:
            print("Chrome window not found, exiting.")
            break
        
        # region = (win.left, win.top, win.width, win.height)
        region = (0, 0, 1280, 720)
        
        # 2. 检测 yellow_flag.png
        print("Checking for yellow_flag.png...")
        scroll_to_top(win)
        if not locate_image(yellow_flag, region):
            print("yellow_flag.png not found, task complete.")
            unmute_all_chrome_windows()
            break
        
        # 3. 等待 Task_com.png 出现
        print("Waiting for video to complete (Task_com.png)...")
        while True:
            tc = locate_image(task_com, region)
            if tc:
                print("Video completed!")
                break
            time.sleep(5) 
        
        # 4. 滑动到底部，点击 next_button.png 两次
        for i in range(2):
            scroll_to_bottom(win)
            nb = locate_image(next_button, region)
            if nb:
                center_x, center_y, _, _ = nb
                pyautogui.click(center_x, center_y)
                print(f"Clicked next_button.png ({i+1}/2)")
                time.sleep(5)
            else:
                print(f"next_button.png not found on attempt {i+1}")
                break
        
        # 5. 第三次点击 next_button.png（检测 notice_flag.png）
        # scroll_to_bottom(win)
        notice = locate_image(notice_flag, region)
        if notice:
            print("##### Test Attention! #####")
            time.sleep(1) # For safety test only.
            tip = locate_image(tip_flag, region)
            if tip:
                break
            nb = locate_image(next_button, region)
            if nb:
                center_x, center_y, _, _ = nb
                pyautogui.click(center_x, center_y)
                print("Found notice_flag.png, clicked next_button.png (3rd time, popup), entering second page")
                time.sleep(5) 
            else:
                print("Found notice_flag.png, but next_button.png not found in popup")
        else:
            print("No notice_flag.png detected, skipping third next_button.png click")
            time.sleep(3) 
        
        # 6. 播放视频并静音
        play_and_mute_window(win, region)
        
        # 7. 循环检测 yellow_flag.png
        print("Returning to check yellow_flag.png...")
        time.sleep(5)
    
    print("Task finished, no more yellow_flag.png detected.")

if __name__ == "__main__":
    image_dir = "loc"
    required_images = ["yellow_flag.png", "Task_com.png", "next_button.png", "on.png", "notice_flag.png"]
    for img in required_images:
        if not os.path.exists(os.path.join(image_dir, img)):
            print(f"Error: {img} not found in {image_dir} directory.")
            exit(1)
    
    main()