#!/usr/bin/env python3
"""
智谱 AI 图像生成脚本
使用 GLM-4A / CogView 模型生成图像

Usage:
    python zhipu_image.py "一只可爱的猫咪" --size 1024x1024 --output cat.png
"""

import argparse
import base64
import json
import os
import sys
import urllib.request
import urllib.error

API_URL = "https://open.bigmodel.cn/api/paas/v4/images/generations"


def get_api_key():
    """获取 API Key"""
    api_key = os.environ.get("ZHIPU_API_KEY")
    if not api_key:
        print("错误: 未设置 ZHIPU_API_KEY 环境变量")
        print("请运行: export ZHIPU_API_KEY='your-api-key'")
        sys.exit(1)
    return api_key


def generate_image(prompt: str, model: str = "cogview-3-plus", size: str = "1024x1024") -> str:
    """
    生成图像

    Args:
        prompt: 图像描述
        model: 模型名称
        size: 图像尺寸

    Returns:
        生成的图像 URL 或 base64 数据
    """
    api_key = get_api_key()

    payload = {
        "model": model,
        "prompt": prompt,
        "size": size,
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

        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))

        if "data" in result and len(result["data"]) > 0:
            return result["data"][0].get("url") or result["data"][0].get("b64_json")
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


def download_image(url: str, output_path: str):
    """下载图片到本地"""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as response:
            with open(output_path, "wb") as f:
                f.write(response.read())
        print(f"图像已保存到: {output_path}")
    except Exception as e:
        print(f"下载图像失败: {e}")
        sys.exit(1)


def save_base64_image(b64_data: str, output_path: str):
    """保存 base64 图像"""
    try:
        image_data = base64.b64decode(b64_data)
        with open(output_path, "wb") as f:
            f.write(image_data)
        print(f"图像已保存到: {output_path}")
    except Exception as e:
        print(f"保存图像失败: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="智谱 AI 图像生成")
    parser.add_argument("prompt", help="图像描述")
    parser.add_argument("--model", default="cogview-3-plus", help="模型名称 (默认: cogview-3-plus)")
    parser.add_argument("--size", default="1024x1024", help="图像尺寸 (默认: 1024x1024)")
    parser.add_argument("--output", default="generated_image.png", help="输出文件路径")

    args = parser.parse_args()

    print(f"正在生成图像: {args.prompt}")
    print(f"模型: {args.model}, 尺寸: {args.size}")

    result = generate_image(args.prompt, args.model, args.size)

    if result.startswith("http"):
        download_image(result, args.output)
    else:
        save_base64_image(result, args.output)


if __name__ == "__main__":
    main()
