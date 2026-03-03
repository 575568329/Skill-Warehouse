# 智谱 AI API 参考

## 认证

所有 API 请求需要在 Header 中携带 API Key：

```
Authorization: Bearer YOUR_API_KEY
```

获取 API Key: https://open.bigmodel.cn/

## 基础 URL

```
https://open.bigmodel.cn/api/paas/v4
```

---

## 图像生成 API

### 端点
```
POST /images/generations
```

### 请求参数

| 参数 | 类型 | 必需 | 说明 |
|------|------|------|------|
| model | string | 是 | 模型名称，如 `cogview-3-plus` |
| prompt | string | 是 | 图像描述，支持中英文 |
| size | string | 否 | 图像尺寸，默认 `1024x1024` |
| n | int | 否 | 生成数量，默认 1 |

### 支持的尺寸
- `1024x1024` - 正方形
- `768x1024` - 竖版
- `1024x768` - 横版

### 请求示例

```json
{
  "model": "cogview-3-plus",
  "prompt": "一只可爱的猫咪在阳光下打盹",
  "size": "1024x1024"
}
```

### 响应示例

```json
{
  "created": 1709123456,
  "data": [
    {
      "url": "https://..."
    }
  ]
}
```

---

## 视频生成 API

### 端点
```
POST /videos/generations
```

### 请求参数

| 参数 | 类型 | 必需 | 说明 |
|------|------|------|------|
| model | string | 是 | 模型名称，如 `cogvideox` |
| prompt | string | 是 | 视频描述 |
| image | string | 否 | 参考图片的 base64（图生视频） |

### 请求示例

```json
{
  "model": "cogvideox",
  "prompt": "一只猫在草地上奔跑"
}
```

### 响应示例

```json
{
  "id": "task_123456",
  "status": "processing"
}
```

### 查询任务状态

```
GET /videos/generations/{task_id}
```

响应：
```json
{
  "id": "task_123456",
  "status": "succeeded",
  "data": [
    {
      "url": "https://..."
    }
  ]
}
```

---

## 视觉理解 API (GLM-4V)

### 端点
```
POST /chat/completions
```

### 请求参数

| 参数 | 类型 | 必需 | 说明 |
|------|------|------|------|
| model | string | 是 | 模型名称，使用 `glm-4v` |
| messages | array | 是 | 对话消息列表 |
| max_tokens | int | 否 | 最大输出 token 数 |

### 消息格式

```json
{
  "model": "glm-4v",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": "https://example.com/image.jpg"
          }
        },
        {
          "type": "text",
          "text": "描述这张图片"
        }
      ]
    }
  ]
}
```

### 支持的图片格式
- URL 形式: `{"url": "https://..."}`
- Base64 形式: `{"url": "data:image/jpeg;base64,..."}`

### 响应示例

```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "这是一张..."
      }
    }
  ]
}
```

---

## 模型列表

| 模型 | 功能 | 说明 |
|------|------|------|
| glm-4v | 视觉理解 | 支持图片分析、OCR、图表理解 |
| cogview-3-plus | 图像生成 | 高质量文生图 |
| cogvideox | 视频生成 | 文生视频、图生视频 |

---

## 错误码

| 错误码 | 说明 |
|--------|------|
| 401 | API Key 无效或过期 |
| 429 | 请求频率超限 |
| 500 | 服务器内部错误 |

---

## 官方文档

- 智谱 AI 开放平台: https://open.bigmodel.cn/
- API 文档: https://open.bigmodel.cn/dev/api
