# nimmer

Create acronyms from sentences

## What is this?

This is a toy package we [created together on Twitch on 2022-01-26](https://www.twitch.tv/videos/1277115435) as a way to talk about some of what people can learn in [_Publishing Python Packages: Test, share, and automate your projects_](https://pypackages.com) and the corresponding [code companion](https://github.com/daneah/publishing-python-packages).

## Tools mentioned

* [asdf](https://asdf-vm.com/): Install base versions of various language runtimes
* [python-launcher](https://github.com/brettcannon/python-launcher): A convenient way to run the Python you mean. Not strictly necessary, but very convenient (semi-ported behavior from Windows Python).
* [pipx](https://pypa.github.io/pipx/): Install command-line interface tools for global use.
* [build](https://pypa-build.readthedocs.io/en/stable/): A PEP 517-compliant package build tool from PyPA.
* [tox](https://tox.wiki/en/latest/): Testing and task management tool extraordinaire.
* [pytest](https://docs.pytest.org/en/6.2.x/): A nicer way of unit testing.
* [black](https://black.readthedocs.io/en/stable/): Format your code consistently.
* [mypy](http://www.mypy-lang.org/): Check your code for type errors.
* [flake8](https://flake8.pycqa.org/en/latest/index.html): Check your code for common bugs.
* [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/): Create reusable project templates.

## PEPs mentioned

* [PEP 8](https://www.python.org/dev/peps/pep-0008/): Code formatting
* [PEP 420](https://www.python.org/dev/peps/pep-0420/): Implicit namespace packages
* [PEP 517](https://www.python.org/dev/peps/pep-0517/): New package build framework

## Command cheat sheet

| Command | Purpose / explanation |
| --- | --- |
| `py -3.10 -m venv .venv` | Using python-launcher, find the Python 3.10 base version and use its `venv` module to create a virtual environment in a `.venv/` directory. |
| `py -m pip install -r requirements.txt` | Using python-launcher to automatically pick up the copy of Python in `.venv/`, use that Python's `pip` module to install requirements into the virtual environment. |
| `pyproject-build .` | Using `build`, build the current directory as a package using the PEP 517 approach. |
| `tox` | Run the default environment(s) specified in tox's `envlist`. You can also run them explicitly with `tox -e py310`, as an example. |
| `tox -e format` | Run the `format` environment |

## What's in the book that we didn't cover

* More detail on all of what we did cover, with some extra tips and tricks
* Creating non-Python extensions in C using Cython
* Creating command-line interfaces as packages
* Creating and automating documentation
* Automating testing and code quality with GitHub Actions
* Extracting a project template with cookiecutter
* Starting an effective community for your project

## Note from the Twitch session

The issue with `tox -e typecheck` at the end turned out to be because we were packaging up the `dist/` directory we created by running `pyproject-build`. This is where the `MANIFEST.in` file is helpful, because it can filter out files you *don't* want in your package. I typically include the following in my `MANIFEST.in`, which only includes files inside the `src/` directory and excludes some generated files:

```
graft src
recursive-exclude __pycache__ *.py[cod]
```

Even after that, type checking failed because we had added `mypy .` as the command -- this ends up trying to type check `setup.py`, which imports `setuptools`, which has no type hints available. Updating the command to `mypy --ignore-missing-imports .` fixes the issue, or you can update to only check your source code and tests with `mypy src tests`.
