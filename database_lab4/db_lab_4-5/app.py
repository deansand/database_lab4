import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from waitress import serve
import yaml

from my_project import create_app, db

DEVELOPMENT_PORT = 5000
PRODUCTION_PORT = 8080
HOST = "0.0.0.0"
DEVELOPMENT = "development"
PRODUCTION = "production"
FLASK_ENV = "FLASK_ENV"
ADDITIONAL_CONFIG = "ADDITIONAL_CONFIG"

# Define the path to the app.yml file
config_yaml_path = os.path.join(os.path.dirname(__file__), 'config', 'app.yml')

if __name__ == '__main__':
    flask_env = os.environ.get(FLASK_ENV, DEVELOPMENT).lower()

    with open(config_yaml_path, "r", encoding='utf-8') as yaml_file:
        config_data_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)
        additional_config = config_data_dict[ADDITIONAL_CONFIG]

        if flask_env == DEVELOPMENT:
            config_data = config_data_dict[DEVELOPMENT]
            create_app(config_data, additional_config).run(port=DEVELOPMENT_PORT, debug=True)

        elif flask_env == PRODUCTION:
            config_data = config_data_dict[PRODUCTION]
            serve(create_app(config_data, additional_config), host=HOST, port=PRODUCTION_PORT)