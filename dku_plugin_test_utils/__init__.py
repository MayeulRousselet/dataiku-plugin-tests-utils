import json


def get_plugin_info():
    """
    Read the plugin information that can be found at the root level of each plugin

    Returns:
        dict: The python dict representing the plugin informations
    """
    with open('plugin.json') as json_file:
        data = json.load(json_file)
    return data


def scenario(client, project_key, scenario_id):
    """
    Remotly run a DSS scenario that correspond to one pytest test

    Args:
        client: DSS client instance from dataikuapi
        project_key (str): The project holding the scenarios to run
        scenario_id (str): The DSS scenario to run
    """
    client.get_project(project_key).get_scenario(scenario_id).run_and_wait()
