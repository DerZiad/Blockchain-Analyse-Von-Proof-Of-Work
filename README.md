# Blockchain Technology: Analysis of Proof of Work (Bitcoin)

Seminar project completed in the **Applied Mathematics and Computer Science** degree program at **FH Aachen, Campus Jülich**.

This repository documents a German-language study of blockchain technology with a focus on Bitcoin's Proof-of-Work (PoW) consensus mechanism. It combines a written report, presentation slides, LaTeX source material, and a small Python demonstration of nonce-based mining.

[Read the report](./report.pdf) · [View the presentation](./presentation.pptx) · [Open the Python demo](./example.py)

## Academic context

| | |
|---|---|
| **Institution** | FH Aachen University of Applied Sciences |
| **Campus** | Jülich |
| **Faculty** | Medical Engineering and Technomathematics |
| **Degree program** | Applied Mathematics and Computer Science |
| **Project type** | Seminar paper |
| **Author** | Ziad Bougrine |
| **Date** | March 2023 |
| **Language** | German |
| **Reviewers** | Prof. Dr. rer. nat. Volker Sander and M. Sc. Lukas Walk |

## Topics covered

- Blockchain fundamentals, block structure, hashes, Merkle trees, and decentralization
- Proof-of-Work mechanics, nonce discovery, mining pools, and difficulty adjustment
- Benefits and limitations of PoW, including security, energy use, scalability, and mining-pool concentration
- Sidechains, two-way pegs, smart contracts, and Bitcoin sidechain examples
- Security threats such as Sybil attacks, double spending, 51% attacks, and routing attacks

## Repository contents

| Path | Description |
|---|---|
| [`report.pdf`](./report.pdf) | Complete 46-page seminar paper |
| [`presentation.pptx`](./presentation.pptx) | 27-slide presentation accompanying the paper |
| [`example.py`](./example.py) | Simplified SHA-256 nonce-search demonstration |
| [`tex-code/`](./tex-code/) | LaTeX working files, diagrams, figures, and course template material |

The pre-built PDF is the easiest way to read the paper. The `tex-code/` directory preserves the original working environment and also contains template and exercise files from the associated LaTeX coursework.

## Run the mining demonstration

The example uses only Python's standard library. Pass the desired difficulty as a command-line argument:

```bash
python3 example.py 4
```

The difficulty is the number of leading hexadecimal zeroes required in the SHA-256 hash. The script changes the nonce until it finds a matching hash or reaches its nonce limit.

Each additional leading zero makes the expected search roughly 16 times harder, so start with a value between `1` and `4`. Runtime depends on the selected difficulty and the computer running the script.

> **Note:** This script illustrates the core search idea behind PoW. It does not implement Bitcoin's block format, network protocol, target encoding, or mining rules and must not be treated as a production miner.

## Scope and status

This repository preserves an academic submission from 2023. The report and slides reflect the sources and state of the technology at the time of writing; cryptocurrency protocols, network statistics, and ecosystem details may have changed since then.

## License

No license file is currently included. Standard copyright restrictions therefore apply. If you would like to reuse material from this project, please contact the author or open an issue in the [GitHub repository](https://github.com/DerZiad/Blockchain-Analyse-Von-Proof-Of-Work).
