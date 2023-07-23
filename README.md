# pyluca
A headless Python double entry accounting package. It is Python [Luca Pacioli][luca] :) 
It is a plug and play Python module, which does NOT come with any server or databases.
It helps you to build your own application using core double entry accounting (pyluca)
module.

## Usage
On a high level, you just need to do the following steps to start using it.

1. Setup accounting configuration
2. Pass journal entries
3. Get balances

## Example
**You need to have basic accounting/bookkeeping knowledge to set up the configuration**

Check out `demo/personal_finance.py` for examples. You can even check out `pyluca/tests` for advanced usage.

1. Basic accounting configuration
2. Creating an accountant and passing journal entries
3. Creating events and configuring actions
4. Ledger usage and as of any "time"

[luca]: https://enwp.org/Luca_Pacioli
