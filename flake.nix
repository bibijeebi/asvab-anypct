{
  description = "Hello world flake using uv2nix";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    pyproject-nix = {
      url = "github:pyproject-nix/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    uv2nix = {
      url = "github:pyproject-nix/uv2nix";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    pyproject-build-systems = {
      url = "github:pyproject-nix/build-system-pkgs";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.uv2nix.follows = "uv2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {
    nixpkgs,
    uv2nix,
    pyproject-nix,
    pyproject-build-systems,
    ...
  }: let
    inherit (nixpkgs) lib;

    workspace = uv2nix.lib.workspace.loadWorkspace {workspaceRoot = ./.;};

    overlay = workspace.mkPyprojectOverlay {
      sourcePreference = "wheel";
    };

    pyprojectOverrides = _final: _prev: {
    };

    pkgs = nixpkgs.legacyPackages.x86_64-linux;

    python = pkgs.python311;

    pythonSet =
      (pkgs.callPackage pyproject-nix.build.packages {
        inherit python;
      })
      .overrideScope
      (
        lib.composeManyExtensions [
          pyproject-build-systems.overlays.default
          overlay
          pyprojectOverrides
        ]
      );

    asvabEnv = pythonSet.mkVirtualEnv "asvab-anypct-env" workspace.deps.default;
  in {
    packages.x86_64-linux.default = pkgs.writeShellScriptBin "asvab-anypct" ''
      #!${asvabEnv}/bin/python
      import asvab_anypct.__main__
      if __name__ == "__main__":
        asvab_anypct.__main__.main()
    '';

    devShells.x86_64-linux = {
      impure = pkgs.mkShell {
        packages = [
          python
          pkgs.uv
          pkgs.gum
        ];
        shellHook = ''
          unset PYTHONPATH
          export UV_PYTHON_DOWNLOADS=never
        '';
      };

      uv2nix = let
        editableOverlay = workspace.mkEditablePyprojectOverlay {
          root = "$REPO_ROOT";
        };

        editablePythonSet = pythonSet.overrideScope editableOverlay;

        virtualenv = editablePythonSet.mkVirtualEnv "asvab-anypct-dev-env" workspace.deps.all;
      in
        pkgs.mkShell {
          packages = [
            virtualenv
            pkgs.uv
          ];
          shellHook = ''
            unset PYTHONPATH

            export UV_NO_SYNC=1

            export UV_PYTHON_DOWNLOADS=never

            export REPO_ROOT=$(git rev-parse --show-toplevel)
          '';
        };
    };
  };
}
