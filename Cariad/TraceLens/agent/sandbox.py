# -*- coding: utf-8 -*-
"""代码安全执行沙箱。

在子进程中执行 LLM 生成的 Python 代码，提供超时保护和输出捕获。
"""

import os
import sys
import subprocess
import tempfile
from typing import Dict


def execute_code(code: str, timeout: int = 30) -> Dict:
    """在子进程中安全执行 Python 代码，捕获输出和错误。

    Args:
        code: 待执行的 Python 代码字符串。
        timeout: 执行超时时间（秒），默认 30 秒。

    Returns:
        {
            "success": bool,     # 是否成功执行
            "output": str,       # stdout 输出
            "images": list[str], # 解析出的图片路径列表（从 SUCCESS: 标记提取）
            "error": str,        # stderr 输出或超时信息
        }
    """
    # 将代码写入临时文件
    tmp_fd, tmp_path = tempfile.mkstemp(suffix=".py", prefix="mf4_agent_")
    try:
        with os.fdopen(tmp_fd, "w", encoding="utf-8") as f:
            f.write(code)

        # 在子进程中执行
        result = subprocess.run(
            [sys.executable, tmp_path],
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
            errors="replace",
        )

        success = result.returncode == 0
        output = result.stdout or ""
        error = result.stderr or ""

        if not success and not error:
            error = f"进程退出码: {result.returncode}"

    except subprocess.TimeoutExpired:
        success = False
        output = ""
        error = f"代码执行超时（超过 {timeout} 秒）"
    except Exception as e:
        success = False
        output = ""
        error = f"沙箱执行异常: {e}"
    finally:
        # 清理临时文件
        try:
            os.unlink(tmp_path)
        except OSError:
            pass

    # 从输出中解析图片路径
    images = []
    for line in output.splitlines():
        line_stripped = line.strip()
        if line_stripped.startswith("SUCCESS:"):
            img_path = line_stripped[len("SUCCESS:"):].strip()
            if img_path:
                images.append(img_path)

    return {
        "success": success,
        "output": output,
        "images": images,
        "error": error,
    }
