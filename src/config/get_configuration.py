import yaml

configuration = dict()
# Load the YAML file
with open("src/config/config.yaml", "r") as file:
    configuration = yaml.safe_load(file)