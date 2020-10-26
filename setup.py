import setuptools

with open("README.md", "r") as fd:
    long_desc = fd.read()


setuptools.setup(
    name="dataiku-plugin-tests-utils",
    version="0.0.1",
    description="The common tooling needed for each plugin",
    author="Dataiku",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.dataiku.com",
    packages=["dku_plugin_test_utils"],
    classifiers = [
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Topic :: Software Development :: Libraries',
            'Programming Language :: Python',
            'Operating System :: OS Independent'
        ],
    python_requires='>=2.7'
)
