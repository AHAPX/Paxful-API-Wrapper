
# General
This package contains a python wrapper for the Paxful Cryptocurrency Exchange APIv1. It utilizes the requests python 
package to communicate with the API. A Paxful account is required and must be authenticated using your own  API key.

Please visit https://paxful.readthedocs.io/ for more details on the API. 

# Install
This package can be installed from the PyPi repository.

`pip install paxful-api`

You can also download the zip and and place it into a Virtual Environment created using virtualenv (recommended).

# Setup
In the main client, you must define your API key and API secret.
Example:

`api_key=cinow2P4gwP8hCD_MTe6p-YlnhQIeRrtiQswcxx 
api_secret=F8Rt6xuKwertRpLVs7vowoDwertX79O_39RK1kLdxx`

The _main client_ is used for general operations such as opening a trade, creating offers, fetching available payment 
methods, and getting transaction information.

The _trade client_ is used for specific trade operations such as chatting, releasing funds, sending pictures and giving
feedback. **Each trade client object represents an individual trade.** _Do not initialize a trade object directly from the
trade client, always use the main client_. See the example below.

## Example
After installing, import:

`from paxful.main_client import PaxfulClient`

Initialize the client:  

`client = PaxfulClient()`

Get the list of active trades:

`trades = client.trade_list()`

Extract the _hash id_ of each trade and create a trade object:

`tr = client.trade(hash_id)` 

# LICENSE
MIT License

Copyright (c) 2019 Tyvaughn Holness

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.