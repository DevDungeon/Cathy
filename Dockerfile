# Build with: `docker build . --tag cathy`
# Run with: `docker run cathy --help`
# Run with: `docker run --env-file .env cathy`
# Attach to a running container and get a shell
# `docker exec -it <container_id> /bin/sh`
FROM python:3.8.1-alpine

RUN apk add build-base

WORKDIR /cathy

# Copy only the necessary files
COPY ./cathy ./cathy
COPY ./README.rst .
COPY ./setup.py .

RUN python3 setup.py install

# Command to run when `docker run` invoked directly.
# Any args passed get passed to the entrypoint executable
ENTRYPOINT ["cathy"]

# Default args for entrypoint if none are provided to `docker run`.
# The CMD is executed directly if no ENTRYPOINT present.
CMD [""]
