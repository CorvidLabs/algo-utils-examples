# 🔷 Algorand Utils Examples
![Python](https://img.shields.io/badge/python-3.14-blue.svg)
![Algorand](https://img.shields.io/badge/blockchain-Algorand-00D1B2.svg)
![AlgoKit](https://img.shields.io/badge/AlgoKit-Utils-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Learning](https://img.shields.io/badge/project-educational-yellow.svg)

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

## 🙏 Acknowledgments

This project was developed as a learning exercise with assistance from AI (Claude/Cursor) 
for code review, best practices guidance, and educational explanations about Algorand blockchain development.
Special thanks to [Leif](https://github.com/0xLeif) and [Gaspar](https://github.com/0xGaspar) for helping me so much with programming concepts and tools!

## 📄 License

MIT
