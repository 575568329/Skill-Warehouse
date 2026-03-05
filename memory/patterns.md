# patterns.md - 代码模式

记录常用的代码模式和最佳实践，提高代码质量和一致性。

---

## PowerShell命令习惯

### 文件操作

```powershell
# 列出文件
ls
Get-ChildItem

# 读取文件
cat file.txt
Get-Content file.txt

# 写入文件
echo "content" > file.txt
Set-Content file.txt "content"

# 追加内容
echo "content" >> file.txt
Add-Content file.txt "content"

# 删除文件
rm file.txt
Remove-Item file.txt

# 创建目录
mkdir dirname
New-Item -ItemType Directory -Path dirname
```

### Git操作

```powershell
# 查看状态
git status

# 添加文件
git add .
git add filename

# 提交
git commit -m "message"

# 推送
git push origin main

# 拉取
git pull origin main

# 查看日志
git log --oneline -5

# 查看差异
git diff
git diff --cached
git diff master...HEAD
```

### 文件路径处理

```powershell
# 当前目录
pwd
Get-Location

# 切换目录
cd path
Set-Location path

# 路径中有空格时使用引号
cd "C:\Program Files"

# 查找文件
Get-ChildItem -Recurse -Filter "*.md"
```

---

## Markdown文档模式

### 标题层级

```markdown
# 一级标题（文档标题）

## 二级标题（主要章节）

### 三级标题（子章节）

#### 四级标题（细节）
```

### 列表

```markdown
- 无序列表项1
- 无序列表项2

1. 有序列表项1
2. 有序列表项2

- [ ] 待办事项
- [x] 已完成事项
```

### 代码块

````markdown
```language
代码内容
```
````

### 表格

```markdown
| 列1 | 列2 | 列3 |
|-----|-----|-----|
| 内容1 | 内容2 | 内容3 |
```

### 链接和图片

```markdown
[链接文本](URL)
![图片描述](图片URL)
```

---

## Git Commit Message模式

### Conventional Commits

```
<type>(<scope>): <subject>

<body>

<footer>
```

### 常用Type

- `feat` - 新功能
- `fix` - 修复bug
- `docs` - 文档变更
- `style` - 代码格式
- `refactor` - 重构
- `perf` - 性能优化
- `test` - 测试
- `chore` - 构建/工具

### 示例

```bash
feat(skills): 添加3个核心skills

- code-review: 代码审查模板
- commit-helper: 智能commit message生成
- project-summary: 项目结构快速总结
```

---

## OpenClaw配置模式

### Skill定义

```markdown
---
name: skill-name
description: 描述。触发条件：(1) 条件1 (2) 条件2
---

# Skill标题

使用说明...
```

### Agent定义

```markdown
---
name: agent-name
description: Agent描述
model: opus/sonnet/haiku
---

# Agent标题

角色定义...
```

---

## 错误处理模式

### Try-Catch（PowerShell）

```powershell
try {
    # 尝试执行的代码
    Get-Content "file.txt"
} catch {
    # 错误处理
    Write-Error "无法读取文件: $_"
}
```

### 条件检查

```powershell
# 检查文件是否存在
if (Test-Path "file.txt") {
    # 文件存在
} else {
    # 文件不存在
}

# 检查变量是否为空
if ($variable) {
    # 变量不为空
}
```

---

## 文档结构模式

### README.md标准结构

```markdown
# 项目名称

简短描述

## 功能特性

- 特性1
- 特性2

## 安装

安装步骤

## 使用

使用方法

## 配置

配置说明

## 开发

开发指南

## 许可证

许可证信息
```

### CHANGELOG.md标准结构

```markdown
# Changelog

## [版本号] - YYYY-MM-DD

### Added
- 新增功能

### Changed
- 变更内容

### Fixed
- 修复问题

### Removed
- 移除内容
```

---

## 安全模式

### 敏感信息处理

```markdown
# 不要在代码中硬编码
password = "123456"  # ❌ 错误

# 使用环境变量
password = os.getenv('PASSWORD')  # ✅ 正确

# 使用配置文件（.env，不提交到Git）
# .env文件
PASSWORD=123456
```

### .gitignore模式

```gitignore
# 敏感文件
.env
*.key
*.pem

# 依赖
node_modules/

# 构建产物
dist/
build/

# 系统文件
.DS_Store
Thumbs.db
```

---

## 最佳实践

### 代码注释

```markdown
# 好的注释
# 计算用户年龄（基于出生日期）
def calculate_age(birth_date):
    ...

# 不好的注释
# 计算年龄
def calculate_age(birth_date):
    ...
```

### 文件命名

```
# 使用连字符
my-file.md

# 使用下划线
my_file.md

# 避免空格
my file.md  # ❌ 避免
```

### 版本控制

```bash
# 小步提交
git commit -m "feat: 添加功能A"
git commit -m "fix: 修复bug B"

# 而不是大提交
git commit -m "添加功能A、B、C，修复bug D、E"  # ❌ 避免
```

---

_最后更新：2026-03-05_
