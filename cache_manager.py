# cache_manager.py
from cachetools import TTLCache

# 创建一个全局的缓存实例
global_cache = TTLCache(maxsize=10, ttl=300)  # 示例中只缓存10个状态，ttl为300秒
