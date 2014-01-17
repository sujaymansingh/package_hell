import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="small-util",
        description="Some small util",
        version="0.0.1",
        author="Sujay",
        author_email="sujay@example.com",
        packages=setuptools.find_packages(),
        include_package_data=True,
        url="https://github.com/sujaymansingh/package_hell",
        install_requires=["docopt==0.6.1"]
    )
