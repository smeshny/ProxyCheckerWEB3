# ProxyCheckerWEB3
Continuously monitors the health of proxy servers in relation to Web3 RPC endpoints. Well-suited for static server proxies.

## Requirements

- Python 3.11

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/smeshny/ProxyCheckerWEB3.git
   ```

2. Navigate to the project directory:
   ```
   cd ProxyCheckerWEB3
   ```

3. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Add HTTP (!) proxy servers to check in the `data/proxies.xlsx` file. The format should be as follows:
   ```
   | Name   | HTTP Proxy (any format)          |
   |--------|----------------------------------|
   | Name1  | host:port@login:password         |
   | Name2  | host:port@login:password         |
   | Name3  | host:port|login:password         |
   | Name4  | login:password@host:port         |
   | Name5  | http://host:port:login:password  |
   | Name6  | http://host:port@login:password  |
   | Name7  | http://host:port@login:password  |
   | Name8  | http://host:port|login:password  |
   | Name9  | http://login:password@host:port  |
   | Name10 | http://login:password@host:port  |
   ```

2. Configure settings in the `data/config.py` file. Be cautious with the delay settings because the script works asynchronously. If the delays are too short, you might overwhelm the proxy or RPC provider.
3. Run the script:
   ```
   python main.py
   ```

## Results

Check results are saved in the `data/results/` directory in Excel format. A new Excel file is created after each check.

## Author

[MimbleWimbleLAB](https://t.me/MimbleWimbleLAB)