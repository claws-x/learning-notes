#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日科普文章生成器
风格参考：卓克老师的科技参考
特点：实实在在、通俗易懂、有数据支撑、逻辑清晰
"""

import json
from datetime import datetime, timedelta

# 科普主题库
SCIENCE_TOPICS = [
    {
        "category": "健康科学",
        "topics": [
            {
                "title": "为什么我们需要睡眠？",
                "key_points": [
                    "睡眠占人生的 1/3 时间",
                    "深度睡眠时大脑在清理代谢废物",
                    "睡眠不足会增加阿尔茨海默病风险",
                    "成年人建议 7-9 小时睡眠"
                ],
                "data": "研究表明，连续 24 小时不睡觉，认知能力下降相当于血液酒精浓度 0.1%"
            },
            {
                "title": "咖啡因是如何提神的？",
                "key_points": [
                    "咖啡因阻断腺苷受体",
                    "效果持续 3-5 小时",
                    "下午 2 点后不建议摄入",
                    "个体差异很大"
                ],
                "data": "一杯咖啡 (200mg 咖啡因) 可以让反应时间提高 5-10%"
            }
        ]
    },
    {
        "category": "技术科普",
        "topics": [
            {
                "title": "AI 是如何工作的？",
                "key_points": [
                    "机器学习是模式识别",
                    "深度学习模拟人脑神经元",
                    "需要大量数据训练",
                    "AI 不会思考，只是统计"
                ],
                "data": "GPT-3 有 1750 亿个参数，训练成本超过 1000 万美元"
            },
            {
                "title": "区块链到底是什么？",
                "key_points": [
                    "分布式账本技术",
                    "不可篡改的数据链",
                    "去中心化的信任机制",
                    "应用场景有限"
                ],
                "data": "比特币网络每秒处理 7 笔交易，Visa 每秒处理 24000 笔"
            }
        ]
    },
    {
        "category": "生活科学",
        "topics": [
            {
                "title": "为什么手机越用越卡？",
                "key_points": [
                    "存储空间不足",
                    "后台应用占用内存",
                    "系统更新要求更高配置",
                    "电池老化影响性能"
                ],
                "data": "手机存储占用超过 80% 时，性能下降 30-50%"
            },
            {
                "title": "微波炉加热安全吗？",
                "key_points": [
                    "微波是非电离辐射",
                    "不会破坏食物营养",
                    "加热要均匀",
                    "某些容器不能微波"
                ],
                "data": "微波加热的营养保留率比水煮高 20-30%"
            }
        ]
    }
]

def generate_article(topic_data, date):
    """生成科普文章"""
    
    title = topic_data["title"]
    key_points = topic_data["key_points"]
    data = topic_data["data"]
    category = topic_data.get("category", "科普")
    
    article = f"""---
layout: post
title: "每日科普 | {title}"
date: {date.strftime('%Y-%m-%d')} 08:00:00 +0900
categories: [科普，{category}]
tags: [科普，科学，知识]
author: 六度空间
excerpt: "{data}"
---

AI 用起来，这里是六度空间学习之路。

---

## 📊 今日科普：{title}

{data}

---

## 🔬 核心要点

"""
    
    for i, point in enumerate(key_points, 1):
        article += f"""### {i}. {point}

这是本期的第一个要点。我们会用通俗易懂的方式来解释这个知识点。

"""
    
    article += f"""
## 💡 实际应用

了解这些知识后，我们可以在日常生活中应用：

1. **理性看待**：不盲从，不轻信
2. **科学决策**：基于事实做决定
3. **持续学习**：保持好奇心

---

## 📚 延伸阅读

- [相关研究论文](https://scholar.google.com)
- [科普维基百科](https://zh.wikipedia.org)
- [科学松鼠会](http://songshuhui.net)

---

## 🎯 小结

今天我们学习了关于"{title}"的知识。

**记住这个数据**：{data}

**实践建议**：将今天学到的知识应用到生活中。

---

**AI 用起来，这里是六度空间学习之路。**

**明天见！** 🚀

---

*本文风格参考卓克老师的科技参考，力求实实在在、通俗易懂。*
"""
    
    return article

def get_todays_topic():
    """获取今日主题 (按日期循环)"""
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    
    # 扁平化所有主题
    all_topics = []
    for category in SCIENCE_TOPICS:
        for topic in category["topics"]:
            topic["category"] = category["category"]
            all_topics.append(topic)
    
    # 循环选择
    topic_index = day_of_year % len(all_topics)
    return all_topics[topic_index]

def save_article(article, date):
    """保存文章到博客"""
    filename = f"/Users/aiagent_master/.openclaw/workspace-blog/_posts/{date.strftime('%Y-%m-%d')}-daily-science.md"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(article)
    
    print(f"✅ 文章已保存：{filename}")
    return filename

def main():
    """主函数"""
    today = datetime.now()
    
    # 获取今日主题
    topic = get_todays_topic()
    
    # 生成文章
    article = generate_article(topic, today)
    
    # 保存文章
    filename = save_article(article, today)
    
    # 输出信息
    print(f"📝 今日科普文章已生成")
    print(f"📄 主题：{topic['title']}")
    print(f"📁 文件：{filename}")
    print(f"📊 分类：{topic.get('category', '科普')}")

if __name__ == "__main__":
    main()
