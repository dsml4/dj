from pathlib import Path


from dagstermill import local_output_notebook_io_manager
from dagster import (
    job,
    Definitions,
    reconstructable,
    execute_job,
    DagsterInstance,
)
from dagstermill.manager import MANAGER_FOR_NOTEBOOK_INSTANCE


from dj.job_composition import NbsJobComposition
from dj.utils.cfg import read_piepline_yml


_pipeline_cfg = read_piepline_yml()

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


if __name__ == "__main__":
    context = MANAGER_FOR_NOTEBOOK_INSTANCE.context
    j = reconstructable(nb_pipeline)
    res = execute_job(job=j, instance=DagsterInstance.get())
    print(res.run_id)
