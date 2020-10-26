# dataiku-plugin-tests-utils
Common tooling for DSS plugins

# How to install in your plugin
To install the `dataiku-plugin-tests-utils` package for your plugins use the
following line depending on your prefered way to managed packages and situation
you are in.
## Using Requierement.txt
### Development cycle
`git+git://github.com/dataiku/dataiku-plugin-tests-utils.git@<BRANCH>#egg=dku_plugin_test_utils/`
Replace `<BRANCH>` by the most accurate value
### Stable release (untested for now)
git+git://github.com/dataiku/dataiku-plugin-tests-utils.git@releases/tag/<RELEASE_VERSION>#egg=dku_plugin_test_utils/
Replace `<RELEASE_VERSION>` by the moist accurate value

## Using Pipfile
Put the following line under `[dev-packages]` section
### Development cycle
`dku_plugin_test_utils = {git = "git://github.com/dataiku/dataiku-plugin-tests-utils.git", ref = "<BRANCH>"}`
### Stable release
TBD
