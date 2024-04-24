import requests
import pytest

headers = {"Content-Type": "application/json"}


@pytest.fixture
def base_uri():
    return "http://localhost:5000"


def test_scan_file_clean(base_uri):
    file_data = {"fileId": "123", "status": "clean"}
    response = requests.post(f"{base_uri}/scans/scan", headers=headers, json=file_data)
    response_json = response.json()
    assert response.status_code == 200 and response_json['status'] == 'clean'


def test_scan_file_infected(base_uri):
    file_data = {"fileId": "456", "status": "infected"}
    response = requests.post(f"{base_uri}/scans/scan", headers=headers, json=file_data)
    response_json = response.json()
    assert response.status_code == 404 and response_json['status'] == 'infected'


def test_update_definitions(base_uri):
    response = requests.put(f"{base_uri}/scans/update", headers=headers)
    response_json = response.json()
    assert response.status_code == 200 and ["message"] == "Definitions updated successfully"


def test_get_scan_history(base_uri):
    response = requests.get(f"{base_uri}/scans/history", headers=headers)
    assert response.status_code == 200


def test_get_scan_history_exist(base_uri):
    response = requests.get(f"{base_uri}/scans/history", headers=headers)
    response_json = response.json()
    assert isinstance(response_json, list)


def test_get_quarantine(base_uri):
    response = requests.get(f"{base_uri}/quarantine/quarantine", headers=headers)
    assert response.status_code == 200


def test_get_quarantine_fileid(base_uri):
    response = requests.get(f"{base_uri}/quarantine/quarantine", headers=headers)
    response_json = response.json()
    assert isinstance(response_json, list)


def test_delete_from_quarantine_file_deleted(base_uri):
    response = requests.delete(f"{base_uri}/quarantine/delete", headers=headers)
    assert response.status_code == 200 and "message" in response.json()


def test_delete_from_quarantine_file_not_found(base_uri):
    response = requests.delete(f"{base_uri}/quarantine/delete", headers=headers)
    response_json = response.json()

    assert response.status_code == 404 and "error" in response_json
