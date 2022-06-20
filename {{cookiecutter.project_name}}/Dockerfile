# (C) Copyright {{ cookiecutter.copyright_year }} {{ cookiecutter.copyright_holder }}.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

FROM continuumio/miniconda3

COPY . /srv

WORKDIR /srv

RUN conda install -c conda-forge make gcc python=3.10 \
    && make conda-env-update CONDAFLAGS="-n base" \
    && pip install -e .
