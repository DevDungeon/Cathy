# Run cathy in a docker container

FROM python:3.6-alpine

RUN apk add build-base

WORKDIR cathy

# Copy only the necessary files
COPY ./bin ./bin
COPY ./cathy ./cathy
COPY ./setup.py .

RUN python3 setup.py install

# Command to run when `docker run` invoked directly.
# Any args passed get passed to the entrypoint executable
ENTRYPOINT ["cathy"]

# Default args for entrypoint if none are provided to `docker run`.
# The CMD is executed directly if no ENTRYPOINT present.
CMD ["--help"]
