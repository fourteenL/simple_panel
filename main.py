import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.autoreload
import asyncio
from conf import TEMPLATE_PATH, STATIC_PATH
from router import router
from lib import update_global_cache


settings = dict(
    template_path=TEMPLATE_PATH,
    static_path=STATIC_PATH,
    default_content_type="application/json",
    debug=True
)

app = tornado.web.Application(router.handlers, **settings)

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)

    # 启动异步任务
    loop = tornado.ioloop.IOLoop.current().asyncio_loop
    asyncio.ensure_future(update_global_cache(), loop=loop)

    print('Development server is running at http://sg.170001.xyz:8888')
    print('Quit the server with Control-C')
    tornado.ioloop.IOLoop.current().start()
