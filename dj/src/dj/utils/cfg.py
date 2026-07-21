from pathlib import Path
import os
import yaml


def read_piepline_yml():
    dagster_home = os.getenv("DAGSTER_HOME")
    if dagster_home is None:
        raise ValueError("DAGSTER_HOME is not defined")
    pipeline_yaml_path = Path(dagster_home) / "pipeline.yaml"
    if not pipeline_yaml_path.exists():
        raise ValueError("pipeline.yaml doesn't exist")
    with open(pipeline_yaml_path, "r") as file:
        pipeline_cfg = yaml.safe_load(file)
    return pipeline_cfg
