# OpenClaw 安全与成本控制指南

> 创建时间：2026-03-05
> 更新时间：2026-03-05

## 🔒 安全最佳实践

### 1. 敏感文件保护
- ✅ 已创建`.claudeignore` - 防止AI读取敏感文件
- ✅ 已创建`.gitignore` - 防止敏感信息提交到Git
- ⚠️ 定期检查是否有新的敏感文件需要添加

### 2. 操作权限控制
**需要确认的操作**（遵循AGENTS.md规定）：
- 发送邮件、消息到外部
- 执行git push、git push --force
- 删除文件（使用trash代替rm）
- 修改系统配置

**可自由执行的操作**：
- 读取文件
- 搜索网页
- 组织workspace
- 提交本地git commit（不push）

### 3. 多通道安全
- **主会话**：可访问MEMORY.md和个人上下文
- **群聊**：保持沉默，不主动分享用户信息
- **飞书/Discord**：注意不要泄露workspace内容

### 4. Ngrok安全
当前公网地址：`https://griffin-subchorioidal-contritely.ngrok-free.dev`
- ⚠️ 注意监控访问日志
- ⚠️ 考虑使用认证token
- ⚠️ 定期更换ngrok地址

---

## 💰 成本控制策略

### 1. Token消耗监控
**高消耗场景**：
- 长对话（>100轮）：建议重置会话
- Agent Team：成本N倍放大，控制在2-3个
- 大文件读取：使用offset/limit分批读取

**低消耗优化**：
- ✅ 使用subagent处理独立任务
- ✅ MEMORY.md只在主会话加载
- ✅ 心跳批量检查（不频繁轮询）

### 2. 心跳优化
**当前配置**：AGENTS.md建议4-6小时检查一次

**检查内容轮换**：
```json
{
  "rotate": ["email", "calendar", "weather", "mentions"],
  "frequency": "4-6 hours",
  "quiet_hours": "23:00-08:00"
}
```

**避免**：
- ❌ 每30分钟检查一次（太频繁）
- ❌ 深夜主动发送消息
- ❌ 无事时频繁HEARTBEAT_OK

### 3. Memory管理
**定期维护**（每3-5天）：
1. 清理memory/目录中的旧日志
2. 更新MEMORY.md（保留重要信息）
3. 删除过时的临时文件

**建议保留**：
- 重要决策和项目状态
- 用户偏好和习惯
- 技术环境配置

**建议清理**：
- 日常闲聊记录
- 临时调试信息
- 已解决的问题

### 4. Subagent使用策略
**适合subagent的任务**：
- ✅ 独立的分析任务（如本次安全分析）
- ✅ 代码审查和重构
- ✅ 文档生成和整理
- ✅ 数据处理和转换

**不适合subagent的任务**：
- ❌ 需要频繁交互的对话
- ❌ 需要主会话上下文的任务
- ❌ 简单的一次性查询

---

## 📋 检查清单

### 每周检查：
- [ ] 检查.claudeignore是否需要更新
- [ ] 清理memory/目录旧文件
- [ ] 审查git提交历史（确保无敏感信息）
- [ ] 检查ngrok访问日志

### 每月检查：
- [ ] 审查AGENT.md和MEMORY.md
- [ ] 评估成本消耗情况
- [ ] 更新安全配置
- [ ] 检查Skill权限

---

## 🚨 应急响应

### 发现敏感信息泄露：
1. 立即更换相关密钥/令牌
2. 从Git历史中删除敏感信息（`git filter-branch`）
3. 更新.claudeignore和.gitignore
4. 通知相关服务提供商

### 成本异常：
1. 检查是否有失控的subagent
2. 审查心跳频率设置
3. 检查是否有长对话未重置
4. 考虑降低模型级别

---

## 📚 参考资料

- [Claude Code安全最佳实践](https://docs.anthropic.com/claude/docs/security)
- [OpenClaw文档](https://github.com/openclaw/openclaw)
- [Ngrok安全配置](https://ngrok.com/docs/security)

---

_本指南应根据实际情况定期更新_
