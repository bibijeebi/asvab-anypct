#!/usr/bin/env -S nix shell github:tomberek/-#python3With.cyclopts.sh -c python3

from cyclopts import App

app = App()

@app.default
def main():
    pass

if __name__ == "__main__":
    app()