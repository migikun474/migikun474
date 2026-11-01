<p align="center">
  <img src="assets/hero.svg" width="100%" alt="Sai Vignesh — systems, compilers, low-latency C and quantum computing"/>
</p>

- 🛠️ Wrote a **compiler for a C-like language** that runs end to end: Flex/Bison front end, Three Address Code with an optimizer (`-O1` to `-O3`), and register-allocated MIPS that runs on SPIM.
- ⚡ Measuring things at the nanosecond level: **fastparse** (SIMD parsers for market data) and **fasttime** (why your `clock_gettime` might secretly be a system call).
- ⚛️ Quantum computing: QAOA for peptide design (Qiskit Fall Fest 2026), a quantum–classical crossover study for α-RuCl₃, and contributions to **Quantum++**.
- 🧮 Merged fix in **Eigen**, the C++ linear algebra library, on GitLab.

---

## ⚙️ How my projects work

<a href="https://github.com/migikun474/COMPILER-DESIGN"><img src="assets/compiler.svg" width="100%" alt="Compiler pipeline: source.c → preprocessor → Flex lexer → LALR(1) parser → semantic analysis → TAC → optimizer → MIPS → SPIM"/></a>

<a href="https://github.com/migikun474/fastparse"><img src="assets/fastparse.svg" width="100%" alt="fastparse: SWAR combines 8 digits in 3 multiply-adds; AVX2 reaches 5,311 MB/s against a 973 MB/s reference"/></a>

<a href="https://github.com/migikun474/fasttime"><img src="assets/fasttime.svg" width="100%" alt="fasttime: rdtsc and vDSO reads take 16–20 ns; hpet and acpi_pm reads trap into the kernel and take 1,213–1,966 ns"/></a>

<a href="https://github.com/migikun474/Q-peptide"><img src="assets/quantum.svg" width="100%" alt="Q·Peptide: a p=2 QAOA circuit makes the optimal bitstring 390 times more likely than uniform sampling"/></a>

<a href="https://github.com/migikun474/rucl3-crossover"><img src="assets/rucl3.svg" width="100%" alt="rucl3-crossover: schematic of classical and quantum cost curves crossing at N*"/></a>

<sub>Every animation is hand-written SVG; the numbers come from each repo's own measurements. Click one to open the project.</sub>

---

## 📊 Activity

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=migikun474&show_icons=true&theme=radical&include_all_commits=true" alt="GitHub stats"/>
</p>
<p align="center">
  <img src="https://streak-stats.demolab.com?user=migikun474&theme=radical" alt="GitHub streak"/>
</p>
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=migikun474&layout=compact&langs_count=10&theme=radical&hide=jupyter%20notebook,html,css&exclude_repo=qpp" alt="Most used languages"/>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/migikun474/migikun474/output/snake-dark.svg"/>
    <img src="https://raw.githubusercontent.com/migikun474/migikun474/output/snake-light.svg" alt="Contribution snake"/>
  </picture>
</p>

---

## 🌐 Open source

- [**Eigen**](https://gitlab.com/libeigen/eigen) (C++ linear algebra library, on GitLab): [!3412 — merged](https://gitlab.com/libeigen/eigen/-/merge_requests/3412). Building an `Affine` or `Isometry` transform from a full matrix now resets the last row to `[0 … 0 1]`, so the transform can no longer silently break its own mode.
- [**Quantum++**](https://github.com/migikun474/qpp) (C++17 quantum computing library by softwareQ): added `qpp::fidelity()`, `qpp::trace_distance()`, `qpp::purity()` and arbitrary state preparation with `qpp::state_prep_circuit()`.

<p align="center">
  <a href="https://github.com/migikun474"><img src="https://img.shields.io/badge/GitHub-migikun474-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
  <a href="https://gitlab.com/migikun474"><img src="https://img.shields.io/badge/GitLab-migikun474-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white" alt="GitLab"/></a>
</p>

<details>
<summary>More projects</summary>

- [T20 World Cup Simulator](https://github.com/migikun474/multithreaded-t20-worldcup-simulator) — a cricket match where every player is a POSIX thread, with FCFS/SJF/priority scheduling and Banker's Algorithm deadlock detection.
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

---

## 📫 Contact

<p align="center">💡 Open to collaborating on systems, compilers, low-latency and quantum-computing projects.</p>

<!-- Fill in and uncomment to show contact links:
<p align="center">
  <a href="https://www.linkedin.com/in/YOUR-HANDLE/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:YOUR-EMAIL"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
</p>
-->
