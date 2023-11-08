import requests

DATADOG_API_KEY = '****'
DATADOG_APP_KEY = '****'

DASHBOARD_NAME = 'web-01 Dashboard'

# DASHBOARDS_ENDPOINT = 'https://api.datadoghq.com/api/v1/dashboard/lists/manual'
DASHBOARDS_ENDPOINT = 'https://api.datadoghq.com/api/v1/dashboard'

headers = {
    'DD-API-KEY': DATADOG_API_KEY,
    'DD-APPLICATION-KEY': DATADOG_APP_KEY,
}

response = requests.get(DASHBOARDS_ENDPOINT, headers=headers)

if response.status_code == 200:
    dashboard_data = response.json()
    # print(dashboard_data.get('dashboards'))

    for dashboard in dashboard_data.get('dashboards'):
        print(dashboard.get('id'))

else:
    print(
        f"Failed to fetch dashboard list. Status code: {response.status_code}")
