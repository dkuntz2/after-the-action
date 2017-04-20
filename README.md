# After the Action

An application for collecting and sharing After Action Reports (AARs) from megagames.
(Better description eventually)

## Running locally

**NOTE**: Currently development is done on a machine running Python 3.6.
Backwards compatibility is not guaranteed, but most lower versions of Python 3 _should_ work.

- Setup a virtualenv
- Install the requirements `pip install -r requirements.txt`
- Install [foreman](https://ddollar.github.io/foreman/) (`gem install foreman`)
- `foreman start`
- Curl locally on port 5000 (by default, you can use `foreman start -p <port>` to change that)
