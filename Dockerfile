FROM continuumio/miniconda3

WORKDIR /src/my-package

COPY environment.yml /src/my-package/

RUN conda install -c conda-forge gcc python=3.10 \
    && conda env update -n base -f environment.yml

COPY . /src/my-package

RUN pip install --no-deps -e .
