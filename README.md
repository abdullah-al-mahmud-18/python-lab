# Python Lab

A repository to learn and experiment with Python code: standard-library modules, argument parsing, pandas, and PyTorch / scikit-learn.

## Requirements

- Python >= 3.14 (see `.python-version`)
- [uv](https://docs.astral.sh/uv/) for dependency management

Dependencies (see `pyproject.toml`): `pandas`, `scikit-learn`, `torch`, `torchvision`. PyTorch and torchvision are installed from the CUDA 13.2 index (`pytorch-cu132`); the scripts fall back to CPU when no GPU is available.

## Setup

```sh
uv sync
```

## Project structure

| Path | Description |
| --- | --- |
| `main.py` | Placeholder entry point. |
| `argument_parser/argument_parser.py` | `argparse` basics: positional choices, required and optional flags. |
| `argument_parser/subcmd_parse.py` | `argparse` subcommands (`run train -t half\|full`). |
| `modules/os_module.py` | `os` module: paths, env variables, listing directories. |
| `modules/glob_module.py` | `glob` module: matching files, including recursive patterns. |
| `pandas/chipotle.py` | Loads the Chipotle orders TSV with pandas. |
| `pytorch/tensors_intro.py` | Tensor basics and fitting a polynomial to `sin(x)`. |
| `pytorch/quick_start.py` | PyTorch quick start: FashionMNIST, train/test loops, save and load a model, then predict. |
| `pytorch/nlp_classifying_names.py` | Work in progress: character-level name classification (dataset preparation). |
| `neural_networks/mlp.py` | Small MLP binary classifier on a synthetic scikit-learn dataset. |

Downloaded datasets (`data/`) and saved models (`models/`) are git-ignored.

## Running scripts

Run a script directly with uv:

```sh
uv run neural_networks/mlp.py
```

Or use the helper scripts, which search for the file by name and run it with `uv run <path> test run`:

```sh
./run.sh mlp.py        # bash
./run.ps1 mlp.py       # PowerShell
```

Note that the helpers always append `test run` as arguments, which suits `argument_parser/subcmd_parse.py`-style experiments but is ignored by other scripts.
