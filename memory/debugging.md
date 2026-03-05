# debugging.md - 调试经验沉淀

记录调试过程中的问题和解决方案，避免重复踩坑。

---

## 🐛 问题模板

当遇到问题时，按以下格式记录：

```markdown
### [问题标题]

**症状**：
- 现象描述
- 错误信息（如有）

**根因**：
- 问题原因
- 为什么会发生

**解决方案**：
- 具体步骤
- 命令/代码

**预防措施**：
- 如何避免再次发生
- 需要注意什么

**相关文件**：
- 涉及的文件路径

**日期**：YYYY-MM-DD
```

---

## 飞书集成问题

### ngrok连接不稳定

**症状**：
- Webhook无法接收飞书事件
- ngrok连接频繁断开
- 国内访问ngrok很慢

**根因**：
- ngrok服务器在国外
- 国内网络访问不稳定
- 免费版有连接限制

**解决方案**：
1. 考虑使用国内内网穿透服务（如cpolar、frp）
2. 或使用云服务器部署OpenClaw
3. 或使用飞书官方云托管

**预防措施**：
- 不要依赖ngrok做长期方案
- 准备备用方案

**相关文件**：
- Webhook配置：见MEMORY.md

**日期**：2026-02-25

---

### Git历史中包含敏感文件

**症状**：
- MEMORY.md和memory/目录被提交到GitHub
- 包含个人信息和配置
- 公开仓库可见

**根因**：
- 初始提交时未配置.gitignore
- 敏感文件被包含在历史中

**解决方案**：
```bash
# 从Git历史中删除敏感文件
git filter-branch --force --index-filter \
  "git rm -r --cached --ignore-unmatch MEMORY.md memory/" \
  --prune-empty --tag-name-filter cat -- --all

# 清理本地仓库
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 强制推送
git push origin --force --all
```

**预防措施**：
- 创建项目时立即配置.gitignore
- 提交前检查敏感文件
- 使用pre-commit hook自动检查

**相关文件**：
- `.gitignore` - Git忽略配置
- `.claudeignore` - AI读取排除配置

**日期**：2026-03-05

---

## Git访问问题

### GitHub国内访问困难

**症状**：
- git push/pull超时
- 无法访问GitHub仓库

**根因**：
- 国内网络限制
- DNS污染

**解决方案**：
1. 使用代理（需配置）
2. 使用国内Git托管（Gitee等）
3. 使用镜像站

**预防措施**：
- 准备备用Git托管平台
- 重要代码多处备份

**相关文件**：
- GitHub仓库：575568329/XIAOSHUO
- GitHub仓库：575568329/Skill-Warehouse

**日期**：2026-03-03

---

## PowerShell问题

### 文件路径处理

**症状**：
- 路径包含空格时命令失败
- 中文路径乱码

**根因**：
- PowerShell对路径处理有特殊规则
- 编码问题

**解决方案**：
```powershell
# 使用引号包裹路径
cd "C:\Users\fjyu9\.openclaw\workspace"

# 或使用转义
cd C:\Users\fjyu9\`.openclaw\`workspace
```

**预防措施**：
- 路径中有空格时始终使用引号
- 注意文件编码（UTF-8）

**日期**：2026-03-05

---

## 待记录问题

- [ ] 飞书权限配置问题（如有）
- [ ] Node.js版本兼容问题（如有）
- [ ] 其他常见问题

---

_最后更新：2026-03-05_
