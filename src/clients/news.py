"""
Функции для взаимодействия с внешним сервисом-провайдером данных о новостях.
"""
from http import HTTPStatus
from typing import Optional

import aiohttp

from clients.base import BaseClient
from logger import trace_config
from settings import API_KEY_NEWSAPI


class NewsClient(BaseClient):
    """
    Реализация функций для взаимодействия с внешним сервисом-провайдером данных о новостях.
    """

    async def get_base_url(self) -> str:
        return "https://newsapi.org/v2"

    async def _request(self, endpoint: str) -> Optional[dict]:

        async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
            async with session.get(endpoint) as response:
                if response.status == HTTPStatus.OK:
                    return await response.json()

                return None

    async def get_news(self, country: str= "Russia") -> Optional[dict]:
        """
        Получение данных о новостях.
        :param country: Страна
        :param category: Категория новостей
        :return:
        """

        return await self._request(
            f"{await self.get_base_url()}/top-headlines?country={country}&apiKey={API_KEY_NEWSAPI}"
        )
