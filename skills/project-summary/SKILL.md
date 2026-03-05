---
name: project-summary
description: 快速生成项目结构总结。分析项目目录、技术栈、关键文件和架构，生成项目概览文档。触发条件：(1) 用户要求总结项目 (2) 快速了解新项目 (3) 生成项目文档 (4) 项目交接 (5) onboarding新成员
---

# Project Summary - 项目结构总结

快速分析并总结项目结构、技术栈和关键信息。

## 总结流程

### 1. 扫描项目根目录

**识别关键文件**：
```bash
# 列出根目录文件
ls -la

# 查找特定类型文件
find . -maxdepth 1 -type f
```

**关键文件识别**：

| 文件 | 信息 |
|------|------|
| `package.json` | Node.js项目，依赖、脚本 |
| `pom.xml` | Maven项目（Java） |
| `build.gradle` | Gradle项目（Java/Kotlin） |
| `requirements.txt` | Python依赖 |
| `go.mod` | Go模块 |
| `Cargo.toml` | Rust项目 |
| `.gitignore` | 项目类型提示 |
| `README.md` | 项目说明 |
| `CLAUDE.md` / `AGENTS.md` | 项目规则 |
| `docker-compose.yml` | Docker配置 |

### 2. 分析技术栈

**前端项目**：
- 框架：React/Vue/Angular/Svelte
- 构建工具：Webpack/Vite/Rollup
- UI库：Element UI/Ant Design/Material-UI
- 状态管理：Redux/Vuex/MobX

**后端项目**：
- 语言：Java/Python/Go/Node.js
- 框架：Spring Boot/Django/Express/Gin
- 数据库：MySQL/PostgreSQL/MongoDB
- 缓存：Redis/Memcached

**基础设施**：
- 容器化：Docker/Kubernetes
- CI/CD：GitHub Actions/Jenkins/GitLab CI
- 云服务：AWS/GCP/Azure

### 3. 分析目录结构

**标准结构识别**：

```
project-root/
├── src/              # 源代码
│   ├── components/   # 组件（前端）
│   ├── pages/        # 页面（前端）
│   ├── services/     # 服务层
│   ├── controllers/  # 控制器（后端）
│   ├── models/       # 数据模型
│   └── utils/        # 工具函数
├── tests/            # 测试代码
├── docs/             # 文档
├── config/           # 配置文件
├── scripts/          # 脚本
└── assets/           # 静态资源
```

**统计信息**：
```bash
# 统计代码行数
find . -name "*.js" -o -name "*.ts" | xargs wc -l

# 统计文件数量
find . -type f | wc -l

# 按类型统计
find . -name "*.js" | wc -l
```

### 4. 生成总结报告

**报告模板**：

```markdown
# 项目总结：[项目名称]

## 项目概述
- **类型**：[Web应用/API服务/库/工具]
- **语言**：[主要编程语言]
- **框架**：[核心框架]

## 技术栈

### 前端（如适用）
- 框架：[React/Vue/etc]
- UI库：[Element UI/etc]
- 状态管理：[Redux/etc]
- 构建工具：[Webpack/Vite/etc]

### 后端（如适用）
- 框架：[Spring Boot/etc]
- 数据库：[MySQL/etc]
- 缓存：[Redis/etc]
- API风格：[REST/GraphQL/etc]

### 基础设施
- 容器化：[Docker/etc]
- CI/CD：[GitHub Actions/etc]
- 部署环境：[云平台/etc]

## 目录结构
```
[关键目录树]
```

**关键目录说明**：
- `src/` - 源代码
- `tests/` - 测试代码
- `docs/` - 文档

## 核心文件

### 配置文件
- `package.json` - Node.js依赖和脚本
- `tsconfig.json` - TypeScript配置
- `.env.example` - 环境变量示例

### 入口文件
- `src/index.ts` - 应用入口
- `src/app.ts` - Express应用配置

### 关键模块
- `src/controllers/` - API控制器
- `src/models/` - 数据模型
- `src/utils/` - 工具函数

## 构建和运行

### 安装依赖
```bash
[安装命令]
```

### 开发模式
```bash
[开发命令]
```

### 生产构建
```bash
[构建命令]
```

### 测试
```bash
[测试命令]
```

## 统计数据

- **总文件数**：XXX
- **代码行数**：XXX
- **主要语言占比**：
  - JavaScript: 60%
  - TypeScript: 30%
  - CSS: 10%

## 特殊说明

[项目特有的重要信息]

---
生成时间：YYYY-MM-DD
```

## 快速分析技巧

### 1. 一眼识别项目类型

**前端项目**：
- 有 `index.html`
- 有 `package.json` + `src/` + `public/`
- 常见框架特征文件

**后端项目**：
- 有 `pom.xml` / `build.gradle` / `go.mod`
- 有 `src/main/` 结构
- 有 `application.properties` / `config.py`

**全栈项目**：
- 同时有前端和后端特征
- 可能有 `client/` + `server/` 分离

**库/工具**：
- 有 `lib/` 或单一入口文件
- 有 `README.md` 详细说明

### 2. 提取关键信息

**package.json**：
```json
{
  "name": "项目名称",
  "version": "版本",
  "scripts": {
    "dev": "开发命令",
    "build": "构建命令",
    "test": "测试命令"
  },
  "dependencies": {
    "关键依赖": "版本"
  }
}
```

**README.md**：
- 项目描述
- 安装步骤
- 使用方法
- 特性列表

### 3. 识别架构模式

**MVC**：有 `models/` + `views/` + `controllers/`
**微服务**：多个独立服务目录
**Monorepo**：有 `packages/` 或 `apps/`
**Layered**：按层次分包（service/dao/entity）

## 输出选项

### 完整报告
生成上述完整模板，适合项目交接。

### 简要总结
只包含：
- 项目类型和技术栈
- 核心目录结构
- 构建命令

### 单页概览
一句话描述 + 技术栈列表 + 关键命令

## 注意事项

1. **避免敏感信息**：不输出 `.env`、密钥、密码等
2. **保持更新**：项目变更后重新生成
3. **补充说明**：对于特殊架构或约定，添加注释
4. **保存位置**：建议保存到 `docs/project-summary.md`

## 示例输出

**简要总结**：

```
项目：Lobster Novel System
类型：西幻小说创作辅助系统
语言：Markdown + JavaScript
框架：无（纯文档 + 脚本）

技术栈：
- 地图：ECharts
- 版本控制：Git
- 编辑器：任意Markdown编辑器

目录结构：
├── docs/         # 设计文档
├── chapters/     # 正文章节
├── worldbuilding/ # 世界观设定
└── map/          # 交互式地图

核心命令：
- 地图预览：打开 map/index.html
- Git提交：git add . && git commit -m "message"
```
