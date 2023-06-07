import cabina
from cabina import env


class Config(cabina.Config):
    class Api(cabina.Section):
        URL: str = env.str("API_URL", default="https://chat-api-tutorial.vedro.io/tl3mzuetbb")
