# repo_A
Example Repository A. Should contain:
- Folder `src/` with source code files.
- example Python module `module_a.py` inside `src/`.
- Folder `tests/` with test files.
- `README.md` with project description.
- `pyproject.toml` for project configuration.
- `.gitignore` to exclude unnecessary files from version control.

# Quick Start
To set up the project with the shared library as a submodule, follow these steps:
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

# Workflow
1. Fetch the latest changes in the submodule:
   ```
   git submodule update --remote --merge
   ```
2. Make changes in the submodule located at `external/repo_B`.
3. Commit and push changes in the submodule:
   ```
   cd external/repo_B
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```
4. Go back to the main project directory, stage the submodule update, and commit:
   ```
   cd ../..
   git add external/repo_B
   git commit -m "Update submodule to latest commit"
   git push origin main
   ```