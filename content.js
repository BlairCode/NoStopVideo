(function(){
    'use strict';
    try {
        function findVideoElement() {
            let v = document.querySelector('video');
            if (v) return v;
            let iframes = document.querySelectorAll('iframe');
            for (let i of iframes) {
                try {
                    let d = i.contentDocument || i.contentWindow.document;
                    v = d.querySelector('video');
                    if (v) return v;
                } catch (e) {}
            }
            return null;
        }
        let video = findVideoElement();
        if (video) {
            console.log('Found video:', video);
            video.pause = function () {
                console.log('Pause blocked');
            };
            setInterval(() => {
                if (video.paused) {
                    video.play().catch(() => {});
                }
            }, 500);
        } else {
            console.log('No video found, blocking mouseout');
            window.addEventListener('mouseout', (e) => {
                e.stopPropagation();
                e.preventDefault();
                console.log('Mouseout blocked');
            }, true);
            if (window.ananas && window.ananas.pause) {
                window.ananas.pause = function () {
                    console.log('ananas pause blocked');
                };
            }
        }
    } catch (e) {
        console.log('Main error:', e.message);
    }
})();