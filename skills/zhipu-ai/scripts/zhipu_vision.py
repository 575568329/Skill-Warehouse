#!/usr/bin/env python3
"""
智谱 AI 视觉理解脚本
使用 GLM-4V 模型分析图片

Usage:
    python zhipu_vision.py image.png "描述这张图片的内容"
    python zhipu_vision.py https://example.com/image.jpg "图片里有什么？"
"""

import argparse
import base64
import json
import os
import sys
import urllib.request
import urllib.error

API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"


def get_api_key():
    """获取 API Key"""
    api_key = os.environ.get("ZHIPU_API_KEY")
    if not api_key:
        print("错误: 未设置 ZHIPU_API_KEY 环境变量")
        print("请运行: export ZHIPU_API_KEY='your-api-key'")
        sys.exit(1)
    return api_key


def image_to_base64(image_path: str) -> str:
    """将图片转换为 base64"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def get_image_mime_type(path: str) -> str:
    """获取图片 MIME 类型"""
    ext = path.lower().split(".")[-1]
    mime_types = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "gif": "image/gif",
        "webp": "image/webp",
        "bmp": "image/bmp",
    }
    return mime_types.get(ext, "image/jpeg")


def is_url(path: str) -> bool:
    """判断是否为 URL"""
    return path.startswith("http://") or path.startswith("https://")


def analyze_image(image_source: str, prompt: str, model: str = "glm-4v") -> str:
    """
    分析图片

    Args:
        image_source: 图片路径或 URL
        prompt: 问题或指令
        model: 模型名称

    Returns:
        分析结果
    """
    api_key = get_api_key()

    # 构建消息内容
    content = []

    # 添加图片
    if is_url(image_source):
        content.append({
            "type": "image_url",
            "image_url": {"url": image_source}
        })
    else:
        # 本地图片转 base64
        b64_image = image_to_base64(image_source)
        mime_type = get_image_mime_type(image_source)
        content.append({
            "type": "image_url",
            "image_url": {"url": f"data:{mime_type};base64,{b64_image}"}
        })

    # 添加文本
    content.append({
        "type": "text",
        "text": prompt
    })

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
        "max_tokens": 1024,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        req = urllib.request.Request(
            API_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST"
        )

        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))

        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            print(f"API 返回错误: {result}")
            sys.exit(1)

    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"HTTP 错误 {e.code}: {error_body}")
        sys.exit(1)
    except Exception as e:
        print(f"请求失败: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="智谱 AI 视觉理解")
    parser.add_argument("image", help="图片路径或 URL")
    parser.add_argument("prompt", help="问题或指令")
    parser.add_argument("--model", default="glm-4v-flash", help="模型名称 (默认: glm-4v-flash)")

    args = parser.parse_args()

    print(f"正在分析图片: {args.image}")
    print(f"问题: {args.prompt}")
    print("-" * 50)

    result = analyze_image(args.image, args.prompt, args.model)
    print(result)


if __name__ == "__main__":
    main()
