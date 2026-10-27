# TP1 Design Document: Advanced Digital Signature Scheme

## 1. Scenario & Parties
* **Scenario:** IoT sensor nodes measuring environmental data and publishing securely to a central gateway.
* **Parties:** 
  * **Devices (Sensors):** Constrained IoT nodes generating measurements.
  * **Gateway:** Collects and verifies incoming signed messages.
  * **Manager / Issuer:** Manages keys or group memberships.

## 2. Chosen Variant
* **Variant:** Ring Signature (e.g., Schnorr-based ring signature on Ed25519)[cite: 2].

## 3. Security Properties to Demonstrate
* **Anonymity:** A verifier cannot determine which specific device in the ring signed the message[cite: 2].
* **Unforgeability:** Only members holding valid keys can produce a valid ring signature.
