import json
import os


class ScenarioConfiguration(object):
    """
    Class that will hold the test cessuib configuration regarding DSS and users that will be involded.
    It is a singleton, so it will read only once the configuration and each time it is requested, it will
    loaded directly from memory and not from the json file.
    """

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

        # Skip the init if we already have read the file.
        if self._initialized:
            return

        # Get the path to the configuration file, if it is empty raise an Error
        test_instance_config_path = os.getenv("PLUGIN_INTEGRATION_TEST_INSTANCE", None)
        if not test_instance_config_path:
            raise ValueError("'PLUGIN_INTEGRATION_TEST_INSTANCE' is not defined, please point it to an instance configuration file")

        # Open the json file and map it to a python dict
        with open(test_instance_config_path, "r") as fd:
            self._run_instance_config = json.load(fd)

        # Slightly change the format to put the key which is the target DSS
        # at the same level of the other walues.
        self._hosts = []
        for key, value in self._run_instance_config.items():
            self._hosts.append({"target": key, **value})

    @property
    def hosts(self):
        return self._hosts
