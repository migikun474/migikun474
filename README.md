<div align="center">
  <h1>Hi, I'm Sai Vignesh 👋</h1>
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=FE428E&width=680&center=true&lines=Systems+%7C+Compilers+%7C+Low-Latency+C;C-like+source+%E2%86%92+TAC+%E2%86%92+MIPS+on+SPIM;SWAR+%7C+SSE%2FAVX2+%7C+x86-64+Assembly;Quantum+Simulation+%7C+Qiskit+%7C+Quantum%2B%2B;Student+at+IIT+Roorkee+%7C+India" alt="Typing SVG"/>
</div>

- 🛠️ Wrote a **compiler for a C-like language** that runs end to end: Flex/Bison front end, Three Address Code with an optimizer (`-O1` to `-O3`), and MIPS code that runs on SPIM.
- ⚡ Measuring things at the nanosecond level: **fastparse** (SIMD parsers for market data) and **fasttime** (why your `clock_gettime` might secretly be a system call).
- ⚛️ Quantum computing: QAOA for peptide design (Qiskit Fall Fest 2026), a quantum–classical crossover study for α-RuCl₃, and contributions to **Quantum++**.
- 🧮 Merged fix in **Eigen**, the C++ linear algebra library, on GitLab.
- 🧵 I like problems close to the machine: parsers, schedulers, threads, clocks, CPU counters.

---

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=migikun474&show_icons=true&theme=radical&include_all_commits=true" alt="GitHub stats"/>
</p>
<p align="center">
  <img src="https://streak-stats.demolab.com?user=migikun474&theme=radical" alt="GitHub streak"/>
</p>
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=migikun474&layout=compact&langs_count=10&theme=radical&hide=jupyter%20notebook,html,css&exclude_repo=qpp" alt="Most used languages"/>
</p>

---

## 🚀 Featured projects

