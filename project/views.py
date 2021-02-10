import aiohttp_jinja2
from aiohttp import web
from search import SearchScrapper


@aiohttp_jinja2.template('start.html')
async def start_page(request):
    return {}


async def ws(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    while True:
        async for msg in ws:
            scrapper = SearchScrapper(msg[1])
            async for message in scrapper.get_messages():
                await ws.send_json(message)
