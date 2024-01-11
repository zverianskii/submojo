from setuptools import setup, find_packages


def main():
    setup(
        name="submojo",
        use_scm_version=True,
        description="",
        version="0.0.1",
        url="",
        author="Aleksandr Zverianskii",
        author_email="",
        license="MIT",
        scripts=["scripts/git_subdir.sh"],
        classifiers=[
            "License :: OSI Approved :: MIT License",
        ],
        py_modules=["submojo"],
        entry_points={
            "console_scripts": [
                "sm = submojo:cli",
            ],
        },
        keywords="",
        packages=find_packages(exclude=[]),
        install_requires=["requests", "click"],
    )


if __name__ == "__main__":
    main()
