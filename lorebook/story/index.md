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

        {% comment %}== 1. 메인 챕터 카드 (chapter_num 있는 것만) =={% endcomment %}
        {% assign main_stories = site.pages | where: "layout", "story" | where_exp: "p", "p.chapter_num" | sort: "chapter_num" %}
        {% for story in main_stories %}
        <a href="{{ story.url | relative_url }}" class="story-card" data-category="main">
            <div>
                <div class="card-num">Chapter {{ story.chapter_num }}</div>
                <h2 class="card-title">{{ story.title }}</h2>
                <div class="card-type">메인 스토리</div>
            </div>
            <div class="read-more">이야기 읽기 →</div>
        </a>
        {% endfor %}

        {% comment %}== 2. 서브 퀘스트 그룹 카드 =={% endcomment %}
        {% assign sub_stories = site.pages | where: "layout", "story" | where: "category", "sub-quests" | sort: "quest_id" %}
        {% assign sub_groups_seen = "" %}
        {% for story in sub_stories %}
            {% assign qid = story.quest_id %}
            {% assign qid_parts = qid | split: "_" %}
            {% assign group_key = qid_parts[0] | append: "_" | append: qid_parts[1] %}
            {% unless sub_groups_seen contains group_key %}
                {% assign sub_groups_seen = sub_groups_seen | append: group_key | append: "," %}
                {% assign group_num = qid_parts[1] %}
                {% assign sub_count = sub_stories | where_exp: "s", "s.quest_id contains group_key" | size %}
                <a href="{{ story.url | relative_url }}" class="story-card" data-category="sub-quests">
                    <div>
                        <div class="card-num">서브 퀘스트 {{ group_num }}</div>
                        <h2 class="card-title">서브 퀘스트 {{ group_num }}번 이야기</h2>
                        <div class="card-type">서브 퀘스트 · {{ sub_count }}개 챕터</div>
                    </div>
                    <div class="read-more">퀘스트 보기 →</div>
                </a>
            {% endunless %}
        {% endfor %}

        {% comment %}== 3. 스킬 퀘스트 그룹 카드 =={% endcomment %}
        {% assign skill_stories = site.pages | where: "layout", "story" | where: "category", "skill-quests" | sort: "quest_id" %}
        {% assign skill_groups_seen = "" %}
        {% for story in skill_stories %}
            {% assign qid = story.quest_id %}
            {% assign qid_parts = qid | split: "_" %}
            {% assign group_key = qid_parts[0] | append: "_" | append: qid_parts[1] %}
            {% unless skill_groups_seen contains group_key %}
                {% assign skill_groups_seen = skill_groups_seen | append: group_key | append: "," %}
                {% assign group_num = qid_parts[1] %}
                {% assign sk_count = skill_stories | where_exp: "s", "s.quest_id contains group_key" | size %}
                <a href="{{ story.url | relative_url }}" class="story-card" data-category="skill-quests">
                    <div>
                        <div class="card-num">스킬 퀘스트 {{ group_num }}</div>
                        <h2 class="card-title">스킬 퀘스트 {{ group_num }}번 이야기</h2>
                        <div class="card-type">스킬 퀘스트 · {{ sk_count }}개 챕터</div>
                    </div>
                    <div class="read-more">퀘스트 보기 →</div>
                </a>
            {% endunless %}
        {% endfor %}

    </div>
</section>

<style>
.story-tabs {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-bottom: 50px;
    flex-wrap: wrap;
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

            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

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
