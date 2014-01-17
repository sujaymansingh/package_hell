import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="big-util",
        description="Some big util",
        version="0.0.1",
        author="Sujay",
        author_email="sujay@example.com",
        packages=setuptools.find_packages(),
        include_package_data=True,
        url="https://github.com/sujaymansingh/package_hell",
        install_requires=["nose==1.3.0"],
        dependency_links=["https://s3-eu-west-1.amazonaws.com/sujaymansingh-foo/small-util-0.0.1.tar.gz"]
    )
