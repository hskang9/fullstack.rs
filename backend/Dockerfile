# author
MAINTAINER "Hyungsuk Kang"

# extra metadata
LABEL version="1.0"
LABEL description="First image with Dockerfile."


FROM rustlang/rust:nightly

RUN cargo install diesel_cli --no-default-features --features postgres

RUN cargo install cargo-watch

WORKDIR /usr/src/app

EXPOSE 5001

VOLUME ["/usr/local/cargo"]
