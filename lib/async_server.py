import asyncio
import psutil
import platform
from cache_manager import global_cache


# 服务器获取状态的异步函数
async def get_server_status():
    await asyncio.sleep(1)
    server_info = {
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent
    }
    return server_info

# 服务器获取详细信息的异步函数
async def get_detailed_system_info():
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
    }
    return system_info

# 更新全局缓存的异步任务
async def update_global_cache():
    global_cache["server_info"] = await get_detailed_system_info()
    while True:
        server_status = await get_server_status()
        global_cache["server_status"] = server_status
        await asyncio.sleep(1)  # 每隔1秒更新一次
