---
layout: default
title: Admin Roadmap (5 Days)
permalink: /admin/roadmap/
---

# 🗓️ 5일 집중 개발 로드맵 (마무리 & 폴리싱)

<p style="color: var(--text-muted); font-size: 1.1rem;">출시 전 마무리를 위한 5일 70시간 강행군 개발 일정입니다. (브라우저에 체크박스와 코멘트가 자동 저장됩니다)</p>

<style>
    .task-item { margin-bottom: 15px; }
    .task-label { display: flex; align-items: start; gap: 10px; cursor: pointer; font-size: 1.05rem; margin-bottom: 5px; }
    .task-checkbox { margin-top: 6px; transform: scale(1.2); }
    .task-text { transition: all 0.3s; }
    .task-comment { margin-left: 25px; width: calc(100% - 30px); padding: 6px 10px; background: rgba(0,0,0,0.2); border: 1px solid var(--border-color, #444); border-radius: 4px; color: #ddd; font-size: 0.9rem; }
    .task-comment:focus { border-color: var(--accent-color, #d4af37); outline: none; background: rgba(0,0,0,0.4); }
</style>

<div style="background: var(--bg-card, #1e1e1e); padding: 20px; border-radius: 12px; margin-bottom: 20px; border: 1px dashed var(--border-color, #333);">
    <h2 style="color: var(--accent-color, #d4af37); margin-top: 0;">Day 1: 🚨 최우선 과제 & 게임 코어 밸런스</h2>
    <div style="display: flex; flex-direction: column; line-height: 1.6;">
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d1_1" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[0시급] 깃허브 업로드를 위한 파일 정리 (In progress)</strong>: 퀘스트 데이터 정보 등 싹 정리. 백업/버전 관리.</span>
            </label>
            <input type="text" id="comment_d1_1" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d1_2" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[0시급] 아이템 이미지 일관성 (In progress)</strong>: 라그나로크 모바일 느낌으로 일관성 작업.</span>
            </label>
            <input type="text" id="comment_d1_2" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d1_3" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[1매우중요] 스태미나 시스템 개편 (OnlyFoundation)</strong>: 공격 시 스태미나 소비 증가, 패시브 적용/코스트 수정.</span>
            </label>
            <input type="text" id="comment_d1_3" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d1_4" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[1매우중요] 시네마틱 연출 기획 및 조사 🔍</strong>: 퀘스트를 직접 플레이하며 시퀀스를 적용할 최적의 위치와 타이밍 기획/자료 조사.</span>
            </label>
            <input type="text" id="comment_d1_4" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
    </div>
</div>

<div style="background: var(--bg-card, #1e1e1e); padding: 20px; border-radius: 12px; margin-bottom: 20px; border: 1px dashed var(--border-color, #333);">
    <h2 style="color: var(--accent-color, #d4af37); margin-top: 0;">Day 2: 🎨 시각적 완성도 & 핵심 콘텐츠 뼈대 다지기</h2>
    <div style="display: flex; flex-direction: column; line-height: 1.6;">
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d2_5" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[1매우중요] 기본 UI 전체 개편 🆕</strong>: 게임 내 기본 UI 디자인 일관성 확보 및 대대적인 시각적 업그레이드.</span>
            </label>
            <input type="text" id="comment_d2_5" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d2_6" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[1매우중요] 메인메뉴 및 캐릭터 생성 로직 변경 🆕</strong>: 게임 진입점인 메인메뉴와 캐릭터 생성 흐름/로직 전면 개편.</span>
            </label>
            <input type="text" id="comment_d2_6" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d2_7" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[1매우중요] 시네마틱 카메라 연출 제작 🎬</strong>: Day 1에 조사된 자료를 토대로 실제 시퀀스 제작 및 플레이어 이동 제한 로직 적용.</span>
            </label>
            <input type="text" id="comment_d2_7" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d2_1" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[2중요] 캐릭터 외형 폴리싱 (In progress)</strong>: 머리카락 cc 오류 수정, 눈/코/입 추가, 색감 조정.</span>
            </label>
            <input type="text" id="comment_d2_1" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d2_2" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[2중요] 아이템 메시 교체 (In progress)</strong>: 음식류 메시 교체 마무리.</span>
            </label>
            <input type="text" id="comment_d2_2" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d2_3" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[2중요] 장비 아이템 (OnlyFoundation)</strong>: 직업별 3종류밖에 없는 장비 뼈대.</span>
            </label>
            <input type="text" id="comment_d2_3" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d2_4" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[2중요] 별자리별 효과 (OnlyFoundation)</strong>: 버프만 존재하는 별자리 시스템 기능 연결.</span>
            </label>
            <input type="text" id="comment_d2_4" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
    </div>
</div>

<div style="background: var(--bg-card, #1e1e1e); padding: 20px; border-radius: 12px; margin-bottom: 20px; border: 1px dashed var(--border-color, #333);">
    <h2 style="color: var(--accent-color, #d4af37); margin-top: 0;">Day 3: ⚙️ 디테일 및 사운드, UI 연결</h2>
    <div style="display: flex; flex-direction: column; line-height: 1.6;">
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d3_1" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[2중요] 호감도 시스템 상세화 (OnlyFoundation)</strong>: 호감도 질문/대사 보강.</span>
            </label>
            <input type="text" id="comment_d3_1" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d3_2" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[2중요] 사운드 & 이펙트 점검</strong>: 누락된 스킬 효과음 확인 및 포탈 이펙트 추가.</span>
            </label>
            <input type="text" id="comment_d3_2" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d3_3" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[2중요] 전투 시스템 수정 (Not started)</strong>: 스매시에 전투 패시브 적용(활 공격력 등).</span>
            </label>
            <input type="text" id="comment_d3_3" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d3_4" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[2중요] Async 로딩화면 (Not started)</strong>: 로딩 로고 수정 및 디테일 향상.</span>
            </label>
            <input type="text" id="comment_d3_4" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
    </div>
</div>

<div style="background: var(--bg-card, #1e1e1e); padding: 20px; border-radius: 12px; margin-bottom: 20px; border: 1px dashed var(--border-color, #333);">
    <h2 style="color: var(--accent-color, #d4af37); margin-top: 0;">Day 4: 🎶 분위기 조성 & 마케팅, 기획 결론</h2>
    <div style="display: flex; flex-direction: column; line-height: 1.6;">
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d4_1" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[2중요] 맵마다 배경음악 추가 (SlowProcess)</strong>: 에셋 또는 AI 생성 활용.</span>
            </label>
            <input type="text" id="comment_d4_1" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d4_2" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[2중요] 게임 페이지 제작 (In progress)</strong>: 배포용 게임 소개 페이지/상점 페이지.</span>
            </label>
            <input type="text" id="comment_d4_2" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d4_3" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[2중요] 초반 시작 영상 제작 (Not started)</strong>: 게임 튜토리얼 도입부 영상 추가.</span>
            </label>
            <input type="text" id="comment_d4_3" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d4_4" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[2중요] 기획 결론 내기 (좀더고민해보자)</strong>: 땅 삽질 관련 설정, UI AFK 적용 여부 결정 후 마무리.</span>
            </label>
            <input type="text" id="comment_d4_4" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
    </div>
</div>

<div style="background: var(--bg-card, #1e1e1e); padding: 20px; border-radius: 12px; margin-bottom: 20px; border: 1px dashed var(--border-color, #333);">
    <h2 style="color: var(--accent-color, #d4af37); margin-top: 0;">Day 5: 🐞 Q&A, 버그 픽스 및 최종 마감</h2>
    <div style="display: flex; flex-direction: column; line-height: 1.6;">
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d5_1" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[2중요] 작물 성장 단계 모델링 (SlowProcess)</strong>: 필요 시 최소한의 단계(3단계 등)로 타협.</span>
            </label>
            <input type="text" id="comment_d5_1" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d5_2" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[3~4순위] 편의성 및 서브 작업</strong>: 주간퀘 몬스터 랜덤 등장, 빠른 이동 복구 등.</span>
            </label>
            <input type="text" id="comment_d5_2" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d5_3" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>[전체] 처음부터 끝까지 플레이 테스트</strong>: 튜토리얼부터 메인 퀘스트, 스킬 획득까지 전체 점검.</span>
            </label>
            <input type="text" id="comment_d5_3" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
        <div class="task-item">
            <label class="task-label">
                <input type="checkbox" id="task_d5_4" class="task-checkbox" onchange="saveProgress(this)">
                <span class="task-text"><strong>출시/업로드 준비</strong>: 깃허브/스팀 최종 빌드 업로드 및 테스트.</span>
            </label>
            <input type="text" id="comment_d5_4" class="task-comment" oninput="saveComment(this)" placeholder="작업 노트 및 코멘트 추가...">
        </div>
    </div>
</div>

<div style="text-align: center; margin-top: 30px;">
    <button onclick="clearProgress()" style="padding: 10px 20px; background: #dc3545; color: #fff; border: none; border-radius: 4px; cursor: pointer; margin-right: 10px;">초기화</button>
    <a href="/admin/" style="display: inline-block; padding: 10px 20px; background: #333; color: #fff; text-decoration: none; border-radius: 4px;">&larr; Back to Admin Console</a>
</div>

<script>
    function saveProgress(checkbox) {
        localStorage.setItem(checkbox.id, checkbox.checked);
        updateStyle(checkbox);
    }

    function saveComment(input) {
        localStorage.setItem(input.id, input.value);
    }

    function updateStyle(checkbox) {
        if(checkbox.checked) {
            checkbox.nextElementSibling.style.textDecoration = 'line-through';
            checkbox.nextElementSibling.style.opacity = '0.4';
            checkbox.nextElementSibling.style.color = '#888';
        } else {
            checkbox.nextElementSibling.style.textDecoration = 'none';
            checkbox.nextElementSibling.style.opacity = '1';
            checkbox.nextElementSibling.style.color = 'inherit';
        }
    }

    function clearProgress() {
        if(confirm("모든 체크박스와 코멘트 내용을 초기화하시겠습니까?")) {
            document.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
                localStorage.removeItem(checkbox.id);
                checkbox.checked = false;
                updateStyle(checkbox);
            });
            document.querySelectorAll('input[type="text"]').forEach(input => {
                localStorage.removeItem(input.id);
                input.value = '';
            });
        }
    }

    document.addEventListener("DOMContentLoaded", () => {
        // Load Checkboxes
        document.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
            const isChecked = localStorage.getItem(checkbox.id) === 'true';
            checkbox.checked = isChecked;
            updateStyle(checkbox);
        });

        // Load Comments
        document.querySelectorAll('input[type="text"]').forEach(input => {
            const savedComment = localStorage.getItem(input.id);
            if(savedComment !== null) {
                input.value = savedComment;
            }
        });
    });
</script>
