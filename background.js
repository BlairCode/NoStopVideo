chrome.runtime.onInstalled.addListener(() => {
    chrome.storage.sync.set({ enabled: false }, () => {
        console.log("Extension installed, default disabled");
    });
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete') {
        chrome.storage.sync.get(['enabled'], (result) => {
            if (result.enabled) {
                chrome.scripting.executeScript({
                    target: { tabId: tabId },
                    files: ['content.js']
                });
            }
        });
    }
});