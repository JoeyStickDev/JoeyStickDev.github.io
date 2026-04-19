---
layout: default
title: 메인 스토리북
description: 조이빌리지에서 시작되는 방대한 대서사시.
permalink: /lorebook/story/
---

<section class="story-index-section">
    <div class="story-index-header">
        <h1>Shards of the Library: Storybook</h1>
        <p>기록되지 않은 이야기의 파편들을 모았습니다.</p>
    </div>

    <!-- Category Tabs -->
    <div class="story-tabs">
        <button class="story-tab-btn active" data-target="all">전체</button>
        <button class="story-tab-btn" data-target="main">메인 스토리</button>
        <button class="story-tab-btn" data-target="sub-quests">서브 퀘스트</button>
        <button class="story-tab-btn" data-target="skill-quests">스킬 퀘스트</button>
    </div>

    <div class="story-grid">
        {% assign stories = site.pages | where: "layout", "story" | sort: "chapter_num" %}
        {% for story in stories %}
        {% assign cat = "main" %}
        {% if story.category %}{% assign cat = story.category %}{% endif %}
        <a href="{{ story.url | relative_url }}" class="story-card" data-category="{{ cat }}">
            <div class="card-num">
                {% if story.chapter_num %}Chapter {{ story.chapter_num }}{% else %}{{ story.quest_id }}{% endif %}
            </div>
            <h2 class="card-title">{{ story.title }}</h2>
            <div class="card-type">{{ cat | replace: 'sub-quests', '서브 퀘스트' | replace: 'skill-quests', '스킬 퀘스트' | replace: 'main', '메인 스토리' }}</div>
            <div class="read-more">이야기 읽기 →</div>
        </a>
        {% endfor %}
    </div>
</section>

<style>
.story-tabs {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-bottom: 50px;
}

.story-tab-btn {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: #888;
    padding: 10px 25px;
    border-radius: 30px;
    cursor: pointer;
    transition: all 0.3s;
    font-weight: 600;
}

.story-tab-btn:hover {
    background: rgba(255, 255, 255, 0.1);
    color: #fff;
}

.story-tab-btn.active {
    background: #ffd700;
    color: #000;
    border-color: #ffd700;
    box-shadow: 0 0 15px rgba(255, 215, 0, 0.3);
}

.card-type {
    font-size: 0.8rem;
    color: #888;
    margin-bottom: 20px;
}
.story-index-section {
    max-width: 1200px;
    margin: 80px auto;
    padding: 0 20px;
}

.story-index-header {
    text-align: center;
    margin-bottom: 60px;
}

.story-index-header h1 {
    font-size: 3rem;
    font-family: 'Outfit', sans-serif;
    margin-bottom: 10px;
    background: linear-gradient(135deg, #fff 0%, #ffd700 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.story-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 30px;
}

.story-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    padding: 30px;
    text-decoration: none;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.story-card:hover {
    background: rgba(255, 255, 255, 0.06);
    border-color: rgba(255, 215, 0, 0.4);
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}

.card-num {
    font-size: 0.8rem;
    color: #ffd700;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.card-title {
    font-size: 1.4rem;
    color: #fff;
    font-family: 'Outfit', sans-serif;
    margin-bottom: 20px;
}

.read-more {
    font-size: 0.9rem;
    color: #ffd700;
    font-weight: 600;
}

@media (max-width: 768px) {
    .story-index-header h1 { font-size: 2.2rem; }
    .story-grid { grid-template-columns: 1fr; }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.story-tab-btn');
    const cards = document.querySelectorAll('.story-card');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const target = tab.getAttribute('data-target');

            // Update active tab
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            // Filter cards
            cards.forEach(card => {
                if (target === 'all' || card.getAttribute('data-category') === target) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
});
</script>
