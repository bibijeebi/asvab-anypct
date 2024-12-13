#!/usr/bin/env -S nix shell --override-input nixpkgs github:nixos/nixpkgs/nixos-unstable nixpkgs#gum github:tomberek/-#python3With.cyclopts.sh --command python3

from cyclopts import App
from sh import gum

app = App()

@app.default
def main():
    # choose a topic
    topic = gum.choose("Word Knowledge", "Arithmetic Reasoning", "Mathematics Knowledge", 
                      header="Choose a topic",
                      _err=True,  # Redirect stderr to avoid mixing with stdout
                      _out=True)  # Capture stdout
    print(f"Selected topic: {topic}")

if __name__ == "__main__":
    app()