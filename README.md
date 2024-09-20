# ProxyCheckerWEB3
Continuously monitors the health and performance of Web3 RPC endpoints via proxies

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/ProxyCheckerWEB3.git
   ```

2. Navigate to the project directory:
   ```
   cd ProxyCheckerWEB3
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Add proxy servers to check in the `data/proxies.txt` file.
2. Configure settings in the `data/config.py` file.
3. Run the script:
   ```
   python main.py
   ```

## Module Descriptions

- `main.py`: Main script to run the proxy check.
- `data/config.py`: Configuration file with settings.
- `data/proxies.txt`: List of proxy servers to check.
- `utils/logger.py`: Logging module.
- `utils/rpc_checker.py`: Module for checking RPC through proxies.
- `utils/proxy_manager.py`: Proxy server manager.
- `utils/result_processor.py`: Processing and saving results.

## Results

Check results are saved in the `data/results/` directory in Excel format.

## License

[Specify your license, e.g., MIT]

## Author

[Your name or username]