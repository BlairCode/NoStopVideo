document.addEventListener('DOMContentLoaded', () => {
    const statusEl = document.getElementById('status');
    const toggleBtn = document.getElementById('toggle');

    chrome.storage.sync.get(['enabled'], (result) => {
        const isEnabled = result.enabled || false; // 默认关闭
        statusEl.textContent = isEnabled ? 'Enabled' : 'Disabled';
        toggleBtn.textContent = isEnabled ? 'Disable' : 'Enable';
    });

    toggleBtn.addEventListener('click', () => {
        chrome.storage.sync.get(['enabled'], (result) => {
            const isEnabled = result.enabled || false;
            const newState = !isEnabled;
            chrome.storage.sync.set({ enabled: newState }, () => {
                statusEl.textContent = newState ? 'Enabled' : 'Disabled';
                toggleBtn.textContent = newState ? 'Disable' : 'Enable';

                chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
                    if (tabs[0]) {
                        if (newState) {
                            chrome.scripting.executeScript({
                                target: { tabId: tabs[0].id },
                                files: ['content.js']
                            });
                        } else {
                            chrome.tabs.reload(tabs[0].id); // 刷新撤销效果
                        }
                    }
                });
            });
        });
    });
});