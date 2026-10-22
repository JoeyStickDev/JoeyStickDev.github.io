document.addEventListener('DOMContentLoaded', () => {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    function activateTab(targetId) {
        if (!document.getElementById(targetId)) return;
        
        tabBtns.forEach(b => b.classList.remove('active'));
        tabContents.forEach(c => c.classList.remove('active'));

        const activeBtn = document.querySelector(`.tab-btn[data-target="${targetId}"]`);
        if(activeBtn) activeBtn.classList.add('active');
        document.getElementById(targetId).classList.add('active');
    }

    // 버튼 클릭 이벤트
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-target');
            activateTab(targetId);
            // URL 해시 업데이트 (이동 없이)
            history.pushState(null, null, '#' + targetId);
        });
    });

    // 페이지 로드 시 URL 해시 확인
    if (window.location.hash) {
        const hash = window.location.hash.substring(1);
        activateTab(hash);
    }

    // 같은 페이지 내에서 드롭다운 메뉴로 해시만 변경될 때 탭 즉각 전환
    window.addEventListener('hashchange', () => {
        if (window.location.hash) {
            const hash = window.location.hash.substring(1);
            activateTab(hash);
        }
    });

    // 휴대폰 메뉴 (☰): 열고 닫기, 메뉴의 링크를 누르면 닫힌다
    const header = document.querySelector('.global-header');
    const navToggle = document.querySelector('.nav-toggle');
    if (header && navToggle) {
        const setOpen = open => {
            header.classList.toggle('nav-open', open);
            navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
            navToggle.textContent = open ? '✕' : '☰';
        };
        navToggle.addEventListener('click', () => setOpen(!header.classList.contains('nav-open')));
        header.querySelectorAll('.main-nav a').forEach(a => a.addEventListener('click', () => setOpen(false)));
    }
});
