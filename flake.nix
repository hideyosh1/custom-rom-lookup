{
  description = "A Nix-flake-based Node.js development environment";

  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

  outputs =
    {
      self,
      nixpkgs,
    }:
    let
      supportedSystems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
      forEachSupportedSystem =
        f:
        nixpkgs.lib.genAttrs supportedSystems (
          system:
          f {
            pkgs = import nixpkgs {
              inherit system;
              overlays = [ self.overlays.default ];
            };
          }
        );
    in
    {
      overlays.default = final: prev: rec {
        nodejs = prev.nodejs;
        yarn = prev.yarn.override { inherit nodejs; };
      };

      devShells = forEachSupportedSystem (
        { pkgs }:
        {
          default = pkgs.mkShell {

            venvDir = ".venv";
            packages =
              with pkgs;
              [
                nodejs
                yarn-berry
                typescript
                typescript-language-server
                pyright
                black
                python3
              ]
              ++ (with pkgs.python3Packages; [
                pip
                venvShellHook
                requests
                beautifulsoup4
                jsonpickle

              ]);
            /*
              shellHook = ''
                npx update-browserslist-db@latest
              '';
            */
          };
        }
      );
    };
}
