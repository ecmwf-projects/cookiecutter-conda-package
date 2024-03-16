# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Quick Start

```python
>>> import {{ cookiecutter.project_slug }}

```

## Workflow for developers/contributors

For best experience create a new conda environment (e.g. {{ cookiecutter.project_slug }}_env) with Python 3.11:

```
conda create -n {{ cookiecutter.project_slug }}_env -c conda-forge python=3.11
conda activate {{ cookiecutter.project_slug }}_env
```

Before pushing to GitHub, run the following commands:

1. Update conda environment: `make conda-env-update`
1. Install this package: `pip install -e .`
1. Sync with the latest [template](https://github.com/ecmwf-projects/cookiecutter-conda-package) (optional): `make template-update`
1. Run quality assurance checks: `make qa`
1. Run tests: `make unit-tests`
1. Run the static type checker: `make type-check`
1. Build the documentation (see [Sphinx tutorial](https://www.sphinx-doc.org/en/master/tutorial/)): `make docs-build`

## License

```
Copyright {{ cookiecutter.copyright_year }}, {{ cookiecutter.copyright_holder }}.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
