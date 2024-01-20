import tornado.gen
import tornado.websocket
import tornado.ioloop
import json
from cache_manager import global_cache


# 存储WebSocket连接对象的列表
websocket_connections = []


class ServerInfoWebSocket(tornado.websocket.WebSocketHandler):
    connections = {}

    def check_origin(self, origin):
        return True  # 允许 WebSocket 跨域请求

    def open(self):
        # 将新连接添加到列表
        if self not in websocket_connections:
            websocket_connections.append(self)
        cached_info = global_cache.get("server_info")
        self.write_message(json.dumps(cached_info))
        self.update_interval = tornado.ioloop.PeriodicCallback(
            self.send_cached_status, 1000
        )  # 每隔1秒触发一次 send_cached_status 方法
        self.update_interval.start()

    def on_close(self):
        # 关闭连接时移除
        if self in websocket_connections:
            websocket_connections.remove(self)

    def send_cached_status(self):
        cached_status = global_cache.get("server_status")
        if cached_status:
            self.write_message(json.dumps(cached_status))

    async def sleep(self):
        await tornado.gen.sleep(1)  # 更新频率：每秒一次
