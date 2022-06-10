# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Workflow for developers/contributors

Before pushing to GitHub, run the following commands (preferably in an isolated conda environment):

1. Update conda environment: `make conda-env-update`
1. Install this package: `pip install -e .`
1. Sync with the latest [template](https://github.com/bopen/cookiecutter-conda-package) (optional): `make template-update`
1. Run quality assurance checks: `make qa`
1. Run tests: `make test`
1. Run the static type checker: `make type-check`

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