| Project | What it is | Stack |
|---|---|---|
| [**COMPILER-DESIGN**](https://github.com/migikun474/COMPILER-DESIGN) | Compiler for a C-like language with classes, references and overloading. Lexer, LALR(1) parser, semantic analysis, TAC with an interpreter, `-O1`/`-O2`/`-O3` optimizations and register-allocated MIPS. Every test program must print exactly what gcc's binary prints, in the TAC interpreter and in SPIM. | C++17, Flex, Bison, MIPS |
| [**fastparse**](https://github.com/migikun474/fastparse) | Turns market-data text like `"27431.55"` into fixed-point integers, written five ways: naive loop, SWAR, hand-written x86-64 assembly, SSE and AVX2. Up to 5.3 GB/s on a Binance trades CSV against a 973 MB/s reference. Each version is checked against the reference on every PR, with fuzzing and sanitizers in CI. | C, x86-64 asm, SSE/AVX2 |
| [**fasttime**](https://github.com/migikun474/fasttime) | Checks whether a Linux machine's time reads are secretly system calls, benchmarks every way to read the time (vDSO, syscall, `rdtsc`, `rdtscp`), and ships a header-only calibrated TSC clock: 16 ns per read on any clocksource. | C, Linux |
| [**Q-peptide**](https://github.com/migikun474/Q-peptide) | Picks the amino-acid substitutions that best trade off predicted activity against hemolysis: QUBO → Ising → QAOA, benchmarked against classical solvers, with noise and error-mitigation studies. Qiskit Fall Fest 2026. | Qiskit, scikit-learn, FastAPI, React |
| [**rucl3-crossover**](https://github.com/migikun474/rucl3-crossover) | Research code, in progress: when will a quantum computer beat classical simulation of the neutron spectrum of the magnet α-RuCl₃? Costs S(q, ω) both ways at the same accuracy: exact Lanczos/Krylov against Trotter circuits with fault-tolerant resource estimates. | Python, NumPy, Numba, QDK |
| [**T20 World Cup Simulator**](https://github.com/migikun474/multithreaded-t20-worldcup-simulator) | A cricket match where every player is a POSIX thread, with FCFS/SJF/priority scheduling and Banker's Algorithm deadlock detection. | C++17, pthreads |

## 🌐 Open source

- [**Eigen**](https://gitlab.com/libeigen/eigen) (C++ linear algebra library, on GitLab): [!3412 — merged](https://gitlab.com/libeigen/eigen/-/merge_requests/3412). Building an `Affine` or `Isometry` transform from a full matrix now resets the last row to `[0 … 0 1]`, so the transform can no longer silently break its own mode.
- [**Quantum++**](https://github.com/migikun474/qpp) (C++17 quantum computing library by softwareQ): added `qpp::fidelity()`, `qpp::trace_distance()`, `qpp::purity()` and arbitrary state preparation with `qpp::state_prep_circuit()`.

<p align="center">
  <a href="https://github.com/migikun474"><img src="https://img.shields.io/badge/GitHub-migikun474-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
  <a href="https://gitlab.com/migikun474"><img src="https://img.shields.io/badge/GitLab-migikun474-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white" alt="GitLab"/></a>
</p>

<details>
<summary>More projects</summary>

- [OptiTrace](https://github.com/migikun474/OptiTrace) — compiler plugin and runtime for finding hot code paths and comparing Clang and GCC optimization passes.
- [Yield Curve Prediction (CIR)](https://github.com/migikun474/-Yield-Curve-Prediction-using-CIR-method) — predicts the 6M–30Y yield curve from the 3-month rate; the jump-diffusion CIR model reaches R² = 0.94 out of sample.
- [VITERBI](https://github.com/migikun474/VITERBI) — Viterbi decoding of a hidden Markov model for exon / splice site / intron structure in DNA.
- [PCA_GENE_EXPRESSION](https://github.com/migikun474/PCA_GENE_EXPRESSION) — PCA from scratch in NumPy, separating ER+ and ER− breast-cancer samples.
- [GO-ENRICHMENT](https://github.com/migikun474/GO-ENRICHMENT) — strand-aware promoter regions upstream of human TSSs with bedtools.
- [Gene2Protein](https://github.com/migikun474/Gene2Protein) — CYP2E1 transcripts, proteins and protein-to-genome mapping in R.

</details>

---

## 🛠️ Skills

<p align="center">
  <img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++"/>
  <img src="https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black" alt="C"/>
  <img src="https://img.shields.io/badge/x86--64%20Assembly-6E4C13?style=for-the-badge" alt="x86-64 Assembly"/>
  <img src="https://img.shields.io/badge/MIPS-4B5563?style=for-the-badge" alt="MIPS"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript"/>
  <img src="https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white" alt="R"/>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/SIMD%20(SSE%2FAVX2)-4B5563?style=for-the-badge" alt="SIMD"/>
  <img src="https://img.shields.io/badge/Flex%20%2F%20Bison-4B5563?style=for-the-badge" alt="Flex and Bison"/>
  <img src="https://img.shields.io/badge/POSIX%20Threads-4B5563?style=for-the-badge" alt="POSIX threads"/>
  <img src="https://img.shields.io/badge/CMake-064F8C?style=for-the-badge&logo=cmake&logoColor=white" alt="CMake"/>
  <img src="https://img.shields.io/badge/Make-427819?style=for-the-badge&logo=gnu&logoColor=white" alt="Make"/>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux"/>
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions"/>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Qiskit-6929C4?style=for-the-badge&logo=qiskit&logoColor=white" alt="Qiskit"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white" alt="SciPy"/>
  <img src="https://img.shields.io/badge/Numba-00A3E0?style=for-the-badge&logo=numba&logoColor=white" alt="Numba"/>
  <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn"/>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
  <img src="https://img.shields.io/badge/GitLab-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white" alt="GitLab"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter"/>
</p>

---

## 📫 Contact

<p align="center">💡 Open to collaborating on systems, compilers, low-latency and quantum-computing projects.</p>

<!-- Fill in and uncomment to show contact links:
<p align="center">
  <a href="https://www.linkedin.com/in/YOUR-HANDLE/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:YOUR-EMAIL"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
</p>
-->
