# 🔷 Algorand Utils Examples

![Python](https://img.shields.io/badge/python-3.14-blue.svg)
![Algorand](https://img.shields.io/badge/blockchain-Algorand-00D1B2.svg)
![AlgoKit](https://img.shields.io/badge/AlgoKit-Utils-orange.svg)
![Learning](https://img.shields.io/badge/project-educational-yellow.svg)

Educational project demonstrating Algorand blockchain development using Python and AlgoKit Utils. This repository provides practical examples of account management, transactions, and asset operations on the Algorand blockchain.

---

## 🚀 Features

### 💼 Account Management (`accounts.py`)
- ✅ Create/load accounts from environment variables
- ✅ Generate random testnet accounts
- ✅ Check account balances
- ✅ Convert between mnemonic and private keys
- ✅ Support for LocalNet, TestNet, and MainNet
- ✅ Automatic account funding on LocalNet

### 💸 Transactions (`transaction.py`)
- ✅ Simple payment transactions (ALGO transfers)
- ✅ Atomic group transactions (all-or-nothing execution)
- ✅ Flexible input (accepts `SigningAccount` or address strings)
- ✅ Automatic microAlgo conversion

### 🪙 Asset Operations (`assets.py`)
- ✅ Create custom assets (tokens/NFTs)
- ✅ Opt-in to assets (enable receiving)
- ✅ Opt-out from assets (remove from account)
- ✅ Transfer assets between accounts
- ✅ Check asset balances
- ✅ Support for decimals and asset configuration

---

## 📦 Quick Start

### Prerequisites

- **Python 3.14+**
- **Poetry** (dependency management)
- **Docker** (for LocalNet)
- **AlgoKit CLI**

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/CorvidLabs/algo-utils-examples.git
   cd algo-utils-examples
   ```

2. **Install dependencies:**
   ```bash
   poetry install
   ```

3. **Start Algorand LocalNet:**
   ```bash
   algokit localnet start
   ```
   
   > ⏳ Wait 30-60 seconds for LocalNet to fully initialize.

4. **(Optional) Configure custom accounts:**
   
   Create a `.env` file in the project root:
   ```env
   JOAO_MNEMONIC="your 25 word mnemonic phrase here"
   JOSE_MNEMONIC="your 25 word mnemonic phrase here"
   ```
   
   > **Note:** If you don't create a `.env` file, LocalNet will automatically generate and manage accounts using KMD.

5. **Run the examples:**
   ```bash
   poetry run python -m algo_utils_examples.main
   ```
   
   Or if you've configured the script in `pyproject.toml`:
   ```bash
   poetry run algo-utils-examples
   ```

---

## 📚 Usage Examples

### Account Management

```python
from algo_utils_examples.accounts import create_account, get_balance
from algokit_utils import AlgorandClient

# Create Algorand client
algorand = AlgorandClient.default_localnet()

# Load account from environment (or create via KMD if not found)
account = create_account(algorand, "SARA", initial_algo=1000)

# Check balance
balance = get_balance(algorand, account.address)
print(f"Balance: {balance} ALGO")
```

### Simple Payment

```python
from algo_utils_examples.transaction import payment

# Send 10 ALGO from Sara to Jose
result = payment(
    algorand=algorand,
    sender=sara,  # Can be SigningAccount or address string
    receiver=jose,
    algo=10.0,
    note=b"Payment for services"
)
print(f"Transaction ID: {result.tx_id}")
```

### Atomic Group Transaction

```python
from algo_utils_examples.transaction import group_transaction
from algokit_utils import PaymentParams, AlgoAmount

# Multiple payments that execute together (atomic)
params = [
    PaymentParams(
        sender=sara.address,
        receiver=jose.address,
        amount=AlgoAmount.from_algo(5),
        note=b"Payment 1"
    ),
    PaymentParams(
        sender=jose.address,
        receiver=sara.address,
        amount=AlgoAmount.from_algo(3),
        note=b"Payment 2"
    )
]

result = group_transaction(algorand, params)
print(f"Group ID: {result.group_id}")
```

### Create an Asset

```python
from algo_utils_examples.assets import create_asset

# Create a token with 6 decimals
asset_id = create_asset(
    algorand=algorand,
    sender=sara,
    name="My Token",
    unit_name="MTK",
    total=1_000_000_000_000,  # 1 trillion base units
    decimals=6,               # = 1 million whole tokens
    frozen=False
)
print(f"Asset ID: {asset_id}")
```

### Asset Operations

```python
from algo_utils_examples.assets import opt_in, assets_transfer, get_asset_balance

# Jose opts in to receive the asset
opt_in(algorand, jose, asset_id)

# Sara transfers 100 tokens to Jose (considering decimals=6)
# To transfer 100 whole tokens: 100 × 10^6 = 100,000,000 base units
assets_transfer(
    algorand=algorand,
    sender=sara,
    receiver=jose,
    asset_id=asset_id,
    amount=100_000_000,  # 100 tokens with 6 decimals
    note=b"Token transfer"
)

# Check Jose's balance
balance = get_asset_balance(algorand, jose, asset_id)
print(f"Jose's token balance: {balance}")
```

---

## 📁 Project Structure

```
algo-utils-examples/
├── src/
│   └── algo_utils_examples/
│       ├── __init__.py
│       ├── accounts.py      # Account management utilities
│       ├── transaction.py   # Payment and group transactions
│       ├── assets.py        # Asset creation and operations
│       └── main.py          # Example usage and demonstrations
├── tests/                   # Unit tests (to be added)
├── .env                     # Environment variables (optional, not in git)
├── pyproject.toml           # Project dependencies and configuration
├── poetry.lock              # Locked dependencies
└── README.md                # This file
```

---

## 🎓 Key Concepts

### Asset Decimals

Assets on Algorand use **base units** (integers) internally, but can display decimal places to users:

- `decimals=0`: Whole units only (e.g., NFTs)
- `decimals=2`: Like dollars and cents (1.00)
- `decimals=6`: Like USDC (1.000000)

**Example:** An asset with `total=1_000_000` and `decimals=2` displays as **10,000.00** to users.

**Formula:**
```
Value shown to user = total ÷ (10^decimals)
```

### Atomic Transactions

Atomic group transactions ensure **all transactions succeed or all fail together**. This is perfect for:
- Swaps/trades
- Multi-party agreements
- Complex operations that must be atomic

### Opt-In Requirement

Before receiving an asset, accounts must **opt-in** to it. This:
- Prevents spam assets
- Gives users control over their account
- Requires a small ALGO balance to maintain

---

## 🛠️ Technologies

| Technology | Purpose |
|------------|---------|
| **Python 3.14** | Programming language |
| **AlgoKit Utils** | Algorand SDK wrapper |
| **Poetry** | Dependency management |
| **Algorand LocalNet** | Local blockchain for testing |
| **Docker** | Containerization for LocalNet |
| **algosdk** | Algorand Python SDK |

---

## 🐛 Troubleshooting

### LocalNet not starting
```bash
# Stop and reset LocalNet
algokit localnet reset

# Start fresh
algokit localnet start
```

### Account not found error
- Make sure `.env` file has correct mnemonic phrases
- Or let LocalNet auto-generate accounts (don't use `.env`)

### Transaction failed: balance too low
- Check account balance: `get_balance(algorand, address)`
- Fund TestNet accounts using the [TestNet Dispenser](https://bank.testnet.algorand.network/)

### Asset opt-in required
- Before receiving assets, run: `opt_in(algorand, account, asset_id)`

### Import errors
- Make sure you're running as a module: `poetry run python -m algo_utils_examples.main`
- Or configure script in `pyproject.toml` and use: `poetry run algo-utils-examples`

---

## 📚 Learning Resources

### Official Documentation
- [Algorand Developer Portal](https://developer.algorand.org/)
- [AlgoKit Documentation](https://github.com/algorandfoundation/algokit-cli)
- [AlgoKit Utils Python](https://algorandfoundation.github.io/algokit-utils-py/)

### Tutorials & Examples
- [AlgoKit Utils Notebook Examples](https://github.com/algorandfoundation/algokit-templates/tree/main/examples/python-utils-notebook)
- [Algorand Smart Contract Examples](https://github.com/algorandfoundation/algokit-examples)

### Tools
- [Lora (LocalNet Explorer)](https://lora.algokit.io/localnet)
- [AlgoExplorer (TestNet/MainNet)](https://testnet.algoexplorer.io/)
- [TestNet Dispenser](https://bank.testnet.algorand.network/)

---

## 🤝 Contributing

This is an educational project, but contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 🙏 Acknowledgments

This project was developed as a learning exercise with assistance from:
- **AI Tools:** Claude/Cursor for code review, best practices, and blockchain concepts
- **Mentors:** [Leif](https://github.com/0xLeif) and [Gaspar](https://github.com/0xGaspar) for programming guidance and support
- **Algorand Foundation:** For excellent documentation and tools

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

---

**Happy coding on Algorand! 🚀**
