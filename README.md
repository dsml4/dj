# Dagster+Jupyter (DJ)

The Python library enables execution of notebooks in two contexts:
1. Dagster(**D**) op in the pipeline
2. standalone notebook in Jupyter (**J**).

Execution in the J context is useful for notebook development in the interactive Jupyter environment by Data Scientists, and execution in the D context is needed to build an environment for running reproducible experiments.

In the Dagster context, notebooks' code is locked.

The **D** context:

<img width="1363" height="823" alt="DJ_D" src="https://github.com/user-attachments/assets/e44f49d7-74aa-4efe-8458-1ee937874a14" />

Notebook configurations are defined in the notebook, and DJ makes them available to set in the Dagster UI:

<table>
  <tr>
    <td>D<img width="686" height="582" alt="Screenshot from 2026-07-31 22-18-19" src="https://github.com/user-attachments/assets/6d6418e7-bccb-49e0-9504-bf851473b34d" />
</td>
    <td>J<img width="978" height="635" alt="Screenshot from 2026-07-31 22-41-11" src="https://github.com/user-attachments/assets/0727cc09-c714-4402-add2-63dc90bbe2b5" />
  </tr>

