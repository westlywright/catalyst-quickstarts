import os
import yaml

config_file = os.getenv('CONFIG_FILE')

with open(config_file, 'r') as file:
    config_data = yaml.load(file, Loader=yaml.FullLoader)
    print(config_data)

for app in config_data['apps']:
    if app['appId'] == 'target':
        app['appPort'] = 5002
        app['workDir'] = './reply'
        app['env']['PORT'] = 5002
    elif app['appId'] == 'caller':
        app['appPort'] = 5001
        app['workDir'] = './request'
        app['env']['PORT'] = 5001

    app['command'] = ['npm', 'run', 'start']

updated_data = {
    'project': config_data['project'],
    'apps': config_data['apps'],
    'appLogDestination': config_data.get('appLogDestination', '')
}

with open(config_file, 'w') as file:
    yaml.safe_dump(updated_data, file, default_flow_style=False, sort_keys=False)

print("YAML file has been updated.")


