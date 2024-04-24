# Antivirus api testing module

antivirus_api_test is a Python module for testing antivirus api.

## Prerequisites
Install used modules (pytest, requests) that are in requirements.txt file.


```bash
pip install -r requirements.txt
```

## Usage

```python
import pytest
import requests

headers = {"Content-Type": "application/json"}


@pytest.fixture
def base_uri():
    return "https://api.antivirusexample.com"


def test_get_quarantine(base_uri):
    response = requests.get(f"{base_uri}/quarantine/quarantine", headers=headers)
    assert response.status_code == 200
```
### How to run

To run all test and show both FAIL and PASS type in terminal:
```
pytest antivirus_api_test.py -v
```

To run specific test, type in terminal (just an example).
```
pytest -k test_get_quarantine
```
