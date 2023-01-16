# streetslab.github.io

This website is built using Sphinx, which is popular for building documentation websites for Python packages.

To edit the website, create a new environment and install the packages in `requirements.txt`. Then, for a live build run `sphinx-autobuild docs docs/_build/html` from the root of the repository. This will build the website and serve it at `localhost:8000`.

All edits to the `main` branch are built via GitHub Actions and deployed to the `gh-pages` branch, which is where the website is hosted.

Edits to the website should be made via PRs to this repository.
