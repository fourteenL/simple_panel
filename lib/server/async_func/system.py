import asyncio
import psutil
import platform


# 服务器状态的异步函数
async def get_server_status():
    await asyncio.sleep(1)
    server_info = {
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent
    }
    return server_info


# 服务器详细信息
async def get_detailed_system_info():
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
    }
    return system_info
