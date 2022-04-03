# Usage

## How to use?

### Setup

To run this program you have to setup your environment by below commands.

```bash
make install
make setup
```

### Run the example

After you run the program, the output file will be stored in the root.

```bash
python examples/spy.py
```

### Example code

You can change the STOCK variable to other symbol you want to request. (Only support US Stock).

```python
import cnbc

STOCK = "SPY"

client = cnbc.Client()
client.apply(STOCK, client.queryQuote, client.save)
```
