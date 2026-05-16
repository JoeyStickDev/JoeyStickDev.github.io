import csv

mbti_path = r"f:\Git\JoeyStickDev.github.io\Temp\NPC_MBTI_DT.csv"
talk_path = r"f:\Git\JoeyStickDev.github.io\Temp\NPC_TalkData_DT.csv"

mbtis = {}
with open(mbti_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if len(row) >= 3:
            mbtis[row[1]] = row[2]

# Template format: 
# "Category": [
#   {"npc": "dialogue", "ans1": ("reply1", "cond1"), "ans2": ("reply2", "cond2")} x 3
# ]

templates = {
    "INTJ": {
        "Friendship": [
            {"npc": "It is rare for me to find someone whose presence is not a distraction. You are... tolerable.", "ans1": ("Thanks, I think?_F+0.2", "0"), "ans2": ("I enjoy your presence too._F+0.5", "30R100")},
            {"npc": "I was reviewing my plans for the future. You seem to appear in several of them.", "ans1": ("Glad I could help._F+0.2", "0"), "ans2": ("I hope I'm in the good plans._F+0.5", "30R100")},
            {"npc": "Small talk is inefficient. But with you, I suppose I can make an exception.", "ans1": ("I appreciate it._F+0.2", "0"), "ans2": ("Let's make it a regular thing._F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "I have run the calculations multiple times. My feelings for you defy logic.", "ans1": ("Maybe logic isn't everything._F+0.2", "0"), "ans2": ("Then let's stop calculating and start feeling._R+0.8", "80R100")},
            {"npc": "I do not easily let people into my world. Yet, I find myself leaving the door open for you.", "ans1": ("I'll be careful._F+0.2", "0"), "ans2": ("I'm never leaving._R+0.8", "80R100")},
            {"npc": "You are the only variable I want to keep constant in my life.", "ans1": ("That's sweet of you._F+0.2", "0"), "ans2": ("And you are my constant._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "Did you move my items? The spatial arrangement is exactly 2 millimeters off.", "ans1": ("Wasn't me._F+0.1", "0"), "ans2": ("Maybe I did it just to test you._F+0.3", "30R100")},
            {"npc": "I have devised a foolproof strategy for avoiding socializing today. You are the only flaw.", "ans1": ("I'll leave then._F+0.0", "0"), "ans2": ("I'm the best kind of flaw._F+0.4", "30R100")},
            {"npc": "If you are trying to annoy me, your success rate is currently hovering at 5%.", "ans1": ("I'll try harder._F+0.2", "0"), "ans2": ("I'm aiming for 100% affection instead._F+0.5", "30R100")}
        ]
    },
    "INFP": {
        "Friendship": [
            {"npc": "I was just daydreaming about a faraway place... but the real world is nice when you're here.", "ans1": ("Daydreaming is fun._F+0.2", "0"), "ans2": ("We can explore the real world together._F+0.5", "30R100")},
            {"npc": "Sometimes words get stuck in my throat. Thank you for understanding my silence.", "ans1": ("No problem._F+0.2", "0"), "ans2": ("I'll always listen, even to your silence._F+0.5", "30R100")},
            {"npc": "Have you ever felt like you belong to another time? I do, often. But right now feels okay.", "ans1": ("Yeah, I get that._F+0.2", "0"), "ans2": ("I'm glad we share this time._F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "In all my stories and dreams, I never imagined someone as wonderful as you.", "ans1": ("You're too kind._F+0.2", "0"), "ans2": ("You are my dream come true._R+0.8", "80R100")},
            {"npc": "When I hold your hand, all the noise of the world just fades away.", "ans1": ("It's peaceful._F+0.2", "0"), "ans2": ("I'll always hold your hand._R+0.8", "80R100")},
            {"npc": "I wrote a poem about you. It's not finished, because my feelings keep growing.", "ans1": ("I'd love to read it._F+0.2", "0"), "ans2": ("Let's write the rest of the story together._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "I tried to talk to a bird today. I think it judged my outfit.", "ans1": ("Birds can be mean._F+0.2", "0"), "ans2": ("I think your outfit is perfect._F+0.4", "30R100")},
            {"npc": "If I hide under this blanket, do you think Monday will forget to find me?", "ans1": ("Probably not._F+0.0", "0"), "ans2": ("I'll hide under there with you._F+0.5", "30R100")},
            {"npc": "I tripped over a shadow earlier. I apologized to it.", "ans1": ("That's very polite of you._F+0.2", "0"), "ans2": ("You are too pure for this world._F+0.4", "30R100")}
        ]
    },
    "ISFJ": {
        "Friendship": [
            {"npc": "Have you eaten today? Please make sure to take care of yourself.", "ans1": ("I will, thanks._F+0.2", "0"), "ans2": ("Only if you take care of yourself too._F+0.5", "30R100")},
            {"npc": "If you ever need a place to rest, you can always come to me.", "ans1": ("That's reassuring._F+0.2", "0"), "ans2": ("You're my favorite resting place._F+0.5", "30R100")},
            {"npc": "I remembered you liked this, so I kept it aside for you.", "ans1": ("Oh, thank you!_F+0.3", "0"), "ans2": ("You always pay attention to the little things._F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "I spend so much time taking care of others. But looking at you... I want you to be the one I cherish most.", "ans1": ("You're so sweet._F+0.2", "0"), "ans2": ("Then let me be the one who cherishes you._R+0.8", "80R100")},
            {"npc": "Your smile makes all my hard work feel completely worth it.", "ans1": ("I'm glad._F+0.2", "0"), "ans2": ("And your smile is my greatest reward._R+0.8", "80R100")},
            {"npc": "I don't need grand gestures. Just sitting here with you is all I ever wanted.", "ans1": ("It's nice and quiet._F+0.2", "0"), "ans2": ("I'll stay by your side forever._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "I accidentally organized my socks by color and mood. Is that weird?", "ans1": ("A little bit._F+0.1", "0"), "ans2": ("I'd expect nothing less from you._F+0.4", "30R100")},
            {"npc": "I brought an umbrella, a coat, and a snack. Just in case the weather changes indoors.", "ans1": ("Better safe than sorry._F+0.2", "0"), "ans2": ("You're basically a walking survival kit._F+0.4", "30R100")},
            {"npc": "Please don't tell anyone, but I sometimes practice my 'surprised face' in the mirror.", "ans1": ("Your secret is safe with me._F+0.2", "0"), "ans2": ("Show me! I promise I won't laugh._F+0.5", "30R100")}
        ]
    },
    "ISTJ": {
        "Friendship": [
            {"npc": "Consistency is important. I appreciate that I can rely on you.", "ans1": ("I try my best._F+0.2", "0"), "ans2": ("You can always count on me._F+0.5", "30R100")},
            {"npc": "My schedule is quite rigid, but I have allocated some free time for our conversation.", "ans1": ("Thanks for fitting me in._F+0.2", "0"), "ans2": ("I'm honored to be in your schedule._F+0.5", "30R100")},
            {"npc": "A well-maintained tool lasts a lifetime. Friendships require the same maintenance.", "ans1": ("Agreed._F+0.2", "0"), "ans2": ("I'll make sure to keep our friendship in top shape._F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "You are the one exception to my rules. And I am entirely okay with that.", "ans1": ("I'm glad._F+0.2", "0"), "ans2": ("I'll be your favorite rule to break._R+0.8", "80R100")},
            {"npc": "I've planned out my future, but the most important part is that you are in it.", "ans1": ("That means a lot._F+0.2", "0"), "ans2": ("I wouldn't want to be anywhere else._R+0.8", "80R100")},
            {"npc": "My loyalty is not given lightly. But to you, it is absolute.", "ans1": ("I won't let you down._F+0.2", "0"), "ans2": ("And you have mine, completely._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "I tried to be spontaneous once. I scheduled it for 3 PM on a Tuesday.", "ans1": ("That defeats the purpose._F+0.1", "0"), "ans2": ("How did that work out for you?_F+0.4", "30R100")},
            {"npc": "Someone told me to 'go with the flow'. I asked them for the flow's trajectory and velocity.", "ans1": ("Classic._F+0.2", "0"), "ans2": ("I think you missed the point, but I love it._F+0.5", "30R100")},
            {"npc": "I have exactly three jokes. I rotate them monthly to maintain comedic efficiency.", "ans1": ("Let's hear one._F+0.2", "0"), "ans2": ("You are hilarious without even trying._F+0.4", "30R100")}
        ]
    },
    "ENFP": {
        "Friendship": [
            {"npc": "I have a million ideas today! Do you want to hear the craziest one?", "ans1": ("Sure, tell me._F+0.2", "0"), "ans2": ("I'm ready for whatever you've got!_F+0.5", "30R100")},
            {"npc": "Just seeing you makes me feel so energized! Let's do something fun!", "ans1": ("What do you have in mind?_F+0.2", "0"), "ans2": ("Any time spent with you is fun._F+0.5", "30R100")},
            {"npc": "I love how we can talk about anything from clouds to the meaning of life.", "ans1": ("Me too._F+0.2", "0"), "ans2": ("There's never a dull moment with you._F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "Of all the adventures I've imagined, falling for you is the most exciting one.", "ans1": ("I feel the same._F+0.2", "0"), "ans2": ("Let's make this adventure last forever._R+0.8", "80R100")},
            {"npc": "You feel like home, but also like the most exciting journey. How do you do that?", "ans1": ("It's my secret._F+0.2", "0"), "ans2": ("It's because you bring out the best in me._R+0.8", "80R100")},
            {"npc": "I could explore the whole universe, but I'd still choose to be right by your side.", "ans1": ("That's very sweet._F+0.2", "0"), "ans2": ("You are my entire universe._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "I was going to be responsible today, but then a butterfly distracted me.", "ans1": ("Happens to the best of us._F+0.2", "0"), "ans2": ("I'll be your designated responsibility buddy._F+0.4", "30R100")},
            {"npc": "If we run fast enough, do you think we can outrun Monday?", "ans1": ("No._F+0.0", "0"), "ans2": ("Let's hold hands and try!_F+0.5", "30R100")},
            {"npc": "I put my shoes on the wrong feet today to see what it felt like. 0/10, do not recommend.", "ans1": ("Why would you do that?_F+0.1", "0"), "ans2": ("Your curiosity knows no bounds._F+0.4", "30R100")}
        ]
    },
    "ENFJ": {
        "Friendship": [
            {"npc": "Seeing you smile brightens up my whole day. Is there anything I can help you with?", "ans1": ("I'm good, thanks._F+0.2", "0"), "ans2": ("Just your company is enough._F+0.5", "30R100")},
            {"npc": "You have so much potential. I believe in you more than you know.", "ans1": ("Thank you._F+0.2", "0"), "ans2": ("Your support means everything to me._F+0.5", "30R100")},
            {"npc": "When people come together, amazing things happen. I'm glad we're friends.", "ans1": ("Me too._F+0.2", "0"), "ans2": ("We make a great team._F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "I've spent my life guiding others to happiness. But with you, I've finally found my own.", "ans1": ("I'm happy for you._F+0.2", "0"), "ans2": ("You deserve all the happiness in the world._R+0.8", "80R100")},
            {"npc": "When I look into your eyes, I see a future so bright it takes my breath away.", "ans1": ("That's beautiful._F+0.2", "0"), "ans2": ("Let's build that future together._R+0.8", "80R100")},
            {"npc": "You give me the strength to be a better person. I love you deeply.", "ans1": ("I care about you too._F+0.2", "0"), "ans2": ("You are already perfect to me._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "I tried to give a motivational speech to a rock. It remained uninspired.", "ans1": ("Rocks are tough crowds._F+0.2", "0"), "ans2": ("I'm sure it felt it on the inside._F+0.4", "30R100")},
            {"npc": "I accidentally hugged a stranger today because they looked sad. They were just looking at their phone.", "ans1": ("That's awkward._F+0.1", "0"), "ans2": ("Your heart is too big for your own good._F+0.5", "30R100")},
            {"npc": "If kindness was a currency, I'd probably still be broke because I'd give it all away.", "ans1": ("That's true._F+0.2", "0"), "ans2": ("I'll make sure you're rich in love._F+0.5", "30R100")}
        ]
    },
    "ENTP": {
        "Friendship": [
            {"npc": "I have a theory that everything is connected. Care to debate me on it?", "ans1": ("Not right now._F+0.1", "0"), "ans2": ("Bring it on!_F+0.5", "30R100")},
            {"npc": "Rules are basically just suggestions, right? Let's bend a few.", "ans1": ("Let's not get in trouble._F+0.2", "0"), "ans2": ("I'm right behind you._F+0.5", "30R100")},
            {"npc": "You're one of the few people who can actually keep up with my train of thought.", "ans1": ("It's not easy._F+0.2", "0"), "ans2": ("It's a wild ride, but I love it._F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "I usually get bored easily, but with you... every single day is fascinating.", "ans1": ("I'm glad._F+0.2", "0"), "ans2": ("I promise to never let you get bored._R+0.8", "80R100")},
            {"npc": "I can argue about anything in the world, except how much you mean to me.", "ans1": ("That's surprisingly sweet._F+0.2", "0"), "ans2": ("You finally conceded a point._R+0.8", "80R100")},
            {"npc": "You challenged my intellect, and ended up capturing my heart.", "ans1": ("I'm a good strategist._F+0.2", "0"), "ans2": ("And you've completely captured mine._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "I played devil's advocate so well yesterday, I think the devil owes me a favor.", "ans1": ("You probably shouldn't collect it._F+0.2", "0"), "ans2": ("Can you get him to do my chores?_F+0.5", "30R100")},
            {"npc": "If someone tells me not to push a button, that button instantly becomes my sole purpose in life.", "ans1": ("You have no self-control._F+0.1", "0"), "ans2": ("I'll make sure to put warning labels on myself._F+0.4", "30R100")},
            {"npc": "I convinced someone that water is dry. My persuasion skills are terrifying.", "ans1": ("That's just lying._F+0.1", "0"), "ans2": ("Use your powers for good!_F+0.4", "30R100")}
        ]
    },
    "INTP": {
        "Friendship": [
            {"npc": "I was researching a highly obscure topic until 4 AM. Anyway, hi.", "ans1": ("You should sleep more._F+0.2", "0"), "ans2": ("Tell me what you learned._F+0.5", "30R100")},
            {"npc": "Your logical consistency is surprisingly high for a human. I appreciate that.", "ans1": ("Thanks._F+0.2", "0"), "ans2": ("I consider that a high compliment from you._F+0.5", "30R100")},
            {"npc": "I don't usually initiate social protocols, but... I'm glad you're here.", "ans1": ("Good to see you too._F+0.2", "0"), "ans2": ("I'm always happy to see you._F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "I've tried to quantify my affection for you, but the numbers keep breaking the scale.", "ans1": ("Math can't solve everything._F+0.2", "0"), "ans2": ("My love for you is infinite too._R+0.8", "80R100")},
            {"npc": "You are the most beautiful, complex anomaly I have ever encountered.", "ans1": ("I'll take that as a compliment._F+0.2", "0"), "ans2": ("I hope you spend your life studying me._R+0.8", "80R100")},
            {"npc": "I used to prefer solitude. Now, solitude just feels like waiting for you.", "ans1": ("I'm here now._F+0.2", "0"), "ans2": ("You'll never have to wait long._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "I tried to explain string theory to a cat. It just purred. Clearly, it already knew.", "ans1": ("Cats are smart._F+0.2", "0"), "ans2": ("Or it was mocking your simplistic explanation._F+0.5", "30R100")},
            {"npc": "I forgot to eat today because I was optimizing my workflow for remembering to eat.", "ans1": ("That is deeply ironic._F+0.2", "0"), "ans2": ("Let's go get some food right now._F+0.5", "30R100")},
            {"npc": "I have 47 tabs open in my brain and I don't know where the music is coming from.", "ans1": ("Close a few tabs._F+0.2", "0"), "ans2": ("Just dance to it._F+0.5", "30R100")}
        ]
    },
    "ESTJ": {
        "Friendship": [
            {"npc": "I've optimized our interaction time to maximize productivity and morale.", "ans1": ("Uh, thanks._F+0.1", "0"), "ans2": ("I'm ready for efficiency!_F+0.4", "30R100")},
            {"npc": "If everyone was as reliable as you, the world would run like clockwork.", "ans1": ("I do what I can._F+0.2", "0"), "ans2": ("Coming from you, that means a lot._F+0.5", "30R100")},
            {"npc": "I have a plan for today. Let me know if you want to be included.", "ans1": ("I'm busy, sorry._F+0.0", "0"), "ans2": ("I'd love to join your plan._F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "I usually demand control, but with you, I'm perfectly happy surrendering it.", "ans1": ("That's new for you._F+0.2", "0"), "ans2": ("I'll take good care of your heart._R+0.8", "80R100")},
            {"npc": "You are the greatest achievement of my life, and I didn't even have to plan it.", "ans1": ("I'm glad it happened._F+0.2", "0"), "ans2": ("Some things are better left unplanned._R+0.8", "80R100")},
            {"npc": "I will protect you, provide for you, and love you efficiently and endlessly.", "ans1": ("That's very reassuring._F+0.2", "0"), "ans2": ("I will do the same for you._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "I scheduled five minutes of unstructured fun today. It was exhausting.", "ans1": ("You need to relax._F+0.2", "0"), "ans2": ("Let's schedule five more minutes together._F+0.5", "30R100")},
            {"npc": "Someone told me to 'chill out'. I have added 'chill out' to my to-do list.", "ans1": ("That's not how it works._F+0.2", "0"), "ans2": ("I can help you cross that off._F+0.5", "30R100")},
            {"npc": "If I look stressed, it's because someone folded the towels incorrectly.", "ans1": ("It's just towels._F+0.1", "0"), "ans2": ("I'll go fix them for you._F+0.5", "30R100")}
        ]
    },
    "ESFP": {
        "Friendship": [
            {"npc": "Did someone say fun? Because I brought the energy!", "ans1": ("Let's go!_F+0.3", "0"), "ans2": ("I can always count on you for a good time._F+0.5", "30R100")},
            {"npc": "You look like you need a distraction. Good thing I'm here!", "ans1": ("I really do._F+0.2", "0"), "ans2": ("You're my favorite distraction._F+0.5", "30R100")},
            {"npc": "I love your vibe! We should totally hang out more.", "ans1": ("Sure thing._F+0.2", "0"), "ans2": ("I'm free whenever you are._F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "I love being the center of attention, but all I want is your attention.", "ans1": ("You have it._F+0.2", "0"), "ans2": ("My eyes are only on you._R+0.8", "80R100")},
            {"npc": "Life is a party, and you are the VIP guest of my heart.", "ans1": ("That's cheesy but sweet._F+0.2", "0"), "ans2": ("I never want this party to end._R+0.8", "80R100")},
            {"npc": "You make every normal day feel like an absolute celebration.", "ans1": ("I'm glad you feel that way._F+0.2", "0"), "ans2": ("Every day with you is a gift._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "I tried to be quiet today. I lasted exactly twelve seconds.", "ans1": ("A new record!_F+0.2", "0"), "ans2": ("I like you loud and happy anyway._F+0.5", "30R100")},
            {"npc": "I bought glitter. I don't know what for yet, but everyone is in danger.", "ans1": ("Please keep it away from me._F+0.0", "0"), "ans2": ("Let's bedazzle everything!_F+0.5", "30R100")},
            {"npc": "My thought process is just upbeat background music and sudden impulses.", "ans1": ("Sounds chaotic._F+0.1", "0"), "ans2": ("That's exactly why I love being around you._F+0.5", "30R100")}
        ]
    },
    "INFJ": {
        "Friendship": [
            {"npc": "I can sense you have a lot on your mind. You don't have to say it, just know I'm here.", "ans1": ("Thanks._F+0.2", "0"), "ans2": ("Your presence always calms me._F+0.5", "30R100")},
            {"npc": "Most interactions drain me, but talking with you actually restores my energy.", "ans1": ("I'm glad to help._F+0.2", "0"), "ans2": ("I feel the same way about you._F+0.5", "30R100")},
            {"npc": "You have a beautiful aura today. The colors are very warm.", "ans1": ("I didn't know I had an aura._F+0.2", "0"), "ans2": ("It must be because I'm with you._F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "I have spent my life looking for a soul that understands mine. I found it in you.", "ans1": ("I understand you._F+0.2", "0"), "ans2": ("Our souls are intertwined forever._R+0.8", "80R100")},
            {"npc": "I don't just love you for who you are, but for the depth of what we share.", "ans1": ("It's very special._F+0.2", "0"), "ans2": ("We have a bond that nothing can break._R+0.8", "80R100")},
            {"npc": "When the world is too loud, you are the only sanctuary I seek.", "ans1": ("I'll always protect you._F+0.2", "0"), "ans2": ("Come here, let me hold you._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "I overthought a conversation I had three years ago. I think I finally have the right comeback.", "ans1": ("A bit late for that._F+0.2", "0"), "ans2": ("Tell me, I'll pretend to be them._F+0.5", "30R100")},
            {"npc": "I stared into the void, and the void asked me to listen to its problems.", "ans1": ("You're too empathetic._F+0.2", "0"), "ans2": ("Even the void needs a therapist like you._F+0.5", "30R100")},
            {"npc": "I have a sixth sense. It mostly warns me when awkward situations are about to happen.", "ans1": ("Very useful._F+0.2", "0"), "ans2": ("Please use it to save us both._F+0.5", "30R100")}
        ]
    },
    "ENTJ": {
        "Friendship": [
            {"npc": "You have potential. Stick with me, and we'll accomplish great things.", "ans1": ("Sounds like a plan._F+0.2", "0"), "ans2": ("I'll follow your lead._F+0.5", "30R100")},
            {"npc": "I don't waste time on trivial matters. The fact that I'm talking to you means you matter.", "ans1": ("I'm honored._F+0.2", "0"), "ans2": ("I'll make sure it's worth your time._F+0.5", "30R100")},
            {"npc": "Obstacles are just stepping stones. What's our next target?", "ans1": ("Let's just relax today._F+0.1", "0"), "ans2": ("Whatever you have in mind!_F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "I demand excellence in all areas of my life. You exceed every expectation I ever had.", "ans1": ("I try my best._F+0.2", "0"), "ans2": ("You make me want to be my best self._R+0.8", "80R100")},
            {"npc": "I am not used to compromising, but for you, I would rewrite all my plans.", "ans1": ("You don't have to change for me._F+0.2", "0"), "ans2": ("Let's write a new plan together._R+0.8", "80R100")},
            {"npc": "You are the only person who can command my heart. Use that power wisely.", "ans1": ("I will._F+0.2", "0"), "ans2": ("I only command you to love me._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "I played a board game yesterday. I didn't just win, I acquired the other players' assets.", "ans1": ("That's... aggressive._F+0.1", "0"), "ans2": ("Remind me never to play Monopoly with you._F+0.5", "30R100")},
            {"npc": "I tried to delegate my emotional processing. Apparently, you have to do that yourself.", "ans1": ("Unfortunately, yes._F+0.2", "0"), "ans2": ("I can help you process them!_F+0.5", "30R100")},
            {"npc": "My resting face is just me calculating the most efficient way to conquer the room.", "ans1": ("It looks intimidating._F+0.1", "0"), "ans2": ("It's a very attractive resting face._F+0.5", "30R100")}
        ]
    },
    "ISTP": {
        "Friendship": [
            {"npc": "Hey. Need anything fixed? I've got my tools right here.", "ans1": ("Not right now, thanks._F+0.2", "0"), "ans2": ("Just you fixing my day by being here._F+0.5", "30R100")},
            {"npc": "Less talking, more doing. That's my motto. But talking to you isn't so bad.", "ans1": ("I'm glad._F+0.2", "0"), "ans2": ("I can be quiet if you want to just chill._F+0.5", "30R100")},
            {"npc": "I respect people who handle their own business. You do that well.", "ans1": ("Thanks._F+0.2", "0"), "ans2": ("I try, but I know I can count on you too._F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "I don't do well with emotions. But when I look at you, everything just... makes sense.", "ans1": ("I feel the same._F+0.2", "0"), "ans2": ("You don't need words. I know how you feel._R+0.8", "80R100")},
            {"npc": "You are the most essential part of my life. Don't ever break down on me.", "ans1": ("I won't._F+0.2", "0"), "ans2": ("If I do, I know you'll fix me._R+0.8", "80R100")},
            {"npc": "I'd rather show you I care than say it. So... just stay close to me.", "ans1": ("Okay._F+0.2", "0"), "ans2": ("I'm not going anywhere._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "If it ain't broke, take it apart anyway to see how it works. Then panic.", "ans1": ("That explains a lot._F+0.2", "0"), "ans2": ("Do you need help putting it back together?_F+0.5", "30R100")},
            {"npc": "I communicated my feelings today. I grunted twice instead of once.", "ans1": ("Progress._F+0.2", "0"), "ans2": ("I am fluent in your grunts._F+0.5", "30R100")},
            {"npc": "I accidentally bought another tool I already own. In my defense, this one is shinier.", "ans1": ("A classic mistake._F+0.2", "0"), "ans2": ("You can never have too many shiny tools._F+0.5", "30R100")}
        ]
    },
    "ESTP": {
        "Friendship": [
            {"npc": "Sitting around is boring! Let's go do something reckless!", "ans1": ("Maybe let's not._F+0.1", "0"), "ans2": ("Lead the way!_F+0.5", "30R100")},
            {"npc": "I bet I can beat you in a race to the town square. Loser buys drinks!", "ans1": ("You're on!_F+0.4", "0"), "ans2": ("I'm going to destroy you._F+0.5", "30R100")},
            {"npc": "You're fun to be around. You don't overthink things like everyone else.", "ans1": ("I just go with the flow._F+0.2", "0"), "ans2": ("I just try to keep up with you._F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "I've chased a lot of thrills in my life, but nothing gets my heart racing like you do.", "ans1": ("That's sweet._F+0.2", "0"), "ans2": ("Then let's keep this thrill going forever._R+0.8", "80R100")},
            {"npc": "I don't want to conquer the world anymore. I just want to conquer your heart.", "ans1": ("You already have._F+0.2", "0"), "ans2": ("It's completely yours._R+0.8", "80R100")},
            {"npc": "You are my favorite risk. And I'm going all in.", "ans1": ("I'm glad._F+0.2", "0"), "ans2": ("I'm betting my heart on you too._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "I thought about the consequences of my actions today. It took three whole seconds.", "ans1": ("You're maturing._F+0.2", "0"), "ans2": ("Don't overdo it, you'll hurt yourself._F+0.5", "30R100")},
            {"npc": "I don't have a short attention span, I just... oh hey, look at that!", "ans1": ("Focus._F+0.1", "0"), "ans2": ("Where?! Let's go check it out!_F+0.5", "30R100")},
            {"npc": "My survival instinct is just me doing something stupid and running very fast.", "ans1": ("It works, apparently._F+0.2", "0"), "ans2": ("I'll be right behind you running just as fast._F+0.5", "30R100")}
        ]
    },
    "ISFP": {
        "Friendship": [
            {"npc": "The colors in the sky are so vivid today. Do you see them too?", "ans1": ("Yeah, it's beautiful._F+0.2", "0"), "ans2": ("They look even better when I'm with you._F+0.5", "30R100")},
            {"npc": "I found this flower and thought of you. It has a quiet strength to it.", "ans1": ("Thank you._F+0.3", "0"), "ans2": ("I'll cherish it forever._F+0.5", "30R100")},
            {"npc": "I prefer to observe rather than speak, but your voice is my favorite sound.", "ans1": ("That's kind of you._F+0.2", "0"), "ans2": ("I love listening to you too._F+0.5", "30R100")}
        ],
        "Relationship": [
            {"npc": "If my heart were a canvas, you would be every single brushstroke.", "ans1": ("That's incredibly romantic._F+0.2", "0"), "ans2": ("You are the masterpiece of my life._R+0.8", "80R100")},
            {"npc": "I don't need the world to notice me. I only want to be seen by you.", "ans1": ("I see you._F+0.2", "0"), "ans2": ("I will always see the true you._R+0.8", "80R100")},
            {"npc": "You make me feel a kind of harmony I never knew existed.", "ans1": ("I'm glad._F+0.2", "0"), "ans2": ("Our hearts play the perfect melody._R+0.8", "80R100")}
        ],
        "Joke": [
            {"npc": "I tried to aggressively express my anger today. I ended up aggressively painting a sunset.", "ans1": ("Very intimidating._F+0.2", "0"), "ans2": ("I bet it's a beautiful sunset._F+0.5", "30R100")},
            {"npc": "I was going to socialize, but my cat fell asleep on my lap. The law is the law.", "ans1": ("You have your priorities straight._F+0.2", "0"), "ans2": ("I'll bring the socializing to you._F+0.5", "30R100")},
            {"npc": "If avoiding eye contact was an Olympic sport, I'd have a gold medal.", "ans1": ("You're getting better at it._F+0.2", "0"), "ans2": ("But you always look at me._F+0.5", "30R100")}
        ]
    }
}

# Ensure all MBTIs in data have a template. If an MBTI is not found, default to ISFJ for now
for k in mbtis.keys():
    if mbtis[k] not in templates:
        print(f"Warning: MBTI {mbtis[k]} for {k} not found in templates. Defaulting to ISFJ.")
        mbtis[k] = "ISFJ"

# Read existing talk rows
with open(talk_path, 'r', encoding='utf-16', errors='replace') as f:
    talk_rows = list(csv.reader(f))

new_rows = []

for name, mbti in mbtis.items():
    cats = templates[mbti]
    for cat_name, dialogues in cats.items():
        for i, d in enumerate(dialogues):
            row_name = f"{name}_{cat_name}_{i}"
            
            # Format details string
            # We want to avoid conflicts with UE formatting, standard is NSLOCTEXT
            details = f'NSLOCTEXT("{name}_Talk", "{row_name}", "{d["npc"]}")'
            
            # Format answer condition
            a1, c1 = d["ans1"]
            a2, c2 = d["ans2"]
            ans_cond = f'(("{a1}", "{c1}"),("{a2}", "{c2}"))'
            
            req_friend = "-100.000000"
            req_rel = "-100.000000"
            if cat_name == "Relationship":
                req_rel = "30.000000" # Some base requirement for relationship talks
            
            new_row = [
                row_name,          # ---
                row_name,          # RowName
                cat_name,          # Category
                details,           # Details
                ans_cond,          # AnswerCondition
                "",                # RequestQuest
                req_friend,        # RequiredFreindship
                req_rel            # RequiredRelationship
            ]
            new_rows.append(new_row)

talk_rows.extend(new_rows)

with open(talk_path, 'w', encoding='utf-16', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(talk_rows)

print(f"Added {len(new_rows)} new dialogue lines to NPC_TalkData_DT.csv!")
