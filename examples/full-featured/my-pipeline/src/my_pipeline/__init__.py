from pathlib import Path


from dagstermill import local_output_notebook_io_manager
from dagster import (
    job,
    Definitions,
    reconstructable,
    execute_job,
    DagsterInstance,
    config_mapping,
    Config,
    RunConfig,
)
from dagstermill.manager import MANAGER_FOR_NOTEBOOK_INSTANCE


from dj.job_composition import NbsJobComposition
from dj.utils.cfg import read_piepline_yml
from my_op.cfg import Nb0Cfg, Nb1Cfg, Nb2Cfg


_pipeline_cfg = read_piepline_yml()


class SimplifiedConfig(Config):
    a: int
    b: int


@config_mapping
def simplified_config(val: SimplifiedConfig) -> RunConfig:
    return RunConfig(
        # ops={
        #     "nb_0": {"config": {"a": 1}},
        #     "nb_1": {"config": {"a": 1}},
        #     "nb_2": {"config": {"b": 2}},
        # }
        ops={
            "nb_0": Nb0Cfg(a=1),
            "nb_1": Nb1Cfg(a=1),
            "nb_2": Nb2Cfg(b=2),
        }
    )


nbs_job_composition = NbsJobComposition(
    root_path=Path(_pipeline_cfg["notebooks"]["path"]),
    nbs_sequence=_pipeline_cfg["notebooks"]["notebooks"],
)


@job(
    name="nb_pipeline",
    description="simple notebooks pipepline",
    resource_defs={
        "output_notebook_io_manager": local_output_notebook_io_manager,
    },
    config=simplified_config,
    metadata=nbs_job_composition.metadata,
)
def nb_pipeline():
    nbs_job_composition.do_compositioin()


defs = Definitions(
    jobs=[nb_pipeline],
    resources={
        "output_notebook_io_manager": local_output_notebook_io_manager,
    },
)
