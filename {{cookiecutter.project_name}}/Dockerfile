FROM continuumio/miniconda3

COPY . /srv

WORKDIR /srv

RUN conda install -c conda-forge make gcc python=3.10 \
    && make conda-env-update CONDAFLAGS="-n base" \
    && pip install -e .
