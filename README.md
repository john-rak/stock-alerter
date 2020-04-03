# stock-alerter
Markets are moving, let's get with the times...



Interacting with the GitHub repo:

1. To start:
   - `git clone [repo_url]`


1. To make a change directly:
    - `git pull`
    - ... do changes ...
    - `git add --all`
    - `git commit -m "[message about what was changed]"`
    - `git push`

2. To make a change you want reviewed:
    - `git pull`
    - `git checkout -b branch_name_for_edits`
    - ... do changes ...
    - `git add --all`
    - `git commit -m "[message about what was changed]"`
    - `git push`
    - then on github, go to your branch, click "Create new pull request", request reviewers on the right sidebar, and open the PR 


1. Create and activate virtualenv running Python 3.7.5.  Below is an example of how this can be done on a Mac with [Brew](https://brew.sh/), but any virtualenv works.
    - `brew install pyenv-virtualenv`
    - `pyenv install -s 3.8`
    - `eval "$(pyenv init -)" # add this to ~/.profile`
    - `pyenv virtualenv -p python3.8 3.8.0  stock-alerter-3.8.0`
    - `pyenv activate stock-alerter-3.8.0`
    - `pip install -r requirements.txt`