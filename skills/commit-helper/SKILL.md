---
name: commit-helper
description: 智能生成Git commit message。根据代码变更自动生成符合规范的commit message，支持Conventional Commits规范。触发条件：(1) 用户要求生成commit message (2) 准备提交代码 (3) 查看git status/diff后需要提交 (4) 批量提交多个文件
---

# Commit Helper - 智能Commit Message生成

根据代码变更自动生成清晰、规范的commit message。

## Commit Message规范

采用 **Conventional Commits** 规范：

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type（必填）

| Type | 说明 | 示例 |
|------|------|------|
| `feat` | 新功能 | feat: 添加用户登录功能 |
| `fix` | 修复bug | fix: 修复登录验证逻辑错误 |
| `docs` | 文档变更 | docs: 更新README安装说明 |
| `style` | 代码格式（不影响逻辑） | style: 统一缩进为2空格 |
| `refactor` | 重构（不增加功能也不修复bug） | refactor: 提取登录逻辑到独立模块 |
| `perf` | 性能优化 | perf: 优化数据库查询性能 |
| `test` | 添加测试 | test: 添加登录单元测试 |
| `chore` | 构建/工具链变动 | chore: 更新webpack配置 |
| `ci` | CI配置变动 | ci: 添加GitHub Actions配置 |
| `revert` | 回滚commit | revert: 撤销用户登录功能 |

### Scope（可选）

影响范围，例如：
- `api` - API相关
- `ui` - UI界面
- `db` - 数据库
- `auth` - 认证授权
- `config` - 配置文件

### Subject（必填）

- 简短描述（50字符以内）
- 使用祈使句（add、fix、update，而非added、fixed）
- 首字母小写
- 结尾不加句号

### Body（可选）

- 详细说明"做了什么"和"为什么"
- 可以分多行
- 与subject空一行

### Footer（可选）

- Breaking Changes：`BREAKING CHANGE: <描述>`
- 关闭Issue：`Closes #123`

## 生成流程

### 1. 分析代码变更

```bash
# 查看变更统计
git diff --stat

# 查看详细变更
git diff

# 查看已暂存的变更
git diff --cached
```

### 2. 识别变更类型

**判断规则**：

| 变更特征 | Type |
|---------|------|
| 新增文件/函数/类 | `feat` |
| 修改bug修复相关代码 | `fix` |
| 修改文档/注释 | `docs` |
| 只改格式/缩进/空行 | `style` |
| 代码移动/重命名/提取 | `refactor` |
| 性能相关改动 | `perf` |
| 测试文件变更 | `test` |
| 配置文件/构建脚本 | `chore` |

### 3. 生成Message

**单文件变更**：
```
feat(auth): 添加JWT token验证
```

**多文件相关变更**：
```
feat(user-profile): 实现用户资料编辑功能

- 添加头像上传接口
- 实现昵称修改逻辑
- 添加个人简介编辑UI
```

**Breaking Change**：
```
refactor(api): 重构用户认证接口

BREAKING CHANGE: 登录接口从 /login 改为 /auth/login
```

### 4. 确认并提交

**预览message**：
```bash
git commit --dry-run
```

**执行提交**：
```bash
git commit -m "type(scope): subject"
```

## 常见场景模板

### 新功能
```
feat(module): 简短描述

- 详细说明1
- 详细说明2
```

### Bug修复
```
fix(module): 修复问题描述

根因：错误原因
修复：解决方案
影响：受影响的功能
```

### 重构
```
refactor(module): 重构描述

Before: 重构前的问题
After: 重构后的改进
Reason: 重构原因
```

### 文档更新
```
docs: 更新描述

添加/修改了哪些文档
```

### 配置变更
```
chore(config): 配置描述

- 配置项1
- 配置项2
```

## 最佳实践

1. **原子性**：一个commit只做一件事
2. **频率**：小步快跑，频繁提交
3. **清晰**：让其他人看message就知道做了什么
4. **关联**：关联Issue/PR（如有）
5. **避免**：
   - 模糊的message（"update code"、"fix bug"）
   - 过于详细的技术细节
   - 多个不相关的变更混在一起

## 示例

**好的commit message**：
```
feat(dashboard): 添加实时数据刷新功能

- 使用WebSocket接收服务器推送
- 每5秒自动更新图表数据
- 添加手动刷新按钮

Closes #234
```

**不好的commit message**：
```
update code
```

```
修改了很多东西，包括前端和后端，还修了一些bug
```

## 快速命令

**生成长message**：
```bash
git commit
# 在编辑器中输入完整message
```

**生成短message**：
```bash
git commit -m "type: subject"
```

**修改上次commit message**：
```bash
git commit --amend
```
