import os
import subprocess
import json
import requests
import click
from pprint import pprint
from distutils.util import strtobool

INDEX_URL = os.environ.get(
    "MOJO_PACKAGES_INDEX_URL",
    "https://api.github.com/gists/185aaea9e26702e50fc035411ae6cdf5",
)


def interactive_y_n(question):
    while True:
        try:
            reply = str(input(question + " (y/n): ")).lower().strip()
            return strtobool(reply)
        except ValueError as e:
            pprint("Please enter yes or no!")
            pass


def get_repos():
    try:
        r = requests.get(INDEX_URL)
        repos = json.loads(
            json.loads(r.text)["files"]["mojo_packages_index"]["content"]
        )
        return repos
    except Exception as e:
        print("can't get index: ", e)
    return []


@click.group()
def cli():
    pass


@cli.command(name="list")
def list_index():
    index = get_repos()
    pprint(list(enumerate(index)))


@cli.command()
@click.argument("name", required=False)
@click.option("-i", required=False, type=int, help="index in list", default=None)
def add(name, i):
    repos = get_repos()
    repo_config = {}
    if name:
        if not (repo_config := next(filter(lambda v: v["name"] == name, repos), None)):
            raise Exception("No such name!")
    elif i is not None:
        if i >= len(repos):
            raise Exception("Index out of range!")
        repo_config = repos[i]
    if repo_config:
        print("Found: ")
        pprint(repo_config)
        if interactive_y_n("Do you want to add?"):
            subprocess.call(
                ["git_subdir.sh", repo_config["ssh_url"], repo_config["folder_name"]]
            )
    else:
        print("No such repo!")
