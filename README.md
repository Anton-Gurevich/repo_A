# repo_A
Example Repository A. Should contain:
- Folder `src/` with source code files.
- example Python module `module_a.py` inside `src/`.
- Folder `tests/` with test files.
- `README.md` with project description.
- `pyproject.toml` for project configuration.
- `.gitignore` to exclude unnecessary files from version control.

# init
```
git clone https://github.com/Anton-Gurevich/repo_A.git
cd repo_A
git submodule add -b main https://github.com/Anton-Gurevich/repo_B.git external/repo_B
git commit -m "Add shared-lib as submodule"

git submodule update --init --recursive
python -m venv .venv && source .venv/bin/activate
pip install -e external/repo_B
pip install -e .
```