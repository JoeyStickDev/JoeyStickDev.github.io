---
layout: default
title: 메인 스토리북
description: 조이빌리지에서 시작되는 방대한 대서사시.
permalink: /lorebook/story/
---

<section class="story-index-section">
    <div class="story-index-header">
        <h1>Shards of the Library: Main Story</h1>
        <p>수수께끼의 도서관에서 펼쳐지는 이야기의 기록입니다.</p>
    </div>

    <div class="story-grid">
        {% assign stories = site.pages | where: "layout", "story" | sort: "chapter_num" %}
        {% for story in stories %}
        <a href="{{ story.url | relative_url }}" class="story-card">
            <div class="card-num">Chapter {{ story.chapter_num }}</div>
            <h2 class="card-title">{{ story.title }}</h2>
            <div class="read-more">이야기 읽기 →</div>
        </a>
        {% endfor %}
    </div>
</section>

<style>
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
