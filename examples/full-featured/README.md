# Installation


Copy the pipeline config in DAGSTER_HOME


```bash
cp examples/full-featured/pipeline.yaml $DAGSTER_HOME
```


Install orchestration pkgs
```bash
cd examples/full-featured
pip install -e my-op
pip install -e my-pipeline
```


Run pipeline
```bash
cd examples/full-featured
dagster dev -h 0.0.0.0 -w workspace.yaml
```
