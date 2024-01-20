import sys
import tornado.gen
from .router import Router
from .router import BaseHandler

from api import ServerInfoWebSocket

# sys.path.append("..")
class IndexHandler(BaseHandler):
    @tornado.gen.coroutine
    def index(self):
        self.render('index.html')


# 路由注册
router = Router(BaseHandler)
router.route(method='get', url='/', auth=False)(IndexHandler.index)

router.ws_route('/ws/server_info', ServerInfoWebSocket)
