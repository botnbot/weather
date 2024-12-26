from importlib import reload

from requests import exceptions
from src.API import get_lat_lon_from_api, get_weather_from_api
from unittest.mock import patch
from main import main


def test_get_lat_lon_from_api_succes():
    mock_response = [{"lat": "55.7558", "lon": "37.6173"}]
    with patch("src.API.requests.get") as mocked_get:
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.json.return_value = mock_response

        lat, lon = get_lat_lon_from_api("москва")
        assert lat == "55.7558"
        assert lon == "37.6173"
        mocked_get.assert_called_once()


def test_get_lat_lon_from_api_empty():
    mock_response = []
    with patch("src.API.requests.get") as mocked_get:
        mocked_get.return_value.status_code = 400
        mocked_get.return_value.json.return_value = mock_response

        lat, lon = get_lat_lon_from_api("")
        assert lat is None
        assert lon is None
        mocked_get.assert_called_once()


def test_get_lat_lon_from_api_http_err():
    with patch("src.API.requests.get") as mocked_get:
        mocked_get.return_value.status_code = 404
        mocked_get.return_value.raise_for_status.side_effect = exceptions.HTTPError

        lat, lon = get_lat_lon_from_api("london")
        assert lat is None
        assert lon is None
        mocked_get.assert_called_once()


def test_get_lat_lon_from_api_connect_err():
    with patch("src.API.requests.get") as mocked_get:
        mocked_get.return_value.raise_for_status.side_effect = exceptions.ConnectionError

        lat, lon = get_lat_lon_from_api("london")
        assert lat is None
        assert lon is None
        mocked_get.assert_called_once()


def test_get_lat_lon_from_api_value_err():
    with patch("src.API.requests.get") as mocked_get:
        mocked_get.return_value.raise_for_status.side_effect = ValueError

        lat, lon = get_lat_lon_from_api("london")
        assert lat is None
        assert lon is None
        mocked_get.assert_called_once()


def test_get_lat_lon_from_api_request_exc():
    with patch("src.API.requests.get") as mocked_get:
        mocked_get.return_value.status_code = 404
        mocked_get.return_value.raise_for_status.side_effect = exceptions.RequestException

        lat, lon = get_lat_lon_from_api("london")
        assert lat is None
        assert lon is None
        mocked_get.assert_called_once()


def test_get_weather_from_api_succes():
    mock_response = {"weather": [{"description": "light snow", "icon": "13d", "id": 600, "main": "Snow"}]}
    with patch("src.API.requests.get") as mocked_get:
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.json.return_value = mock_response

        response = get_weather_from_api(55.7558, 37.6173)
        assert response == mock_response
        mocked_get.assert_called_once()


def test_get_weather_from_api_empty():
    mock_response = None
    with patch("src.API.requests.get") as mocked_get:
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.json.return_value = mock_response

        response = get_weather_from_api(55.7558, 37.6173)
        assert response == mock_response
        mocked_get.assert_called_once()


def test_get_weather_from_api_http_err():
    with patch("src.API.requests.get") as mocked_get:
        mocked_get.return_value.status_code = 404
        mocked_get.return_value.raise_for_status.side_effect = exceptions.HTTPError

        response = get_weather_from_api(55.7558, 37.6173)
        assert response is None
        mocked_get.assert_called_once()


def test_get_weather_from_api_connect_err():
    with patch("src.API.requests.get") as mocked_get:
        mocked_get.return_value.raise_for_status.side_effect = exceptions.ConnectionError

        response = get_weather_from_api(55.7558, 37.6173)
        assert response is None
        mocked_get.assert_called_once()


def test_get_weather_from_api_value_err():
    with patch("src.API.requests.get") as mocked_get:
        mocked_get.return_value.raise_for_status.side_effect = ValueError

        response = get_weather_from_api(55.7558, 37.6173)
        assert response is None
        mocked_get.assert_called_once()


def test_get_weather_from_api_request_exc():
    with patch("src.API.requests.get") as mocked_get:
        mocked_get.return_value.status_code = 404
        mocked_get.return_value.raise_for_status.side_effect = exceptions.RequestException

        response = get_weather_from_api(55.7558, 37.6173)
        assert response is None
        mocked_get.assert_called_once()
