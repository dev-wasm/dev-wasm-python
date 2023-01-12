FROM brendanburns/wasm-dev-base:0.0.6

RUN apt install unzip -y -qq && \
    curl https://github.com/tiran/cpython-wasm-test/releases/download/v3.11.0/Python-3.11.0-wasm32-wasi-16.zip -L --output Python-3.11.0-wasm32-wasi-16.zip && \
    unzip Python-3.11.0-wasm32-wasi-16.zip

COPY python3-wasm /usr/bin/python3-wasm

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3-wasm 2
    
