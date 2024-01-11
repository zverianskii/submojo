# SUBMOJO

easy way to add others code from GitHub repos, while we don't have package manager.

Install:
```sh
pip install git+ssh://git@github.com/zverianskii/submojo.git
```

To list available repos:
```sh
sm list
```

To add:
```sh
sm add <repo_name>
```

```sh
sm add -i <repo_index_from_list>
```

Current index: https://gist.github.com/zverianskii/185aaea9e26702e50fc035411ae6cdf5

Don't like it?
1. create a gist with the same structure
2. set env variable MOJO_PACKAGES_INDEX_URL