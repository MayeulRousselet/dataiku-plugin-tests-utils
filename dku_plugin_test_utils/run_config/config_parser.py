import json
import os


class ScenarioConfiguration(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Used here to define only one instance of the class
        """
        if not cls._instance:
            cls._instance = \
                super(ScenarioConfiguration, cls).__new__(cls)
            cls._instance._initialized = False

        return cls._instance

    def __init__(self):

        if self._initialized:
            return

        test_instance_config_path = os.getenv("PLUGIN_INTEGRATION_TEST_INSTANCE", None)
        if not test_instance_config_path:
            raise ValueError("'PLUGIN_INTEGRATION_TEST_INSTANCE' is not defined, please point it to an instance configuration file")
        
        with open(test_instance_config_path, "r") as fd:
            self._run_instance_config = json.load(fd)

    @property
    def host(self):
        return self._run_instance_config.get("host", None)

    @property
    def api_key(self):
        return self._run_instance_config.get("api_key", None)
