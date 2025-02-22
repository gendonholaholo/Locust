# WAHA (WhatsApp API)
API_BASE_URL_WAHA = "https://wa.agencerdas.id/"
HEADERS_WAHA = {
    "Authorization": "Bearer wc3/luDnToXP6a92mlKWA60rSFlipTeNe5TQ7nFv4FVq1ty7gKNFFCRu+uUvF9+ReWV924e1E6oTZQ2FZDRMWZMxlc0+3Gdotw6enrD9yQ2j10B4uFQo6gpwokqKKVIvU6G+4A==",
    "Content-Type": "application/json"
}
ENDPOINTS_WAHA = {
    "create_session": "/sessions"
}

# Staging
STAGING_URL = "https://staging.agencerdas.com"
HEADERS_STAGING = {
    "Content-Type": "application/json"
}
ENDPOINTS_STAGING = {
    "register": "/auth/register",
    "login": "/auth/login",
    "landing_page": "/"
}
