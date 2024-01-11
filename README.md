# SUBMOJO

Submojo offers a simplified solution for incorporating other GitHub repositories', while we are waiting for a package manager.

## Installation:

Use the following command to install Submojo:

```sh
pip install git+ssh://git@github.com/zverianskii/submojo.git
```

## Usage:

To see a list of available repositories, use the following command:

```sh
sm list
```

To add a repository, use either of the following commands:

```sh
sm add <repo_name>
```

OR

```sh
sm add -i <repo_index_from_list>
```

Current index can be found here: https://gist.github.com/zverianskii/185aaea9e26702e50fc035411ae6cdf5

## Contributions:

If you wish to add something to the index, we welcome Pull Requests!

## Customization:

If you are not satisfied with the current index, you can:

1. Create a gist with the same structure, and
2. Set the environment variable MOJO_PACKAGES_INDEX_URL
