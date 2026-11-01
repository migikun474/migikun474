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
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=migikun474&show_icons=true&bg_color=172036&title_color=f0b84f&text_color=edf0f7&icon_color=57d3bd&border_color=2e3d60&ring_color=f0b84f&include_all_commits=true" alt="GitHub stats"/>
</p>
<p align="center">
  <img src="https://streak-stats.demolab.com?user=migikun474&background=172036&border=2e3d60&stroke=2e3d60&ring=f0b84f&fire=f0b84f&currStreakNum=edf0f7&sideNums=edf0f7&currStreakLabel=f0b84f&sideLabels=8e9bbb&dates=8e9bbb" alt="GitHub streak"/>
</p>
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=migikun474&layout=compact&langs_count=10&bg_color=172036&title_color=f0b84f&text_color=edf0f7&icon_color=57d3bd&border_color=2e3d60&ring_color=f0b84f&hide=jupyter%20notebook,html,css&exclude_repo=qpp" alt="Most used languages"/>
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
  <a href="https://github.com/migikun474"><img src="https://img.shields.io/badge/GitHub-migikun474-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=github" alt="GitHub"/></a>
  <a href="https://gitlab.com/migikun474"><img src="https://img.shields.io/badge/GitLab-migikun474-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=gitlab" alt="GitLab"/></a>
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
  <img src="https://img.shields.io/badge/C++-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=cplusplus" alt="C++"/>
  <img src="https://img.shields.io/badge/C-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=c" alt="C"/>
  <img src="https://img.shields.io/badge/x86--64%20Assembly-1e2a45?style=for-the-badge" alt="x86-64 Assembly"/>
  <img src="https://img.shields.io/badge/MIPS-1e2a45?style=for-the-badge" alt="MIPS"/>
  <img src="https://img.shields.io/badge/Python-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/TypeScript-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=typescript" alt="TypeScript"/>
  <img src="https://img.shields.io/badge/R-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=r" alt="R"/>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/SIMD%20(SSE%2FAVX2)-1e2a45?style=for-the-badge" alt="SIMD"/>
  <img src="https://img.shields.io/badge/Flex%20%2F%20Bison-1e2a45?style=for-the-badge" alt="Flex and Bison"/>
  <img src="https://img.shields.io/badge/POSIX%20Threads-1e2a45?style=for-the-badge" alt="POSIX threads"/>
  <img src="https://img.shields.io/badge/CMake-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=cmake" alt="CMake"/>
  <img src="https://img.shields.io/badge/Make-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=gnu" alt="Make"/>
  <img src="https://img.shields.io/badge/Linux-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=linux" alt="Linux"/>
  <img src="https://img.shields.io/badge/GitHub%20Actions-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=githubactions" alt="GitHub Actions"/>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Qiskit-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=qiskit" alt="Qiskit"/>
  <img src="https://img.shields.io/badge/NumPy-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=numpy" alt="NumPy"/>
  <img src="https://img.shields.io/badge/SciPy-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=scipy" alt="SciPy"/>
  <img src="https://img.shields.io/badge/Numba-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=numba" alt="Numba"/>
  <img src="https://img.shields.io/badge/pandas-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=pandas" alt="pandas"/>
  <img src="https://img.shields.io/badge/scikit--learn-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=scikitlearn" alt="scikit-learn"/>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=fastapi" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/React-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=react" alt="React"/>
  <img src="https://img.shields.io/badge/Git-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=git" alt="Git"/>
  <img src="https://img.shields.io/badge/GitLab-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=gitlab" alt="GitLab"/>
  <img src="https://img.shields.io/badge/Jupyter-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=jupyter" alt="Jupyter"/>
</p>

---

---

## 📫 Contact

<p align="center">💡 Open to collaborating on systems, compilers, low-latency and quantum-computing projects.</p>

<!-- Fill in and uncomment to show contact links:
<p align="center">
  <a href="https://www.linkedin.com/in/YOUR-HANDLE/"><img src="https://img.shields.io/badge/LinkedIn-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=linkedin" alt="LinkedIn"/></a>
  <a href="mailto:YOUR-EMAIL"><img src="https://img.shields.io/badge/Email-1e2a45?style=for-the-badge&logoColor=f0b84f&logo=gmail" alt="Email"/></a>
</p>
-->
