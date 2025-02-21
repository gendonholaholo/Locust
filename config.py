# WAHA (WhatsApp API)
API_BASE_URL_WAHA = "https://waha.devlike.pro/api/v1"
HEADERS_WAHA = {
    "Authorization": "Bearer YOUR_WAHA_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
ENDPOINTS_WAHA = {
    "create_session": "/sessions/create"
}

# Staging
STAGING_URL = "https://staging.agencerdas.com"
HEADERS_STAGING = {
    "Content-Type": "application/json"
}
ENDPOINTS_STAGING = {
    "register": "/auth/register",  # Minta Fariz
    "login": "/auth/login",  # Minta Fariz
    "landing_page": "/"  # Minta Fariz
}
