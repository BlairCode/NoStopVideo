# No Stop Video

一个先进的 Chrome 扩展，专注于无缝视频播放体验，防止暂停并智能拦截鼠标移出事件，附带高效的学习通自动化刷课脚本。（持续优化更新中...）

> **No Stop Video**  
> *技碎枷锁鸣，影贯寰宇情。*  
> *Tech shatters chains' chime, streams pierce the realm sublime.*  
> *愿世间视频，皆自由流淌。*  
> *May all videos flow, unbound and strong.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Python 3.8+](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org) [![Chrome Extension](https://img.shields.io/badge/Chrome-Extension-yellow.svg)](https://www.google.com/chrome)

## ✨ 扩展核心功能特性
- **智能视频防暂停**：动态监测并确保视频持续播放，无惧鼠标移出窗口。
- **鼠标事件拦截**：精准阻止因鼠标离开触发的中断，优化用户体验。
- **零配置全站兼容**：开箱即用，适配所有网页环境。

## 🚀 Auto.py：学习通自动化刷课脚本
`Auto.py` 是一款精心设计的学习通刷课工具，集成以下功能：
- **图像识别引擎**：精准定位课程界面元素。
- **自动化操作流**：模拟点击，自动播放视频并推进进度。
- **音频控制**：静音 Chrome 进程，消除干扰。
- **任务状态检测**：智能翻页并确认任务完成。
- **题目自动处理**：高效完成视频内简单题目。
- **⚠️ 使用须知**：
  - **测试先行**：长时间运行（如夜间）前，建议先测试稳定性。若遇异常（如误点提交按钮），可关闭网页或终止脚本。
  - **静音管理**：默认静音 Chrome，可运行 `unmute.py` 快速恢复，或注释 `mute_chrome_process()` 调用。

## 🛠️ 安装指南
| 步骤 | 操作 |
|------|------|
| 1    | 打开 Chrome，导航至 `chrome://extensions/` |
| 2    | 启用“开发者模式”（右上角开关） |
| 3    | 点击“加载已解压的扩展” |
| 4    | **关键**：移除 `Auto.py`、`unmute.py` 及 `loc/` 文件夹，选择含 `manifest.json` 的目录 |
| 5    | 安装完成，立即生效 |

## 🔧 管理扩展
- **禁用**：访问 `chrome://extensions/`，切换扩展开关至关闭。
- **卸载**：在扩展页面点击“移除”按钮。

## 📂 项目结构
```
/
├── manifest.json       # 扩展核心配置文件
├── content.js          # 视频控制与事件拦截逻辑
├── background.js       # 后台运行服务
├── popup.html          # 精简交互界面
├── popup.js            # 弹出窗口动态脚本
├── icons/              # 高质量图标集
│   ├── icon16.png      # 16x16 小图标
│   ├── icon48.png      # 48x48 中图标
│   ├── icon128.png     # 128x128 大图标
├── Auto.py             # 学习通自动化脚本
├── unmute.py           # Chrome一键解除静音
└── loc/                # 图像识别资源
    ├── Task_com.png    # 任务完成标志
    ├── next_button.png # 下一步按钮
    ├── notice_flag.png # 弹窗标识
    ├── on.png          # 播放触发器
    ├── tip_flag.png    # 提示标识
    └── yellow_flag.png # 课程状态标记
```
> **提示**：推荐使用 `icons/` 存放多尺寸图标，遵循 Chrome 设计规范。

### 运行依赖
```bash
pip install pygetwindow pyautogui pycaw
```

## ⚠️ 注意事项与风险
- **定制化支持**：默认全站生效，可编辑 `manifest.json` 的 `host_permissions` 限定网站。
- **潜在冲突**：可能影响需暂停交互的网站功能。
- **安全限制**：部分网站启用 CSP，可能限制脚本执行。
- **合规性**：请确保使用符合目标平台的服务条款。
- **调试建议**：若功能异常，可禁用扩展恢复默认行为。

## 📜 许可证
本项目遵循 [MIT 许可证](https://opensource.org/licenses/MIT)，开源共享，欢迎贡献与定制。

## 📬 联系与支持
如在使用过程中遇到任何问题、技术疑问或建议，欢迎随时联系我：
- **邮箱**: [zhanghoubing777@gmail.com](mailto:your.email@example.com)
- **GitHub Issues**: [提交问题](https://github.com/BlairCode/NoStopVideo/issues)
- **社区支持**: 加入我们的 [讨论区](https://github.com/BlairCode/NoStopVideo/discussions) 与其他用户交流
我会尽快回复，助你解决问题！

---
_打造无缝学习与娱乐体验，No Stop Video 与你同行！_
