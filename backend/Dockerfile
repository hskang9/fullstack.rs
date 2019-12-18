FROM rustlang/rust:nightly
RUN sudo apt-get install postgresql postgresql-contrib
RUN cargo install diesel_cli --no-default-features --features postgres

RUN cargo install cargo-watch

WORKDIR /usr/src/app

EXPOSE 8080
EXPOSE 5432

VOLUME ["/usr/local/cargo"]
