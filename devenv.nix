{ pkgs, ... }:

{
  languages.python = {
    enable = true;
    venv.enable = true;
    venv.requirements = builtins.readFile ./requirements.txt;
  };

  # https://devenv.sh/pre-commit-hooks/
  pre-commit.hooks.ruff.enable = true;

  # https://devenv.sh/processes/
  # processes.ping.exec = "ping example.com";

  # See full reference at https://devenv.sh/reference/options/
}
