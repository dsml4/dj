# Installation

Copy the pipeline config in DAGSTER_HOME

```bash
cd examples/simple
cp pipeline.yaml $DAGSTER_HOME
```

Run dagster

```bash
cd examples/simple
dagster dev -h 0.0.0.0 -f pipeline/def.py
```