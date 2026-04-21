---
layout: default
title: 세계관 및 배경
description: Shards of the Library의 방대한 세계관과 설정들을 확인해 보세요.
permalink: /lorebook/world/
---

<section class="world-index-section">
    <div class="world-index-header">
        <h1>World & Background</h1>
        <p>망각된 도서관과 그 주변 세계에 대한 기록들입니다.</p>
    </div>

    <!-- Category Tabs -->
    <div class="world-tabs">
        <button class="world-tab-btn active" data-target="all">전체</button>
        <button class="world-tab-btn" data-target="역사">역사</button>
        <button class="world-tab-btn" data-target="지리">지리</button>
        <button class="world-tab-btn" data-target="종족">종족</button>
        <button class="world-tab-btn" data-target="설정">설정</button>
    </div>

    <div class="world-grid">
        {% assign world_pages = site.pages | where: "layout", "world" | sort: "order" %}
        {% for item in world_pages %}
        <a href="{{ item.url | relative_url }}" class="world-card" data-category="{{ item.category }}">
            <div class="card-category">{{ item.category }}</div>
            <h2 class="card-title">{{ item.title }}</h2>
            <p class="card-desc">{{ item.description | truncate: 100 }}</p>
            <div class="read-more">자세히 보기 →</div>
        </a>
        {% endfor %}
        
        {% if world_pages.size == 0 %}
        <div class="no-content">
            <p>아직 등록된 세계관 문서가 없습니다. 곧 업데이트될 예정입니다!</p>
        </div>
        {% endif %}
    </div>
</section>

<style>
.world-index-section {
    max-width: 1200px;
    margin: 80px auto;
    padding: 0 20px;
}

.world-index-header {
    text-align: center;
    margin-bottom: 60px;
}

.world-index-header h1 {
    font-size: 3.5rem;
    font-family: 'Outfit', sans-serif;
    margin-bottom: 15px;
    background: linear-gradient(135deg, #fff 0%, #ffd700 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.world-index-header p {
    color: #888;
    font-size: 1.1rem;
}

.world-tabs {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 50px;
}

.world-tab-btn {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: #aaa;
    padding: 12px 28px;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s;
    font-weight: 600;
    font-size: 0.95rem;
}

.world-tab-btn:hover {
    background: rgba(255, 255, 255, 0.08);
    color: #fff;
    border-color: rgba(255, 215, 0, 0.3);
}

.world-tab-btn.active {
    background: #ffd700;
    color: #000;
    border-color: #ffd700;
    box-shadow: 0 8px 20px rgba(255, 215, 0, 0.2);
}

.world-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 30px;
}

.world-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 20px;
    padding: 40px;
    text-decoration: none;
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
}

.world-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, #ffd700, transparent);
    opacity: 0;
    transition: opacity 0.3s;
}

.world-card:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: rgba(255, 215, 0, 0.4);
    transform: translateY(-10px);
    box-shadow: 0 25px 50px rgba(0,0,0,0.5);
}

.world-card:hover::before {
    opacity: 1;
}

.card-category {
    font-size: 0.75rem;
    color: #ffd700;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 15px;
    font-weight: 700;
}

.card-title {
    font-size: 1.6rem;
    color: #fff;
    font-family: 'Outfit', sans-serif;
    margin-bottom: 15px;
}

.card-desc {
    font-size: 0.95rem;
    color: #999;
    margin-bottom: 25px;
    line-height: 1.6;
}

.read-more {
    font-size: 0.9rem;
    color: #ffd700;
    font-weight: 600;
    margin-top: auto;
}

.no-content {
    grid-column: 1 / -1;
    text-align: center;
    padding: 100px 0;
    color: #666;
    border: 2px dashed rgba(255,255,255,0.05);
    border-radius: 20px;
}

@media (max-width: 768px) {
    .world-index-header h1 { font-size: 2.5rem; }
    .world-grid { grid-template-columns: 1fr; }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.world-tab-btn');
    const cards = document.querySelectorAll('.world-card');

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
