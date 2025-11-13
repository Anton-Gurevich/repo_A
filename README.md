# repo_A
Example Parent Repository A. Should contain:
- Folder `src/` with source code files `src/repo_a/<module.py>`.
- Folder `tests/` with test files.
- `README.md` with project description.
- `pyproject.toml` for project configuration.
- `.gitignore` to exclude unnecessary files from version control.

## Shared Libraries as Git Submodules in a parent repository:
```
project/
  pyproject.toml
  src/project_pkg/...
  external/
    shared-a/      # submodule -> its own repo
      pyproject.toml
      src/shared_a/...
    shared-b/      # submodule -> its own repo
      pyproject.toml
      src/shared_b/...
    shared-c/      # submodule -> its own repo
      pyproject.toml
      src/shared_c/...
  tests/

```

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
   
2. Make changes in the submodule located at `external/repo_B`. Commit to the submodule repo (inside its folder):
    ```
    cd external/repo_B
    git checkout -b fix/foo
    git commit -am "Fix: foo"
    git push origin fix/foo
    # open PR in the shared-lib repo
    ```
   
3. After merging upstream, update the parent to the new pinned commit:
    ```
    cd external/repo_B
    git fetch
    git checkout main
    git pull
    ```

3. Go back to the main project directory, stage the submodule update, and commit:
   ```
   cd ../..
   git add external/repo_B
   git commit -m "Update submodule to latest commit"
   # continue working on repo_A as usual
   git push origin main
   ```