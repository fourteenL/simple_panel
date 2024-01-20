from cache_manager import global_cache
import asyncio
from .network import get_network_info
from .network import get_network_speed
from .system import get_server_status
from .system import get_detailed_system_info


# 只执行一次
async def only_once():
    global_cache["server_info"] = await get_detailed_system_info()
    global_cache["network_info"] = await get_network_info()


# 更新全局缓存的异步任务
async def update_global_cache():
    await only_once()
    while True:
        server_status = await get_server_status()
        network_status = await get_network_speed()
        global_cache["server_status"] = server_status
        global_cache["network_status"] = network_status
        await asyncio.sleep(1)  # 每隔1秒更新一次
