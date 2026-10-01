# Python 3.14 (the version the Mawj course uses) with uv, installed the way uv's
# docs recommend for containers: its binaries copied from uv's own image, pinned.
FROM mcr.microsoft.com/devcontainers/python:3.14-trixie
COPY --from=ghcr.io/astral-sh/uv:0.12.21 /uv /uvx /bin/
