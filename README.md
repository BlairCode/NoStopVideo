# No Stop Video

一个简约的 Chrome 扩展与高效自动化工具组合，专注于无缝视频播放与学习通刷课体验。扩展防止视频暂停并拦截鼠标移出事件，自动化脚本智能管理课程进度。

> **No Stop Video**  
> *技碎枷锁鸣，影贯寰宇情。*  
> *Tech shatters chains' chime, streams pierce the realm sublime.*  
> *愿世间视频，皆自由流淌。*  
> *May all videos flow, unbound and strong.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Python 3.8+](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org) [![Chrome Extension](https://img.shields.io/badge/Chrome-Extension-yellow.svg)](https://www.google.com/chrome)

## ✨ 项目核心功能
### chrome-extension
- **智能视频防暂停**：动态监测，确保视频持续播放，无惧鼠标移出窗口。
- **鼠标事件拦截**：精准阻止因鼠标离开触发的中断。
- **零配置全站兼容**：开箱即用，适配所有网页。

### automation-program
- **图像识别引擎**：精准定位学习通课程界面元素。
- **自动化操作流**：模拟点击，自动播放视频并推进进度。
- **音频控制**：支持静音/取消静音 Chrome 进程。
- **任务状态检测**：智能翻页并确认任务完成。
- **题目自动处理**：高效完成视频内简单题目。

  ![Automation_window](https://github.com/user-attachments/assets/d90b7935-84ff-4c82-a675-f791da6ebf5e)


## 🛠️ 安装指南
### 下载与解压
- 从 [GitHub Releases](https://github.com/BlairCode/NoStopVideo/releases/tag/v1.0.0) 下载 `nostopvideo-v1.0.0.zip`。
- 解压后包含两个文件夹：`chrome-extension` 和 `automation-program`。

### 1. 安装 chrome-extension
| 步骤 | 操作 |
|------|------|
| 1    | 打开 Chrome，导航至 `chrome://extensions/` |
| 2    | 启用“开发者模式”（右上角开关） |
| 3    | 点击“加载已解压的扩展” |
| 4    | 选择解压后的 `chrome-extension` 文件夹 |
| 5    | 安装完成，立即生效 |

### 2. 运行 automation-program
| 步骤 | 操作 |
|------|------|
| 1    | 进入解压后的 `automation-program` 文件夹 |
| 2    | 确保 `loc` 文件夹与 `Auto.exe` 在同一目录 |
| 3    | 双击 `Auto.exe` 运行 |

## 🔧 使用说明
- **扩展管理**：在 `chrome://extensions/` 禁用或移除扩展。
- **静音控制**：`automation-program` 默认静音 Chrome，可点击界面“解除静音”按钮切换。
- **测试建议**：首次运行 `Auto.exe` 时，建议观察几分钟，确保稳定后再长时间运行。
- **窗口管理**：Chrome窗口置于最上方，`Auto.exe`才可检测到窗口信息。

## 📂 Release 结构
```
nostopvideo-v1.0.0.zip
├── chrome-extension/       # Chrome 扩展文件夹
│   ├── manifest.json      # 扩展核心配置文件
│   ├── content.js         # 视频控制与事件拦截逻辑
│   ├── background.js      # 后台运行服务
│   ├── popup.html         # 精简交互界面
│   ├── popup.js           # 弹出窗口动态脚本
│   └── icons/             # 高质量图标集
│       ├── icon16.png     # 16x16 小图标
│       ├── icon48.png     # 48x48 中图标
│       └── icon128.png    # 128x128 大图标
└── automation-program/     # 自动化程序文件夹
    ├── Auto.exe           # 可执行文件
    └── loc/               # 图像识别资源
        ├── Task_com.png   # 任务完成标志
        ├── next_button.png # 下一步按钮
        ├── notice_flag.png # 弹窗标识
        ├── on.png         # 播放触发器
        └── yellow_flag.png # 课程状态标记
```

## ⚠️ 注意事项
- **扩展范围**：默认全站生效，可编辑 `manifest.json` 的 `host_permissions` 限定网站（如 `["*://*.chaoxing.com/*"]`）。
- **潜在冲突**：扩展可能影响需暂停交互的网站。
- **合规性**：请确保使用符合学习通服务条款。
- **稳定性**：若 `Auto.exe` 异常（如误点），可关闭 Chrome 或终止程序。

## 📜 许可证
本项目遵循 [MIT 许可证](https://opensource.org/licenses/MIT)，开源共享，欢迎贡献。

## 📬 联系与支持
- **邮箱**: [zhanghoubing777@gmail.com](mailto:zhanghoubing777@gmail.com)
- **GitHub Issues**: [提交问题](https://github.com/BlairCode/NoStopVideo/issues)
- **讨论区**: [加入交流](https://github.com/BlairCode/NoStopVideo/discussions)

---
# _打造无缝学习与娱乐体验，No Stop Video 与你同行！_
