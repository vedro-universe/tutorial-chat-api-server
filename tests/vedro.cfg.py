import vedro
import vedro.plugins.director.rich as rich_reporter
import vedro_httpx
import vedro_valera_validator as valera_validator


class Config(vedro.Config):

    class Plugins(vedro.Config.Plugins):

        class ValeraValidator(valera_validator.ValeraValidator):
            enabled = True

        class RichReporter(rich_reporter.RichReporter):
            enabled = True
            show_timings = True
            v2_verbosity = True

        class VedroHTTPX(vedro_httpx.VedroHTTPX):
            enabled = True
