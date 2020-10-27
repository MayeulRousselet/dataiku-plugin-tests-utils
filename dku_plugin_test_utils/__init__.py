import json


def get_plugin_info():
    with open('plugin.json') as json_file:
        data = json.load(json_file)
        return data


def scenario(client, project_key, scenario_id):
    client.get_project(project_key).get_scenario(scenario_id).run_and_wait()
