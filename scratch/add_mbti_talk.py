import csv

mbti_path = r"f:\Git\JoeyStickDev.github.io\Temp\NPC_MBTI_DT.csv"
talk_path = r"f:\Git\JoeyStickDev.github.io\Temp\NPC_TalkData_DT.csv"

# Read MBTI
mbtis = {}
with open(mbti_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if len(row) >= 3:
            name = row[1]
            mbti = row[2]
            mbtis[name] = mbti

mbti_dialogs = {
    "INTJ": {
        "npc": "You are constantly around... it disrupts my usual patterns. Yet, I find myself factoring you into my equations.",
        "reply1": ("It's just coincidence. Don't overthink it._F+0.2", "0"),
        "reply2": ("Someone just like you... Sharp enough to see through me, soft enough to stay._R+0.8", "80R100")
    },
    "INFP": {
        "npc": "Sometimes I get lost in my own thoughts, wandering far away... but when I look back, you're always there, anchoring me.",
        "reply1": ("I just happen to be around._F+0.2", "0"),
        "reply2": ("I'll always wait for you to find your way back to me._R+0.8", "80R100")
    },
    "ISFJ": {
        "npc": "I'm always making sure everyone else is okay. But... who checks on me? Ah, sorry, you already do, don't you?",
        "reply1": ("That's what friends are for._F+0.2", "0"),
        "reply2": ("You don't always have to be the strong one. Let me take care of you._R+0.8", "80R100")
    },
    "ISTJ": {
        "npc": "I prefer certainty. Rules, schedules, logic. But you... you are an unpredictable variable I don't want to remove.",
        "reply1": ("I'll try to be less chaotic._F+0.2", "0"),
        "reply2": ("Some things are worth breaking the rules for._R+0.8", "80R100")
    },
    "ENFP": {
        "npc": "There's a whole world out there waiting for us! But honestly? Right here, with you... this is my favorite adventure.",
        "reply1": ("We should travel more._F+0.2", "0"),
        "reply2": ("Anywhere we go, as long as we're together, is a perfect adventure._R+0.8", "80R100")
    },
    "ENFJ": {
        "npc": "I try to guide others, to be the light they need. But sometimes... I just need someone to hold my hand in the dark.",
        "reply1": ("You're doing a great job._F+0.2", "0"),
        "reply2": ("I'll be your light when you're tired of shining._R+0.8", "80R100")
    },
    "ENTP": {
        "npc": "I can argue any side of a debate just for fun. But there's one thing I won't ever argue against... and that's you.",
        "reply1": ("You just don't want to lose._F+0.2", "0"),
        "reply2": ("I guess you finally met your match._R+0.8", "80R100")
    },
    "INTP": {
        "npc": "I've analyzed countless systems, but the way I feel when you're around... it defies all logic.",
        "reply1": ("You just need more data._F+0.2", "0"),
        "reply2": ("Some things aren't meant to be analyzed, just felt._R+0.8", "80R100")
    },
    "ESTJ": {
        "npc": "Efficiency is key. Time wasted is time lost. Yet, spending time with you never feels like a waste.",
        "reply1": ("I'm glad I'm productive for you._F+0.2", "0"),
        "reply2": ("I'll gladly take up all of your free time._R+0.8", "80R100")
    },
    "ESFP": {
        "npc": "Life is a stage, and I love being in the spotlight! But lately, I only care if you're in the audience.",
        "reply1": ("I'll clap for you._F+0.2", "0"),
        "reply2": ("I'll always be cheering for you from the front row._R+0.8", "80R100")
    },
    "INFJ": {
        "npc": "I see beneath the surface of people. It's exhausting. But with you... your soul is a place of rest.",
        "reply1": ("I'm glad you feel comfortable._F+0.2", "0"),
        "reply2": ("You don't have to carry the weight of the world alone anymore._R+0.8", "80R100")
    },
    "ENTJ": {
        "npc": "I conquer objectives. I build empires. But of all my ambitions, standing by your side is the greatest one.",
        "reply1": ("You always set your sights high._F+0.2", "0"),
        "reply2": ("We'll conquer the world together._R+0.8", "80R100")
    },
    "ISTP": {
        "npc": "I like fixing things. Making them work. But you... you're perfectly fine just the way you are.",
        "reply1": ("Thanks, I guess?_F+0.2", "0"),
        "reply2": ("And you're the only one I'd let into my heart's engine room._R+0.8", "80R100")
    },
    "ESTP": {
        "npc": "I live for the thrill, the action, the moment! But strangely, my heart races the fastest when I'm just sitting next to you.",
        "reply1": ("That's probably just adrenaline._F+0.2", "0"),
        "reply2": ("Then let's enjoy the quiet thrill of just being here._R+0.8", "80R100")
    },
    "ISFP": {
        "npc": "I express myself better through what I create than what I say. But if I had to paint you... I'd run out of colors.",
        "reply1": ("You should use more vibrant paints._F+0.2", "0"),
        "reply2": ("You are the most beautiful masterpiece in my world._R+0.8", "80R100")
    }
}

# Read existing talk data to find length
with open(talk_path, 'r', encoding='utf-16', errors='replace') as f:
    talk_rows = list(csv.reader(f))

# Header is row 0
header = talk_rows[0]

new_rows = []
row_idx = len(talk_rows)
# Add new rows for each character
for name, mbti in mbtis.items():
    if mbti in mbti_dialogs:
        d = mbti_dialogs[mbti]
        
        row_name = f"{name}_MBTI_Talk"
        category = "Relationship"
        
        # Details format: NSLOCTEXT("GUID", "Key", "Text")
        # I'll just use a generic format to ensure UE parses it nicely or just plain text if they use that. 
        # But looking at existing: NSLOCTEXT("[...]", "...", "Hey...")
        details = f'NSLOCTEXT("MBTI_Talk_Gen", "MBTI_Talk_{name}", "{d["npc"]}")'
        
        # AnswerCondition format: (("Answer1", "Condition1"),("Answer2", "Condition2"))
        # Example: (("I'm good._F+0.3", "0"),("..._R+0.8", "80R100"))
        # Note: Must properly escape inner quotes if needed.
        # Format string directly:
        a1, c1 = d["reply1"]
        a2, c2 = d["reply2"]
        # Because we write to CSV via csv.writer, the writer handles quotes automatically.
        # But the inner string itself must match Unreal's tuple format: (("Text", "Cond"), ("Text", "Cond"))
        ans_cond = f'(("{a1}", "{c1}"),("{a2}", "{c2}"))'
        
        new_row = [
            row_name,          # ---
            row_name,          # RowName
            category,          # Category
            details,           # Details
            ans_cond,          # AnswerCondition
            "",                # RequestQuest
            "-100.000000",     # RequiredFreindship
            "80.000000"        # RequiredRelationship
        ]
        
        new_rows.append(new_row)

# Append to file using utf-16 to preserve original encoding. 
# Wait, let's write the whole file to make sure it's clean.
talk_rows.extend(new_rows)

with open(talk_path, 'w', encoding='utf-16', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(talk_rows)

print(f"Added {len(new_rows)} MBTI specific dialogues to NPC_TalkData_DT.csv!")
