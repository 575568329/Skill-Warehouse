---
name: zhipu-ai
description: 智谱AI图像生成、视频生成和视觉理解。触发词：生成图片、生成图像、画图、GLM-Image、生成视频、CogVideoX、看图、分析图片、理解图片、GLM-4V。Use when user asks to: (1) generate images with text prompts, (2) generate videos from text or images, (3) analyze/understand/describe images.
---

# 智谱 AI 多模态技能

支持智谱 AI 的图像生成、视频生成和视觉理解功能。

## 前置要求

需要设置智谱 API Key：
```bash
# 环境变量方式
export ZHIPU_API_KEY="your-api-key"

# 或在 OpenClaw 配置中
# ~/.openclaw/openclaw.json:
# { "env": { "ZHIPU_API_KEY": "your-api-key" } }
```

获取 API Key: https://open.bigmodel.cn/

## 功能

### 1. 图像生成 (GLM-4A / CogView)

使用文本描述生成图像。

```bash
python scripts/zhipu_image.py "一只可爱的猫咪在阳光下打盹"
```

参数：
- `prompt`: 图像描述（必需）
- `--model`: 模型选择，默认 `cogview-3-plus`
- `--size`: 图像尺寸，默认 `1024x1024`
- `--output`: 输出文件路径，默认 `generated_image.png`

示例：
```bash
# 基础生成
python scripts/zhipu_image.py "赛博朋克风格的城市夜景"

# 指定尺寸
python scripts/zhipu_image.py "山水画" --size 768x1024 --output landscape.png
```

### 2. 视频生成 (CogVideoX)

从文本或图像生成视频。

```bash
# 文本生成视频
python scripts/zhipu_video.py "一只猫在草地上奔跑"

# 图像生成视频
python scripts/zhipu_video.py "让这张图片动起来" --image input.png
```

参数：
- `prompt`: 视频描述（必需）
- `--image`: 参考图片路径（可选，用于图生视频）
- `--model`: 模型选择，默认 `cogvideox`
- `--output`: 输出文件路径，默认 `generated_video.mp4`

### 3. 视觉理解 (GLM-4V)

分析图片内容，回答关于图片的问题。

```bash
python scripts/zhipu_vision.py image.png "描述这张图片的内容"
```

参数：
- `image`: 图片路径或 URL（必需）
- `prompt`: 问题或指令（必需）
- `--model`: 模型选择，默认 `glm-4v`

示例：
```bash
# 描述图片
python scripts/zhipu_vision.py photo.jpg "这张图片里有什么？"

# 识别物体
python scripts/zhipu_vision.py screenshot.png "找出图片中的所有文字"

# 分析图表
python scripts/zhipu_vision.py chart.png "分析这个图表的趋势"
```

## 支持的模型

| 功能 | 模型 | 说明 |
|------|------|------|
| 图像生成 | cogview-3-plus | 高质量图像生成 |
| 视频生成 | cogvideox | 文本/图像生成视频 |
| 视觉理解 | glm-4v-flash | 免费/低价多模态模型 |
| 视觉理解 | glm-4v / glm-4v-plus | 高级多模态模型（需单独开通） |

## API 参考

详细 API 文档见 [references/api.md](references/api.md)
