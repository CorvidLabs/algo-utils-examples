# 🔷 Algorand Utils Examples

Educational project to learn Algorand blockchain development using Python.

## 🚀 Features

- ✅ Account management
- ✅ Simple payment transactions
- ✅ Atomic group transactions

## 📦 Setup

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Start LocalNet:
   ```bash
   algokit localnet start
   ```

3. **(Optional)** Create `.env` for custom accounts:
   ```
   JOAO_MNEMONIC="your 25 word mnemonic phrase here"
   JOSE_MNEMONIC="your 25 word mnemonic phrase here"
   ```
   
   **Note:** If you don't create `.env`, LocalNet will automatically 
   generate and manage accounts for you using KMD.

4. Run the project:
   ```bash
   poetry run python src/algo_utils_examples/main.py
   ```

## 🛠️ Technologies

- Python 3.14
- AlgoKit Utils
- Poetry
- Algorand LocalNet
- Docker

## 📚 Learning Resources

- [Algorand Developer Portal](https://developer.algorand.org/)
- [AlgoKit Documentation](https://github.com/algorandfoundation/algokit-cli)
- [Algokit Utils Documentation](https://algorandfoundation.github.io/algokit-utils-py/#)

## 📄 License

MIT
