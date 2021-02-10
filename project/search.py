import asyncio
import environ
from aiovk.sessions import TokenSession
from aiovk.api import API
from aiovk.exceptions import VkAPIError

env = environ.Env()


class SearchScrapper:
    def __init__(self, search_phrase):
        self.search_phrase = search_phrase
        self.session = TokenSession(access_token=env('VK_TOKEN'))
        self.api = API(self.session)
    
    async def get_messages(self):
        search_result = await self.api.newsfeed.search(q=self.search_phrase)
        await asyncio.sleep(1)
        for result in search_result['items']:
            try:
                owner_id = result['owner_id']
                if owner_id < 0:
                    user_data = await self.api.groups.getById(group_id=-owner_id)
                    user_name = user_data[0]['name']
                else:
                    user_data = await self.api.users.get(user_ids=owner_id)
                    user_name = f'{user_data[0]["first_name"]} {user_data[0]["last_name"]}'
                wall_posts = await self.api.wall.get(owner_id=owner_id, count=1)
                wall_post = wall_posts['items'][0]
                yield {'name': user_name, 'text': wall_post['text']}
                await asyncio.sleep(1)
            except VkAPIError:
                continue
