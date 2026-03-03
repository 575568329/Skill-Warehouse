#!/usr/bin/env python3
"""
智谱 AI 视频生成脚本
使用 CogVideoX 模型生成视频

Usage:
    python zhipu_video.py "一只猫在草地上奔跑" --output video.mp4
    python zhipu_video.py "让图片动起来" --image input.png --output video.mp4
"""

import argparse
import base64
import json
import os
import sys
import time
import urllib.request
import urllib.error

API_URL = "https://open.bigmodel.cn/api/paas/v4/videos/generations"
ASYNC_RESULT_URL = "https://open.bigmodel.cn/api/paas/v4/async-result"


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


def create_video_task(prompt: str, model: str = "cogvideox", image_path: str = None) -> dict:
    """
    创建视频生成任务

    Args:
        prompt: 视频描述
        model: 模型名称
        image_path: 参考图片路径（可选）

    Returns:
        任务信息字典
    """
    api_key = get_api_key()

    payload = {
        "model": model,
        "prompt": prompt,
    }

    if image_path:
        payload["image"] = image_to_base64(image_path)

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

        return result

    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"HTTP 错误 {e.code}: {error_body}")
        sys.exit(1)
    except Exception as e:
        print(f"请求失败: {e}")
        sys.exit(1)


def get_video_result(task_id: str) -> dict:
    """查询视频生成结果"""
    api_key = get_api_key()

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    url = f"{ASYNC_RESULT_URL}/{task_id}"

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"查询失败: {e}")
        return None


def download_video(url: str, output_path: str):
    """下载视频到本地"""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=300) as response:
            with open(output_path, "wb") as f:
                f.write(response.read())
        print(f"视频已保存到: {output_path}")
    except Exception as e:
        print(f"下载视频失败: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="智谱 AI 视频生成")
    parser.add_argument("prompt", help="视频描述")
    parser.add_argument("--model", default="cogvideox", help="模型名称 (默认: cogvideox)")
    parser.add_argument("--image", help="参考图片路径（用于图生视频）")
    parser.add_argument("--output", default="generated_video.mp4", help="输出文件路径")

    args = parser.parse_args()

    print(f"正在生成视频: {args.prompt}")
    if args.image:
        print(f"参考图片: {args.image}")
    print(f"模型: {args.model}")

    result = create_video_task(args.prompt, args.model, args.image)

    # 检查任务状态
    task_id = result.get("id")
    if not task_id:
        print(f"API 返回格式错误: {result}")
        sys.exit(1)

    print(f"任务 ID: {task_id}")
    print("等待视频生成（约需 2-5 分钟）...")

    max_attempts = 60
    for i in range(max_attempts):
        time.sleep(10)
        status = get_video_result(task_id)
        if status:
            task_status = status.get("task_status", "PROCESSING")
            print(f"进度: {i+1}/{max_attempts} - {task_status}")

            if task_status == "SUCCESS":
                video_result = status.get("video_result", [])
                if video_result and len(video_result) > 0:
                    video_url = video_result[0].get("url")
                    cover_url = video_result[0].get("cover_image_url")
                    if video_url:
                        print(f"视频 URL: {video_url}")
                        if cover_url:
                            print(f"封面 URL: {cover_url}")
                        download_video(video_url, args.output)
                        return
                print(f"未找到视频 URL: {status}")
                sys.exit(1)

            elif task_status == "FAILED":
                print(f"视频生成失败: {status}")
                sys.exit(1)

    print("超时：视频生成时间过长")
    sys.exit(1)


if __name__ == "__main__":
    main()
