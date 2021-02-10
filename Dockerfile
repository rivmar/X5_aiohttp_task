FROM docker-registry.x5.ru/python:3.8.5-alpine

RUN echo http://mirror.yandex.ru/mirrors/alpine/v3.12/main > /etc/apk/repositories; \
    echo http://mirror.yandex.ru/mirrors/alpine/v3.12/community >> /etc/apk/repositories

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # paths
    CODE_PATH="/code" \
    VENV_PATH="/code/.venv" \
    PYTHONPATH="/code/.venv/lib/python3.8/site-packages" \
    # prepend poetry and venv to path
    PATH="/root/.local/bin:/code/.venv/bin:$PATH"


WORKDIR $CODE_PATH

COPY ./project $CODE_PATH
COPY ./requirements.txt $CODE_PATH

RUN apk update && apk add --no-cache musl-dev gcc && pip3 install -r requirements.txt

WORKDIR "$CODE_PATH/project"
