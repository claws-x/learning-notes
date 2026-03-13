#!/bin/bash
# daily_science_post.sh - 每日科普文章自动发布脚本
# 用途：每日 08:00 自动发布科普文章到博客

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLOG_DIR="$SCRIPT_DIR/../workspace-blog"
CONTENT_DIR="$SCRIPT_DIR/../workspace-content"
DATE=$(date +"%Y-%m-%d")
TIME=$(date +"%H:%M")

echo "📚 每日科普发布脚本"
echo "日期：$DATE"
echo "时间：$TIME"
echo ""

# 检查是否在 07:00-08:00 之间运行
HOUR=$(date +"%H")
if [ "$HOUR" -lt 7 ] || [ "$HOUR" -gt 8 ]; then
    echo "⚠️  当前不是发布时段 (07:00-08:00)"
    echo "提示：请设置 cron 在 07:30 运行"
    exit 0
fi

cd "$BLOG_DIR"

# 检查是否有当天的草稿
DRAFT_FILE="_posts/_drafts/daily-science-${DATE}.md"
if [ -f "$DRAFT_FILE" ]; then
    echo "✅ 找到当天草稿：$DRAFT_FILE"
    
    # 移动到发布目录
    mv "$DRAFT_FILE" "_posts/"
    echo "✅ 文章已移动到发布目录"
    
    # Git 提交
    git add "_posts/daily-science-${DATE}.md"
    git commit -m "📚 每日科普 | $DATE"
    git push origin master
    
    echo "✅ 文章已发布并推送"
    
    # 记录发布日志
    echo "$DATE $TIME: Published daily science post" >> "$CONTENT_DIR/publish/science_publish_log.txt"
    
else
    echo "❌ 未找到当天草稿：$DRAFT_FILE"
    echo ""
    echo "📝 建议:"
    echo "1. 检查草稿目录是否有文件"
    echo "2. 手动创建当天文章"
    echo "3. 提前准备至少 7 篇草稿"
    
    # 发送提醒（可以集成邮件/推送通知）
    echo ""
    echo "⚠️  发送提醒..."
    # 这里可以添加邮件或推送通知代码
fi

echo ""
echo "📊 发布检查完成"
echo "下次检查：明天 07:30"
