import logging
from logging_loki import LokiHandler

# Loki handler config (similar to pino-loki)
handler = LokiHandler(
    url="http://loki-gateway.loki.svc.cluster.local/",
    tags={
        "service": "fast-api-services",
        "env": "development"
    },
    auth=None,  # add if needed
    version="1",
)

# Add multi-tenancy header
handler.session.headers.update({
    "X-Scope-OrgID": "tenant1"
})

# Formatter (structured logs)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)

# Create logger
logger = logging.getLogger("fastapi-app")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# Also log to console (VERY useful)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)