# Free-Order Logic (FOL) Specification
**Version:** 1.0 (Draft)
**Architect:** kedi-kat

## 1.0 Abstract
Free-Order Logic (FOL) is a commutative, non-linear state description language designed for swarm robotics, distributed IoT systems, and xeno-linguistic analysis. Unlike traditional linear programming, FOL does not rely on sequence or synchronized time; it relies on **State Clouds**.

In FOL, `A.B` is functionally identical to `B.A`. This allows for robust, asynchronous coordination in high-latency or chaotic environments (e.g., nanobots in fluid dynamics, deep-space probes).

## 2.0 Core Philosophy: Digital Stigmergy
FOL is designed to enable **Stigmergy** (communication through the environment). Agents do not pass messages linearly; they modify the shared state environment.
* **Statelessness:** Logic is derived from the current density of tokens, not a historical log.
* **Non-Linearity:** The parser ignores sequence. It processes "Clouds" of tokens.
* **Locality:** Logic is executed at the edge (on the agent), removing the need for a central clock or satellite uplink.

## 3.0 Syntax & Semantics

### 3.1 The State Cloud
A valid instruction is defined as a cluster of 2 or more tokens.
* **Format:** `Subject.State.Modifier`
* **Example:** `Motor.Forward.HighIntensity`
* **Rule:** The order of tokens MUST NOT affect execution. `Motor.Forward` and `Forward.Motor` resolve to the same bytecode.

### 3.2 Conflict Resolution: The "Net Force" Rule
Unlike traditional logic which throws errors on conflict, FOL treats contradictory states as opposing physics vectors.
* **Rule:** If a subject receives conflicting states (e.g., `Motor.Forward` and `Motor.Backward`), the parser MUST sum the intensity of the tokens (Vector Summation).
* **Behavior:** Conflicting tokens cancel each other out via destructive interference.
    * *Example:* Input `Forward` (Intensity 5) + `Backward` (Intensity 3) = Result `Forward` (Intensity 2).
* **Result:** This allows for smooth "drift" and democratic decision-making within a swarm.

## 4.0 The Subsumption Architecture (The "Brain")
To ensure survival in chaotic environments, FOL parses states using a strict three-layer hierarchy. Higher layers **subsume** (override) lower layers.

### Layer 1: The Safety Interlock (Priority Override)
* **Function:** Immediate survival reflexes.
* **Rule:** Tokens tagged as `CRITICAL` (e.g., `Danger`, `Halt`) trigger an immediate **Interrupt**.
* **Behavior:** The parser ignores all other tokens. The `CRITICAL` state executes instantly.

### Layer 2: The Consensus Engine (Vector Summation)
* **Function:** Navigation and Swarm Coordination.
* **Rule:** If no `CRITICAL` tokens are present, the parser sums the vectors of all active states.
* **Behavior:** The output is the **Net Vector** of the swarm's intent.

### Layer 3: The Entropy Floor (Signal Decay)
* **Function:** Garbage collection.
* **Rule:** All states possess a `Time-To-Live (TTL)`.
* **Behavior:** Every clock cycle, the intensity of a stored state decreases by a fixed Entropy Factor (e.g., -5%).
* **Result:** Signals that are not reinforced fade to zero, preventing "Ghost Data" from polluting the swarm.

## 5.0 Implementation Profiles
Implementers should adhere to the profile matching their use case:

### Profile A: The "Agent" Profile (Robotics & IoT)
* **Use Case:** Active agents (Nanobots, Drones, Smart Homes).
* **Requirements:** MUST implement **Layer 1**, **Layer 2**, and **Layer 3**.
* **Goal:** Survival, reflex speed, and autonomous coordination.

### Profile B: The "Analyst" Profile (Linguistics & Data)
* **Use Case:** Static analysis (Whale CETI, Database Search).
* **Requirements:** MUST implement **Layer 2 (Vectors)** only.
* **Exclusions:** Ignore Priority and Decay rules to preserve raw data ambiguity.
* **Goal:** Capturing semantic nuance and "fuzzy" logic.
