"""
Dream Symbol Database — 周公解梦 + Modern Interpretations
"""

SYMBOLS = {
    # === 动物 Animals ===
    "蛇": {
        "en": "snake",
        "category": "动物",
        "traditional": "蛇为小龙，梦蛇多主财运、智慧。被蛇咬则可能有小人。",
        "modern": "May represent hidden fears, transformation, or temptation.",
        "fortune": "吉凶参半",
        "keywords": ["snake", "serpent", "蛇"]
    },
    "狗": {
        "en": "dog",
        "category": "动物",
        "traditional": "狗为忠诚之兽，梦狗主朋友、忠诚。狗咬人则可能有口舌之争。",
        "modern": "Represents loyalty, friendship, or protection instincts.",
        "fortune": "吉",
        "keywords": ["dog", "puppy", "狗", "犬"]
    },
    "龙": {
        "en": "dragon",
        "category": "动物",
        "traditional": "龙为帝王之象，大吉！主事业腾飞、贵人相助。",
        "modern": "Symbol of power, success, and ambition.",
        "fortune": "大吉",
        "keywords": ["dragon", "龙"]
    },
    "猫": {
        "en": "cat",
        "category": "动物",
        "traditional": "猫主独立、神秘。梦猫可能有女性贵人，或需防小人。",
        "modern": "Independence, intuition, feminine energy.",
        "fortune": "中",
        "keywords": ["cat", "kitten", "猫"]
    },
    "鱼": {
        "en": "fish",
        "category": "动物",
        "traditional": "鱼通'余'，年年有余！梦鱼主财运、富足。",
        "modern": "Abundance, fertility, the unconscious mind.",
        "fortune": "吉",
        "keywords": ["fish", "鱼"]
    },
    "鸟": {
        "en": "bird",
        "category": "动物",
        "traditional": "鸟主自由、消息。梦鸟飞主好消息将至。",
        "modern": "Freedom, perspective, messages from the subconscious.",
        "fortune": "吉",
        "keywords": ["bird", "鸟"]
    },

    # === 自然 Nature ===
    "水": {
        "en": "water",
        "category": "自然",
        "traditional": "水主财。清水为财运，浑水需谨慎。大水/洪水主大变动。",
        "modern": "Emotions, the unconscious, cleansing or overwhelm.",
        "fortune": "视情况",
        "keywords": ["water", "river", "ocean", "水", "河", "海"]
    },
    "火": {
        "en": "fire",
        "category": "自然",
        "traditional": "火主兴旺。梦火烧主事业红火，但需防冲动。",
        "modern": "Passion, transformation, anger, or creativity.",
        "fortune": "吉凶参半",
        "keywords": ["fire", "flame", "火", "焰"]
    },
    "山": {
        "en": "mountain",
        "category": "自然",
        "traditional": "山主稳重、障碍。爬山成功主克服困难。",
        "modern": "Challenges, goals, stability, obstacles to overcome.",
        "fortune": "中",
        "keywords": ["mountain", "hill", "山"]
    },
    "雨": {
        "en": "rain",
        "category": "自然",
        "traditional": "雨主恩泽、润泽。梦雨多为吉兆，滋润万物。",
        "modern": "Cleansing, renewal, sadness, or fertility.",
        "fortune": "吉",
        "keywords": ["rain", "雨"]
    },
    "雪": {
        "en": "snow",
        "category": "自然",
        "traditional": "雪主纯洁、瑞雪兆丰年。但也可能暗示冷淡。",
        "modern": "Purity, isolation, emotional coldness, or fresh start.",
        "fortune": "吉",
        "keywords": ["snow", "雪"]
    },

    # === 人物 People ===
    "死人": {
        "en": "dead person",
        "category": "人物",
        "traditional": "梦见死人反为吉！主长寿、旧事了结。死去的亲人托梦要注意。",
        "modern": "Endings, transformation, unresolved feelings about the person.",
        "fortune": "吉",
        "keywords": ["dead", "death", "deceased", "死", "亡"]
    },
    "婴儿": {
        "en": "baby",
        "category": "人物",
        "traditional": "婴儿主新生、希望。梦婴儿主新开始或好消息。",
        "modern": "New beginnings, innocence, vulnerability, new projects.",
        "fortune": "吉",
        "keywords": ["baby", "infant", "婴儿", "宝宝"]
    },
    "陌生人": {
        "en": "stranger",
        "category": "人物",
        "traditional": "陌生人可能代表自己未知的一面，或即将遇到的贵人/小人。",
        "modern": "Unknown aspects of yourself, new opportunities or threats.",
        "fortune": "中",
        "keywords": ["stranger", "unknown person", "陌生人"]
    },

    # === 物品 Objects ===
    "棺材": {
        "en": "coffin",
        "category": "物品",
        "traditional": "大吉！棺材 = 官财（升官发财）。棺材入宅主财运进门。",
        "modern": "Endings leading to new beginnings, transformation.",
        "fortune": "大吉",
        "keywords": ["coffin", "棺材", "棺"]
    },
    "钱": {
        "en": "money",
        "category": "物品",
        "traditional": "梦钱不一定主财。捡钱可能漏财，丢钱反而可能得财。",
        "modern": "Self-worth, power, anxiety about resources.",
        "fortune": "视情况",
        "keywords": ["money", "cash", "钱", "金钱"]
    },
    "镜子": {
        "en": "mirror",
        "category": "物品",
        "traditional": "镜子主自省、真相。破镜则需防口舌或分离。",
        "modern": "Self-reflection, truth, vanity, or self-image issues.",
        "fortune": "中",
        "keywords": ["mirror", "镜子", "镜"]
    },
    "车": {
        "en": "car",
        "category": "物品",
        "traditional": "车主前进、事业。开车顺利主事业顺遂。",
        "modern": "Life direction, control, ambition, journey.",
        "fortune": "吉",
        "keywords": ["car", "vehicle", "车"]
    },
    "房子": {
        "en": "house",
        "category": "物品",
        "traditional": "房子主自身。新房主新生活，旧房主怀旧或需改变。",
        "modern": "The self, security, family, different rooms = different aspects of psyche.",
        "fortune": "中",
        "keywords": ["house", "home", "房子", "房", "屋"]
    },

    # === 动作 Actions ===
    "飞": {
        "en": "flying",
        "category": "动作",
        "traditional": "飞主高升、自由。飞得高主志向远大，但需防骄傲。",
        "modern": "Freedom, escape, ambition, transcending limitations.",
        "fortune": "吉",
        "keywords": ["fly", "flying", "飞", "飞翔"]
    },
    "掉牙": {
        "en": "losing teeth",
        "category": "动作",
        "traditional": "传统认为掉牙主亲人健康需注意。但也可能主蜕变。",
        "modern": "Anxiety about appearance, aging, loss of control, major life changes.",
        "fortune": "需注意",
        "keywords": ["teeth", "losing teeth", "tooth", "掉牙", "牙"]
    },
    "跑": {
        "en": "running",
        "category": "动作",
        "traditional": "跑主追求或逃避。追人主有所求，被追主有压力。",
        "modern": "Pursuit of goals, escaping problems, anxiety.",
        "fortune": "中",
        "keywords": ["run", "running", "chase", "跑", "追"]
    },
    "哭": {
        "en": "crying",
        "category": "动作",
        "traditional": "梦哭反主喜！哭得越厉害，喜事越大。",
        "modern": "Emotional release, sadness, or joy in disguise.",
        "fortune": "吉",
        "keywords": ["cry", "crying", "tears", "哭", "泪"]
    },
    "考试": {
        "en": "exam",
        "category": "动作",
        "traditional": "考试主被评判、压力。考得好主顺利，考砸需自省。",
        "modern": "Fear of judgment, self-evaluation, imposter syndrome.",
        "fortune": "中",
        "keywords": ["exam", "test", "考试", "测试"]
    },
    "结婚": {
        "en": "wedding",
        "category": "动作",
        "traditional": "梦结婚主人生新阶段、承诺。未婚者梦此可能有姻缘。",
        "modern": "Commitment, union of different aspects of self, new phase.",
        "fortune": "吉",
        "keywords": ["wedding", "marriage", "marry", "结婚", "婚礼"]
    },
    "怀孕": {
        "en": "pregnancy",
        "category": "动作",
        "traditional": "怀孕主新生、创造。可能有新计划或创意。",
        "modern": "Creativity, new ideas, development, anticipation.",
        "fortune": "吉",
        "keywords": ["pregnant", "pregnancy", "怀孕"]
    },
}

# Fortune ratings explanation
FORTUNE_LEVELS = {
    "大吉": ("🌟🌟🌟", "Extremely auspicious! Great fortune ahead."),
    "吉": ("🌟🌟", "Auspicious. Good things coming."),
    "中": ("🌟", "Neutral. Depends on context."),
    "需注意": ("⚠️", "Needs attention. Be cautious."),
    "吉凶参半": ("🌓", "Mixed fortune. Both good and bad aspects."),
    "视情况": ("🔮", "Depends on dream details."),
}

def search_symbol(query: str) -> list:
    """Search for symbols matching the query."""
    query = query.lower().strip()
    results = []
    
    for key, data in SYMBOLS.items():
        # Check if query matches any keyword
        keywords = [k.lower() for k in data.get("keywords", [])]
        if query in keywords or query == key.lower() or query == data.get("en", "").lower():
            results.append((key, data))
    
    # Fuzzy match if no exact results
    if not results:
        for key, data in SYMBOLS.items():
            keywords = " ".join(data.get("keywords", [])).lower()
            if query in keywords or query in key.lower() or query in data.get("en", "").lower():
                results.append((key, data))
    
    return results
