# Devcontainer WASM-Python
Simple devcontainer for Python development

# Usage

## Github Codespaces
Just click the button:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=575700892)

## Visual Studio Code
Note this assumes that you have the VS code support for remote containers and `docker` installed 
on your machine.

```sh
git clone https://github.com/dev-wasm/dev-wasm-python
cd dev-wasm-python
code ./
```

Visual studio should prompt you to see if you want to relaunch the workspace in a container, you do.

# Running

```sh
# The workspace is mapped into the wasm environment in the
# /workspace directory
./python3-wasm /workspace/main.py
```

# TODO
* Figure out how to get PIP working
* Figure out how to package Python + script as a single .wasm file