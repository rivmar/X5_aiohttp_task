import aiohttp_jinja2
import jinja2
from aiohttp import web
from views import start_page, ws

app = web.Application()

aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('./templates/'))

app.add_routes([
    web.get('/', start_page),
    web.get('/ws/', ws),
])
app.router.add_static('/static/', './static')

if __name__ == '__main__':
    web.run_app(app, port=8000)
