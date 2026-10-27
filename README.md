# TP1: Advanced Digital Signature Scheme (IoT Security)

This repository contains the practical work (TP1) implementation for the IoT Security & Cybersecurity module.

## 👥 Team Members
* Member 1 Name
* Member 2 Name

## 📂 Repository Structure
* `DESIGN.md`: One-page design document detailing the scenario, parties, and security properties[cite: 2].
* `signature.py`: Core implementation of the chosen advanced signature scheme.
* `test_signature.py`: Correctness tests (valid signatures, modified messages, wrong keys)[cite: 2].
* `test_properties.py`: Variant-specific property tests (e.g., ring anonymity check)[cite: 2].
* `benchmark.py`: Performance benchmarking script (signing/verification time and signature size)[cite: 2].
* `iot_demo.py`: MQTT simulation connecting 10 sensors to a gateway[cite: 2, 3].

## 🚀 How to Reproduce Results
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/tp1-signatures.git](https://github.com/your-username/tp1-signatures.git)
   pip install pynacl cryptography paho-mqtt matplotlib
   python test_signature.py
   python iot_demo.py
