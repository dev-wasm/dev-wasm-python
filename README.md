# Devcontainer WASM-Python
Simple devcontainer for Python development.

Note that Python + WASM is a little different for now, since the interperter (`python.wasm`) runs a standard `.py` python script.
There is no really great way to package up a script and `python.wasm` into a single bundle for now, so that is sadly an exercise
for the reader.

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

## Simple example
```sh
./python3-wasm main.py
```

## Web serving with WAGI

There is a simple example of web serving via WebAssembly + CGI (WAGI) in
the `webserver` directory. It uses the lighttpd web server and `mod_cgi`.
See the `webserver/lighttpd.conf` file for more details.

```sh
lighttpd -D -f webserver/lighttpd.conf
```

Once the server is running, VS Code or Codespaces should prompt you to connect to the open port.

It is important to note that the current configuration allows filesystem access to a variety of filepaths for both read and write.
This should be considered for test use only, we need to lock down to read-only access for production.

# TODO
* Figure out how to get PIP working
* Figure out how to package Python + script as a single .wasm file
