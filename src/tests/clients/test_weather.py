"""
Тестирование функций клиента для получения информации о погоде.
"""
import pytest

from clients.weather import WeatherClient


@pytest.mark.asyncio
class TestWeatherClient:
    """
    Тестирование клиента для получения информации о погоде.
    """

    base_url = "https://api.openweathermap.org/data/2.5/weather"

    @pytest.fixture
    def client(self):
        return WeatherClient()

    async def test_get_base_url(self, client):
        assert await client.get_base_url() == self.base_url

    async def test_get_weather(self, mocker, client):
        mocker.patch("clients.weather.WeatherClient._request")
        await client.get_weather()
        client._request.assert_called_once_with(f"{self.base_url}?units=metric&q=London&appid=4f06fab6de87a8137087084b564530c6")

        await client.get_weather("test")
        client._request.assert_called_with(f"{self.base_url}?units=metric&q=test&appid=4f06fab6de87a8137087084b564530c6")
