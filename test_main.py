from unittest.mock import patch

from requests import exceptions

from main import get_lat_lon_from_api


def test_get_lat_lon_from_api_succes():
    mock_response = [{"lat": "55.7558", "lon": "37.6173"}]
    with patch("main.requests.get") as mocked_get:
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.json.return_value = mock_response

        lat, lon = get_lat_lon_from_api("москва")
        assert lat == "55.7558"
        assert lon == "37.6173"
        mocked_get.assert_called_once()


def test_get_lat_lon_from_api_empty():
    mock_response = []
    with patch("main.requests.get") as mocked_get:
        mocked_get.return_value.status_code = 400
        mocked_get.return_value.json.return_value = mock_response

        lat, lon = get_lat_lon_from_api("")
        assert lat is None
        assert lon is None
        mocked_get.assert_called_once()


def test_get_lat_lon_from_api_http_err():
    with patch("main.requests.get") as mocked_get:
        mocked_get.return_value.status_code = 404
        mocked_get.return_value.raise_for_status.side_effect = exceptions.HTTPError

        lat, lon = get_lat_lon_from_api("london")
        assert lat is None
        assert lon is None
        mocked_get.assert_called_once()


def test_get_lat_lon_from_api_http_err():
    with patch("main.requests.get") as mocked_get:
        mocked_get.return_value.raise_for_status.side_effect = exceptions.ConnectionError

        lat, lon = get_lat_lon_from_api("london")
        assert lat is None
        assert lon is None
        mocked_get.assert_called_once()



def test_get_lat_lon_from_api_value_err():
    with patch("main.requests.get") as mocked_get:
        mocked_get.return_value.raise_for_status.side_effect = ValueError

        lat, lon = get_lat_lon_from_api("london")
        assert lat is None
        assert lon is None
        mocked_get.assert_called_once()


def test_get_lat_lon_from_api_request_exc():
    with patch("main.requests.get") as mocked_get:
        mocked_get.return_value.status_code = 404
        mocked_get.return_value.raise_for_status.side_effect = exceptions.RequestException

        lat, lon = get_lat_lon_from_api("london")
        assert lat is None
        assert lon is None
        mocked_get.assert_called_once()


