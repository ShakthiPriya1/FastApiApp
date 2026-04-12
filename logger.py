import logging
import os

logger = logging.getLogger("fastapi-app")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)

# Always log to console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Only enable Loki if not testing
if os.getenv("ENV") != "test":
    from logging_loki import LokiHandler

    loki_handler = LokiHandler(
        url="http://loki-gateway.loki.svc.cluster.local/loki/api/v1/push",
        tags={
            "service": "fast-api-services",
            "env": "development"
        },
        headers={
            "X-Scope-OrgID": "tenant1"
        },
        version="1",
    )

    loki_handler.setFormatter(formatter)
    logger.addHandler(loki_handler)