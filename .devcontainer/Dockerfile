FROM brendanburns/wasm-dev-base:0.0.4

RUN apt install unzip -y -qq && \
    curl https://github.com/tiran/cpython-wasm-test/releases/download/v3.11.0/Python-3.11.0-wasm32-wasi-16.zip -L --output Python-3.11.0-wasm32-wasi-16.zip && \
    unzip Python-3.11.0-wasm32-wasi-16.zip

COPY python3-wasm /usr/bin/python3-wasm
