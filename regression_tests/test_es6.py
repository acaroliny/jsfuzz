from regression_tests import * #pylint: disable=W0614

#@pytest.mark.skip(reason="temporarilly disabling")
def test_ec6():
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6')
    multicall.multicall_directories(path_name, False)

