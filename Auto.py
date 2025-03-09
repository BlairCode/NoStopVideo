import pygetwindow as gw
import pyautogui
import time
import os
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import tkinter as tk
from tkinter import ttk, messagebox
import threading

class AutoVideoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NoStopVideo Automation")
        self.running = False
        self.mute_enabled = True
        self.image_dir = "loc"

        # 美化窗口
        self.root.geometry("600x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#e8f1fd")

        # 设置初始位置为屏幕中心
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 600
        window_height = 300
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # ttk 主题
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Helvetica", 12, "bold"), padding=8, background="#3498db", foreground="white")
        style.map("TButton", background=[("active", "#2980b9")])
        style.configure("TLabel", font=("Helvetica", 14, "bold"), foreground="#2c3e50")

        # GUI 布局
        self.title_label = ttk.Label(root, text="NoStopVideo Automation", foreground="#2c3e50")
        self.title_label.pack(pady=15)

        button_frame = tk.Frame(root, bg="#e8f1fd")
        button_frame.pack(pady=10)
        self.start_button = ttk.Button(button_frame, text="Start", command=self.start_automation)
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.stop_button = ttk.Button(button_frame, text="Stop", command=self.stop_automation, state="disabled")
        self.stop_button.pack(side=tk.LEFT, padx=10)
        self.mute_button = ttk.Button(button_frame, text="解除静音", command=self.toggle_mute)
        self.mute_button.pack(side=tk.LEFT, padx=10)

        self.status_text = tk.Text(root, height=10, width=50, font=("Verdana", 11), bg="#ffffff", fg="#e74c3c", borderwidth=2, relief="groove")
        self.status_text.pack(pady=15, padx=20)

        # 检查图片文件
        required_images = ["yellow_flag.png", "Task_com.png", "next_button.png", "on.png", "notice_flag.png"]
        for img in required_images:
            if not os.path.exists(os.path.join(self.image_dir, img)):
                messagebox.showerror("Error", f"{img} not found in {self.image_dir}")
                exit(1)

        # 启动后动态调整位置
        self.root.after(1000, self.update_window_position)

    def update_window_position(self):
        """后续将窗口放置在 Chrome 窗口正下方"""
        chrome_windows = [w for w in gw.getWindowsWithTitle("Google Chrome")]
        if chrome_windows:
            win = chrome_windows[0]
            if win.isMinimized or win.isMaximized:
                win.restore()
            chrome_x, chrome_y = win.left, win.top
            chrome_width, chrome_height = win.width, win.height
            new_x = chrome_x + (chrome_width - 600) // 2
            new_y = chrome_y + chrome_height + 10
            self.root.geometry(f"600x300+{new_x}+{new_y}")
        self.root.after(1000, self.update_window_position)  # 每秒更新

    def log(self, message):
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
        self.root.update()

    def toggle_mute(self):
        self.mute_enabled = not self.mute_enabled
        if self.mute_enabled:
            self.mute_button.config(text="解除静音")
            self.log("已启用静音功能")
            self.mute_all_chrome_windows()
        else:
            self.mute_button.config(text="启用静音")
            self.log("已解除静音功能")
            self.unmute_all_chrome_windows()

    def set_window_state(self, window_title):
        windows = [w for w in gw.getWindowsWithTitle(window_title)]
        if not windows:
            self.log("未找到 Chrome 窗口")
            return None
        
        win = windows[0]
        if win.isMinimized:
            win.restore()
        if win.isMaximized:
            win.restore()
        win.activate()
        time.sleep(0.5)  # 缩短为 0.5 秒
        win.resizeTo(1280, 880)
        win.moveTo(0, 0)
        self.log("调整 Chrome 窗口大小和位置")
        return win

    def locate_image(self, image_file, region=None, confidence=0.9):
        try:
            pos = pyautogui.locateOnScreen(image_file, region=region, confidence=confidence)
            if pos:
                center_x = pos.left + pos.width // 2
                center_y = pos.top + pos.height // 2
                return center_x, center_y, pos.width, pos.height
            return None
        except Exception:
            return None

    def scroll_to_bottom(self, win):
        pyautogui.moveTo(win.left + win.width // 2, win.top + win.height // 2)
        pyautogui.scroll(-10000)
        time.sleep(1)  # 缩短为 1 秒

    def scroll_to_top(self, win):
        pyautogui.moveTo(win.left + win.width // 2, win.top + win.height // 2)
        pyautogui.scroll(10000)
        time.sleep(1)  # 缩短为 1 秒

    def unmute_all_chrome_windows(self):
        sessions = AudioUtilities.GetAllSessions()
        muted_count = 0
        for session in sessions:
            if session.Process and "chrome" in session.Process.name().lower():
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                volume.SetMute(0, None)
                muted_count += 1
        if muted_count > 0:
            self.log("已取消所有 Chrome 窗口的静音")
        else:
            self.log("未找到静音的 Chrome 窗口")
        time.sleep(1)  # 缩短为 1 秒
        return muted_count > 0

    def mute_all_chrome_windows(self):
        """静音所有 Chrome 窗口"""
        sessions = AudioUtilities.GetAllSessions()
        muted_count = 0
        for session in sessions:
            if session.Process and "chrome" in session.Process.name().lower():
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                volume.SetMute(1, None)
                muted_count += 1
        if muted_count > 0:
            self.log(f"已静音 {muted_count} 个 Chrome 窗口")
        else:
            self.log("未找到可静音的 Chrome 窗口")
        time.sleep(1)  # 与 unmute_all_chrome_windows 保持一致
        return muted_count > 0

    def mute_chrome_process(self, win):
        if not win:
            self.log("未找到当前窗口，无法静音")
            return False
        
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and "chrome" in session.Process.name().lower():
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                volume.SetMute(1, None)
                self.log("已静音 Chrome 音频")
                time.sleep(1)  # 缩短为 1 秒
                return True
        
        self.log("未找到 Chrome 音频会话")
        return False

    def play_and_mute_window(self, win, region):
        on_button = os.path.join("loc", "on.png")
        on_pos = self.locate_image(on_button, region)
        if on_pos:
            center_x, center_y, _, _ = on_pos
            pyautogui.click(center_x, center_y)
            self.log("点击播放按钮，开始播放视频")
        else:
            self.log("未找到播放按钮，跳过播放")
            return False
        
        if self.mute_enabled:
            if self.mute_chrome_process(win):
                return True
        else:
            self.log("静音功能已关闭，保持声音播放")
        return True

    def automation_loop(self):
        window_title = "Google Chrome"
        yellow_flag = os.path.join(self.image_dir, "yellow_flag.png")
        task_com = os.path.join(self.image_dir, "Task_com.png")
        next_button = os.path.join(self.image_dir, "next_button.png")
        notice_flag = os.path.join(self.image_dir, "notice_flag.png")
        tip_flag = os.path.join(self.image_dir, "tip_flag.png")
        Ques_in_v = os.path.join(self.image_dir, "True_or_false.png")
        selector_button = os.path.join(self.image_dir, "selector.png")
        submit_button = os.path.join(self.image_dir, "submit.png")
        
        while self.running:
            win = self.set_window_state(window_title)
            if not win:
                self.log("程序退出")
                break
            
            region = (0, 0, 1280, 880)
            
            self.log("检查视频任务状态...")
            self.scroll_to_top(win)
            if not self.locate_image(yellow_flag, region):
                self.log("所有视频任务完成")
                if not self.mute_enabled:
                    self.unmute_all_chrome_windows()
                break
            
            self.log("等待当前视频播放完成...")
            while self.running:
                tc = self.locate_image(task_com, region)
                if tc:
                    self.log("视频播放完成")
                    break

                ques = self.locate_image(Ques_in_v, region)
                if ques:
                    self.log("检测到题目界面，处理中...")
                    try:
                        matches = list(pyautogui.locateAllOnScreen(selector_button, region=region, confidence=0.95))
                        if not matches:
                            self.log("未找到选项按钮，等待重试")
                            time.sleep(3)  # 缩短为 3 秒
                            continue

                        matches.sort(key=lambda pos: pos.top)
                        for i, pos in enumerate(matches):
                            center_x = pos.left + pos.width // 2
                            center_y = pos.top + pos.height // 2
                            pyautogui.click(center_x, center_y)
                            self.log(f"点击选项 {i+1}")
                            time.sleep(0.2)  # 缩短为 0.2 秒

                            sub = self.locate_image(submit_button, region)
                            if sub:
                                center_x, center_y, _, _ = sub
                                pyautogui.click(center_x, center_y)
                                self.log("点击提交按钮")
                                time.sleep(0.5)  # 缩短为 0.5 秒
                                
                            if not self.locate_image(Ques_in_v, region):
                                self.log("题目界面已清除")
                                break
                    except Exception as e:
                        self.log(f"处理题目时出错: {e}")

                time.sleep(5)  # 缩短为 5 秒
            
            for i in range(2):
                self.scroll_to_bottom(win)
                nb = self.locate_image(next_button, region)
                if nb:
                    center_x, center_y, _, _ = nb
                    pyautogui.click(center_x, center_y)
                    self.log(f"点击 Next 按钮 ({i+1}/2)")
                    time.sleep(2)  # 缩短为 2 秒
                else:
                    self.log(f"未找到 Next 按钮 (尝试 {i+1})")
                    break
            
            notice = self.locate_image(notice_flag, region)
            if notice:
                self.log("检测到提示弹窗")
                time.sleep(0.5)  # 缩短为 0.5 秒
                tip = self.locate_image(tip_flag, region)
                if tip:
                    break
                nb = self.locate_image(next_button, region)
                if nb:
                    center_x, center_y, _, _ = nb
                    pyautogui.click(center_x, center_y)
                    self.log("点击 Next 按钮关闭弹窗，进入下一页")
                    time.sleep(2)  # 缩短为 2 秒
                else:
                    self.log("弹窗中未找到 Next 按钮")
            else:
                self.log("未检测到弹窗，跳过")
                time.sleep(1)  # 缩短为 1 秒
            
            self.log("进入视频页面并处理声音")
            self.play_and_mute_window(win, region)
            self.log("准备检查下一任务...")
            time.sleep(2)  # 缩短为 2 秒
        
        self.log("任务全部完成，程序结束")
        self.stop_automation()

    def start_automation(self):
        if not self.running:
            self.running = True
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")
            threading.Thread(target=self.automation_loop, daemon=True).start()

    def stop_automation(self):
        self.running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoVideoApp(root)
    root.mainloop()