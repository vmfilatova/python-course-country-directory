"""
Тестирование функций клиента для получения информации о новостях.
"""
import pytest

from clients.news import NewsClient


@pytest.mark.asyncio
class TestNewsClient:
    """
    Тестирование клиента для получения информации о новостях.
    """

    base_url = "https://newsapi.org/v2"

    @pytest.fixture
    def client(self):
        return NewsClient()

    async def test_get_base_url(self, client):
        assert await client.get_base_url() == self.base_url

    async def test_get_news(self, mocker, client):
        mocker.patch("clients.news.NewsClient._request")
        await client.get_news()
        client._request.assert_called_once_with(f"{self.base_url}/top-headlines?country=Russia&apiKey=759238380e8c481cae9728cf3e559ed5")

        await client.get_news("test")
        client._request.assert_called_with(f"{self.base_url}/top-headlines?country=test&apiKey=759238380e8c481cae9728cf3e559ed5")
