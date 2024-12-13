#!/usr/bin/env -S nix shell --override-input nixpkgs github:nixos/nixpkgs/nixos-unstable nixpkgs#gum github:tomberek/-#python3With.cyclopts.sh --command python3

from cyclopts import App
from sh import gum

app = App()

@app.default
def main():
    # choose a topic
    topic = gum.choose("Choose a topic", options=["Word Knowledge", "Arithmetic Reasoning", "Mathematics Knowledge"])


if __name__ == "__main__":
    app()