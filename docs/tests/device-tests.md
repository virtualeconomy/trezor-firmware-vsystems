# Running device tests

## 1. Running the full test suite

_Note: You need Pipenv, as mentioned in the core's [documentation](https://docs.trezor.io/trezor-firmware/core/) section._

In the `trezor-firmware` checkout, in the root of the monorepo, install the environment:

```sh
pipenv sync
```

And run the automated tests:

```sh
pipenv run make -C core test_emu
```

## 2. Running tests manually

Install the pipenv environment as outlined above. Then switch to a shell inside the
environment:

```sh
pipenv shell
```

If you want to test against the emulator, run it in a separate terminal from the `core`
subdirectory:
```sh
PYOPT=0 ./emu.sh
```

Now you can run the test suite with `pytest` from the root directory:
```sh
pytest tests/device_tests
```

### Useful Tips

The tests are randomized using the [pytest-random-order] plugin. The random seed is printed in the header of the tests output, in case you need to run the tests in the same order.

If you only want to run a particular test, pick it with `-k <keyword>` or `-m <marker>`:

```sh
pytest -k nem      # only runs tests that have "nem" in the name
pytest -m stellar  # only runs tests marked with @pytest.mark.stellar
```

If you want to see debugging information and protocol dumps, run with `-v`.

If you would like to interact with the device (i.e. press the buttons yourself), just prefix pytest with `INTERACT=1`:

```sh
INTERACT=1 pytest tests/device_tests
```

## 3. Using markers

When you're developing a new currency, you should mark all tests that belong to that
currency. For example, if your currency is called NewCoin, your device tests should have
the following marker:

```python
@pytest.mark.newcoin
```

This marker must be registered in [REGISTERED_MARKERS] file.

If you wish to run a test only on TT, mark it with `@pytest.mark.skip_t1`.
If the test should only run on T1, mark it with `@pytest.mark.skip_t2`.
You must not use both on the same test.

[pytest-random-order]: https://pypi.org/project/pytest-random-order/
[REGISTERED_MARKERS]: ../REGISTERED_MARKERS
