<!-- GitHub profile README: musha1140/musha1140 -->

<p align="center">
  <a href="https://gas-lighting.com"><img alt="gas-lighting" src="https://img.shields.io/badge/gas--lighting-111?style=for-the-badge&amp;logo=simpleicons&amp;logoColor=white"></a>
</p>

<h1 align="center">musha1140</h1>

<p align="center"><strong>Founder — Gas-Lighting LLC / GSL Productions</strong><br>CTO / DPO — Chicago Infectious Disease Physicians, Inc.</p>

<p align="center">Website &amp; infrastructure design · AI simulation · Data pipelines<br>Cryptography &amp; steganography · Optimization · MIDI experiments</p>

<!-- Substrate animation is a separate image; existing embeds stay below. -->
<p align="center">
  <img src="assets/samsara-substrate.gif" alt="Samsara Substrate — animated lattice using sigil-state parameters" width="720">
</p>

<p align="center">
  <a href="https://gist.githubusercontent.com/musha1140/c7a5de6d11c7cfa565c688f551225a91/raw/74449d8aeb76bd3b886634e9cd7fa12b686742d7/sigil-state.json"><img alt="Substrate voices" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgist.githubusercontent.com%2Fmusha1140%2Fc7a5de6d11c7cfa565c688f551225a91%2Fraw%2F74449d8aeb76bd3b886634e9cd7fa12b686742d7%2Fsigil-state.json&amp;query=%24.substrate.parameters.voices&amp;label=voices&amp;logo=tailscale&amp;logoColor=020604&amp;color=d1fae5&amp;style=for-the-badge"></a>
</p>

<p align="left">
  <a href="https://v0gsl.vercel.app"><img alt="Live Hub" src="https://img.shields.io/badge/LIVE-v0gsl.vercel.app-111?style=for-the-badge"></a>
  <a href="https://gsl-wiki.vercel.app"><img alt="Docs" src="https://img.shields.io/badge/DOCS-gsl--wiki-111?style=for-the-badge"></a>
  <a href="https://gsl-kappa.vercel.app"><img alt="MIDI demo" src="https://img.shields.io/badge/DEMO-gsl--kappa-111?style=for-the-badge"></a>
  <a href="https://slayy1.vercel.app"><img alt="Slayy1 demo" src="https://img.shields.io/badge/DEMO-slayy1-111?style=for-the-badge"></a>
</p>

<p align="center"><a href="#live-surfaces">Live surfaces</a> &nbsp; / &nbsp; <a href="#case-studies">Case studies</a> &nbsp; / &nbsp; <a href="#project-catalogue">Projects</a> &nbsp; / &nbsp; <a href="#stack">Stack</a> &nbsp; / &nbsp; <a href="#architecture">Architecture</a></p>

---

## Live surfaces

These are the public entry points that connect everything:

- **GSL Platform Hub (Store + project router):** [Open](https://v0gsl.vercel.app)
- **GSL Wiki (docs + diagrams):** [Open](https://gsl-wiki.vercel.app)
- **MIDI Grid Crypto (Kappa):** [Open](https://gsl-kappa.vercel.app)
- **.slayy Decoder (Slayy1):** [Open](https://slayy1.vercel.app)

---

## Case studies

### 1) Forced Check — Chess negotiation

**What it is:**\
A chess training + sim pipeline that treats negotiation as adversarial play:\
**intentionally sink perceived win-probability, constrain opponent agency, then reverse under constraint.**

The objective layers behavioral constraints onto evaluation and search.

#### Model loop

- Entity state = personality traits + strategy mode
  - aggression
  - deception
  - risk_tolerance
  - adaptability
- Per step: traits → strategy → move selection → evaluation → learning update → introspection + structured summary.

#### Training target

- Drive the game into a position where you *look* worse, but the position is still structurally controllable.
- Keep sinking the probability to the lowest acceptable valley.
- Flip the outcome under a fixed budget (plies/time) once control is established.

#### Companion explainer:

- [Open](https://chatgpt.com/g/g-LnlKe3fmW-hal-9000)
- Stockfish evaluation run on a Paperspace GPU.

<p align="left">
  <a href="szyrgy.png">
    <img src="szyrgy.png" alt="Forced Check training trace" width="200">
  </a>
</p>

Metrics: win rate over episodes, minimum win probability before reversal, and ablations across traits, strategy modes, and engine configurations.

#### Tooling

- Stockfish used for evaluation grounding / calibration in the training harness.
- Comparative configurations used to validate stability of measured outcomes (win-rate, reversal frequency).

---

### 2) SSID Clustering — Aggregate Density → Regional Regimes → Macro Correlation

**What it is:**\
A data pipeline that clusters **aggregate Wi-Fi SSID density** into region-level “activity regimes,” then correlates regime shifts with macro indicators (market behavior, logistics pressure, policy events).

#### Pipeline (high level)

1. Aggregate SSID metadata ingestion (public/consented sources)
2. Feature extraction:
   - density
   - churn
   - temporal shifts
   - category heuristics
3. Clustering:
   - K-Means + elbow
   - stability checks
4. Output:
   - regime labels used as scenario-model inputs

---

### 3) MIDI / Entropy / Steganography — `.slayy` container workflows

**What it is:**\
Tooling that converts structured inputs (MIDI patterns + interaction timing) into entropy, then uses that entropy in encryption + lossless embedding workflows.

Public demos:

- MIDI Grid Crypto: [Open](https://gsl-kappa.vercel.app)
- .slayy Decoder: [Open](https://slayy1.vercel.app)

Related repos/components:

- [GS](https://github.com/musha1140/GS)
- [JSEntropy](https://github.com/musha1140/JSEntropy)
- [steganographr](https://github.com/musha1140/steganographr) (fork)
- [rainbowtables](https://github.com/musha1140/rainbowtables) (fork)

---

## Project catalogue

<sup>Click a category header to toggle details.</sup>

<details>
<summary><strong>A · AI & Simulation</strong></summary>

| Name                     | Repo / Live                                                                                                           | Purpose                                                          | Tech Highlights                         |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------- |
| **GPT Vibe Engine**      | [v0-gpt-vibe-engine](https://github.com/musha1140/v0-gpt-vibe-engine) · [Open](https://v0-gpt-vibe-engine.vercel.app) | Real-time 3D visualization of token dynamics                     | Three.js/React, shaders, WebGL          |
| **Forced Check**         | [Chess-Force-Negatekeep](https://github.com/musha1140/Chess-Force-Negatekeep)                                         | Chess negotiation training and “min-then-max” reversal objective | Search + evaluation harness, trait loop |
| **TwitchMod**            | [UrbanDictionary](https://github.com/musha1140/UrbanDictionary) · [Open](https://urbandictionary.replit.app)          | Chaotic chat simulator for moderator drills                      | Node, WebSockets, event flows           |
| **vLLM Fork**            | [vllm](https://github.com/musha1140/vllm)                                                                             | High-throughput LLM serving experiments                          | CUDA-aware Triton, Python ext           |
| **Macrodata Refinement** | [Macrodata-Refinement](https://github.com/musha1140/Macrodata-Refinement)                                             | Narrative clustering prototype                                   | NLP + graph visualization               |

</details>

<details>
<summary><strong>B · Encryption & Steganography</strong></summary>

| Name                            | Repo / Live                                                                  | Key Idea                                    | Stack                          |
| ------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------- | ------------------------------ |
| **MIDI Grid Encryption Engine** | [GS](https://github.com/musha1140/GS) · [Open](https://gsl-kappa.vercel.app) | MIDI density → entropy → grid-mapped cipher | Tone.js, WebCrypto, XOR layers |
| **Slayy1**                      | [Open](https://slayy1.vercel.app)                                            | Auto-decodes `.slayy` LSB images            | React, Canvas                  |
| **JSEntropy**                   | [JSEntropy](https://github.com/musha1140/JSEntropy)                          | JS scrambler + bit-shift cipher             | Python build chain             |
| **steganographr**               | [steganographr](https://github.com/musha1140/steganographr)                  | Zero-width Unicode text hider               | PHP, Go                        |
| **rainbowtables**               | [rainbowtables](https://github.com/musha1140/rainbowtables)                  | Precomputed hash tables (research/learning) | Python multiprocessing         |
| **SecureSavingDataDock**        | private                                                                      | Milestone-locked savings contract emulator  | Python, Solidity-like DSL      |

</details>

<details>
<summary><strong>C · Networking & Learning Tools</strong></summary>

| Name                                | Repo / Live                                                                    | Function                    | Stack                             |
| ----------------------------------- | ------------------------------------------------------------------------------ | --------------------------- | --------------------------------- |
| **CCNA Guidebook**                  | [ccna](https://github.com/musha1140/ccna) · [Open](https://ccnagsl.vercel.app) | Scored quizzes + diagrams   | Next.js, D3                       |
| **Comparative Death-Toll Analysis** | [Open](https://cn-c.replit.app)                                                | Timeline visualization      | Vue 3, CSV ETL                    |
| **Housing Fee Dashboard**           | [Open](https://statictail.vercel.app)                                          | Policy modeling charts      | Gatsby, Chart.js                  |
| **Adaptive Learning Voice Cache**   | private / pasted                                                               | Caches ElevenLabs responses | Streamlit, Snowflake, OpenAI APIs |

</details>

<details>
<summary><strong>D · Business Ops & Data Pipelines</strong></summary>

| Name                                | Repo / Live                         | Solves                                      | Stack                       |
| ----------------------------------- | ----------------------------------- | ------------------------------------------- | --------------------------- |
| **GSL Consignment / Store Surface** | [Open](https://v0gsl.vercel.app)    | Product surface + routing                   | Next/React, docs + demos    |
| **SecureInvestDD**                  | private                             | Secure investment simulation + DD datastore | Streamlit, Pandas, Postgres |
| **gsl-wiki**                        | [Open](https://gsl-wiki.vercel.app) | Living docs & diagrams                      | Docusaurus, Mermaid         |
| **Investment Simulator**            | local/private                       | Scenario sweeps                             | Python, Matplotlib          |

</details>

<details>
<summary><strong>E · System Utilities & Game Frameworks</strong></summary>

| Name                            | Repo                                                                                                            | Scope                        | Notes                   |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------- | ----------------------- |
| **Keychron-Corsair HID Bridge** | [MacOS-Windows-with-Keychron-and-Corsair](https://github.com/musha1140/MacOS-Windows-with-Keychron-and-Corsair) | One-touch KBM swap across OS | Shell, udev, PowerShell |
| **FiveM Framework Forks**       | profile forks                                                                                                   | Custom RP patches            | TypeScript, Lua         |
| **GPU Swap / System Scripts**   | private                                                                                                         | DDU cleanup + BIOS checks    | Batch, PowerShell       |

</details>

---

## Stack

### Core

<p align="center">
  <img alt="Tailscale" src="https://img.shields.io/badge/Tailscale-111111?style=for-the-badge&amp;logo=tailscale&amp;logoColor=a7f3d0">
  <img alt="AWS" src="https://img.shields.io/badge/AWS-111111?style=for-the-badge&amp;logo=amazonaws&amp;logoColor=a7f3d0">
  <img alt="Cloudflare" src="https://img.shields.io/badge/Cloudflare-111111?style=for-the-badge&amp;logo=cloudflare&amp;logoColor=a7f3d0">
  <img alt="Python" src="https://img.shields.io/badge/Python-111111?style=for-the-badge&amp;logo=python&amp;logoColor=a7f3d0">
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-111111?style=for-the-badge&amp;logo=typescript&amp;logoColor=a7f3d0">
</p>

<p align="center">
  <img alt="Node.js" src="https://img.shields.io/badge/Node.js-111111?style=for-the-badge&amp;logo=nodedotjs&amp;logoColor=a7f3d0">
  <img alt="Kotlin" src="https://img.shields.io/badge/Kotlin-111111?style=for-the-badge&amp;logo=kotlin&amp;logoColor=a7f3d0">
</p>

### Web & interfaces

<p align="center">
  <a href="https://github.com/musha1140/GS"><img alt="HTML" src="https://img.shields.io/badge/HTML-111111?style=for-the-badge&amp;logo=html5&amp;logoColor=a7f3d0"></a>
  <a href="https://github.com/musha1140/GS"><img alt="CSS" src="https://img.shields.io/badge/CSS-111111?style=for-the-badge&amp;logo=css3&amp;logoColor=a7f3d0"></a>
  <a href="https://github.com/musha1140/GS"><img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-111111?style=for-the-badge&amp;logo=javascript&amp;logoColor=a7f3d0"></a>
  <img alt="Tailwind" src="https://img.shields.io/badge/Tailwind-111111?style=for-the-badge&amp;logo=tailwindcss&amp;logoColor=a7f3d0">
  <img alt="PostCSS" src="https://img.shields.io/badge/PostCSS-111111?style=for-the-badge&amp;logo=postcss&amp;logoColor=a7f3d0">
</p>

<p align="center">
  <img alt="React" src="https://img.shields.io/badge/React-111111?style=for-the-badge&amp;logo=react&amp;logoColor=a7f3d0">
  <img alt="Next.js" src="https://img.shields.io/badge/Next.js-111111?style=for-the-badge&amp;logo=nextdotjs&amp;logoColor=a7f3d0">
  <img alt="Astro" src="https://img.shields.io/badge/Astro-111111?style=for-the-badge&amp;logo=astro&amp;logoColor=a7f3d0">
  <img alt="Vue" src="https://img.shields.io/badge/Vue-111111?style=for-the-badge&amp;logo=vuedotjs&amp;logoColor=a7f3d0">
  <a href="https://ionic-react-ebon.vercel.app"><img alt="Ionic" src="https://img.shields.io/badge/Ionic-111111?style=for-the-badge&amp;logo=ionic&amp;logoColor=a7f3d0"></a>
</p>

<p align="center">
  <img alt="three.js" src="https://img.shields.io/badge/three.js-111111?style=for-the-badge&amp;logo=threedotjs&amp;logoColor=a7f3d0">
  <img alt="Canvas" src="https://img.shields.io/badge/Canvas-111111?style=for-the-badge&amp;logoColor=a7f3d0">
</p>

### Systems, crypto & audio

<p align="center">
  <img alt="Swift" src="https://img.shields.io/badge/Swift-111111?style=for-the-badge&amp;logo=swift&amp;logoColor=a7f3d0">
  <img alt="Lua" src="https://img.shields.io/badge/Lua-111111?style=for-the-badge&amp;logo=lua&amp;logoColor=a7f3d0">
  <img alt="Go" src="https://img.shields.io/badge/Go-111111?style=for-the-badge&amp;logo=go&amp;logoColor=a7f3d0">
  <img alt="LLVM backend" src="https://img.shields.io/badge/LLVM%20backend-111111?style=for-the-badge&amp;logo=llvm&amp;logoColor=a7f3d0">
  <img alt="C++" src="https://img.shields.io/badge/C%2B%2B-111111?style=for-the-badge&amp;logo=cplusplus&amp;logoColor=a7f3d0">
</p>

<p align="center">
  <img alt="C" src="https://img.shields.io/badge/C-111111?style=for-the-badge&amp;logo=c&amp;logoColor=a7f3d0">
  <img alt="Assembly" src="https://img.shields.io/badge/Assembly-111111?style=for-the-badge&amp;logoColor=a7f3d0">
  <img alt="Solidity" src="https://img.shields.io/badge/Solidity-111111?style=for-the-badge&amp;logo=solidity&amp;logoColor=a7f3d0">
  <img alt="Tone.js" src="https://img.shields.io/badge/Tone.js-111111?style=for-the-badge&amp;logoColor=a7f3d0">
  <img alt="AES-GCM" src="https://img.shields.io/badge/AES--GCM-111111?style=for-the-badge&amp;logoColor=a7f3d0">
</p>

<p align="center">
  <img alt="WebCrypto" src="https://img.shields.io/badge/WebCrypto-111111?style=for-the-badge&amp;logoColor=a7f3d0">
  <img alt="Brainfuck" src="https://img.shields.io/badge/Brainfuck-111111?style=for-the-badge&amp;logoColor=a7f3d0">
  <img alt="Morse" src="https://img.shields.io/badge/Morse-111111?style=for-the-badge&amp;logoColor=a7f3d0">
</p>

### Cloud, data & identity

<p align="center">
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-111111?style=for-the-badge&amp;logo=postgresql&amp;logoColor=a7f3d0">
  <img alt="Redis" src="https://img.shields.io/badge/Redis-111111?style=for-the-badge&amp;logo=redis&amp;logoColor=a7f3d0">
  <a href="https://github.com/musha1140/StratVest"><img alt="Docker" src="https://img.shields.io/badge/Docker-111111?style=for-the-badge&amp;logo=docker&amp;logoColor=a7f3d0"></a>
  <a href="https://mdtgf.vercel.app"><img alt="Vercel" src="https://img.shields.io/badge/Vercel-111111?style=for-the-badge&amp;logo=vercel&amp;logoColor=a7f3d0"></a>
  <img alt="Netlify" src="https://img.shields.io/badge/Netlify-111111?style=for-the-badge&amp;logo=netlify&amp;logoColor=a7f3d0">
</p>

<p align="center">
  <img alt="AWS Lambda" src="https://img.shields.io/badge/AWS_Lambda-111111?style=for-the-badge&amp;logo=awslambda&amp;logoColor=a7f3d0">
  <img alt="Paperspace" src="https://img.shields.io/badge/Paperspace-111111?style=for-the-badge&amp;logo=paperspace&amp;logoColor=a7f3d0">
  <img alt="Sanity" src="https://img.shields.io/badge/Sanity-111111?style=for-the-badge&amp;logo=sanity&amp;logoColor=a7f3d0">
  <img alt="Keystatic" src="https://img.shields.io/badge/Keystatic-111111?style=for-the-badge&amp;logo=keystatic&amp;logoColor=a7f3d0">
  <a href="https://musha1140.github.io/"><img alt="GitHub Pages" src="https://img.shields.io/badge/GitHub%20Pages-111111?style=for-the-badge&amp;logo=github&amp;logoColor=a7f3d0"></a>
</p>

<p align="center">
  <a href="https://github.com/musha1140"><img alt="Git · GitHub" src="https://img.shields.io/badge/Git%20%C2%B7%20GitHub-111111?style=for-the-badge&amp;logo=git&amp;logoColor=a7f3d0"></a>
  <img alt="Microsoft Entra" src="https://img.shields.io/badge/Microsoft_Entra-111111?style=for-the-badge&amp;logo=microsoft&amp;logoColor=a7f3d0">
  <img alt="Microsoft 365" src="https://img.shields.io/badge/Microsoft_365-111111?style=for-the-badge&amp;logo=microsoft365&amp;logoColor=a7f3d0">
  <img alt="Google SSO" src="https://img.shields.io/badge/Google_SSO-111111?style=for-the-badge&amp;logo=google&amp;logoColor=a7f3d0">
  <img alt="Microsoft Orleans" src="https://img.shields.io/badge/Microsoft_Orleans-111111?style=for-the-badge&amp;logo=dotnet&amp;logoColor=a7f3d0">
</p>

<p align="center">
  <img alt="Google Cloud" src="https://img.shields.io/badge/Google_Cloud-111111?style=for-the-badge&amp;logo=googlecloud&amp;logoColor=a7f3d0">
  <img alt="Bigtable" src="https://img.shields.io/badge/Bigtable-111111?style=for-the-badge&amp;logo=googlecloud&amp;logoColor=a7f3d0">
  <img alt="Porkbun" src="https://img.shields.io/badge/Porkbun-111111?style=for-the-badge&amp;logoColor=a7f3d0">
  <img alt="GoDaddy" src="https://img.shields.io/badge/GoDaddy-111111?style=for-the-badge&amp;logo=godaddy&amp;logoColor=a7f3d0">
</p>

### Hardware, builds & tooling

<p align="center">
  <img alt="Raspberry Pi" src="https://img.shields.io/badge/Raspberry_Pi-111111?style=for-the-badge&amp;logo=raspberrypi&amp;logoColor=a7f3d0">
  <img alt="LineageOS" src="https://img.shields.io/badge/LineageOS-111111?style=for-the-badge&amp;logo=lineageos&amp;logoColor=a7f3d0">
  <img alt="CentOS" src="https://img.shields.io/badge/CentOS-111111?style=for-the-badge&amp;logo=centos&amp;logoColor=a7f3d0">
  <img alt="WSL" src="https://img.shields.io/badge/WSL-111111?style=for-the-badge&amp;logo=linux&amp;logoColor=a7f3d0">
  <img alt="GSL-mdtgf" src="https://img.shields.io/badge/GSL--mdtgf-111111?style=for-the-badge&amp;logo=linux&amp;logoColor=a7f3d0">
</p>

<p align="center">
  <img alt="Bazel" src="https://img.shields.io/badge/Bazel-111111?style=for-the-badge&amp;logo=bazel&amp;logoColor=a7f3d0">
  <img alt="BuildBuddy" src="https://img.shields.io/badge/BuildBuddy-111111?style=for-the-badge&amp;logoColor=a7f3d0">
  <img alt="Redstone" src="https://img.shields.io/badge/Redstone-111111?style=for-the-badge&amp;logo=minecraft&amp;logoColor=a7f3d0">
  <img alt="Shell" src="https://img.shields.io/badge/Shell-111111?style=for-the-badge&amp;logo=gnubash&amp;logoColor=a7f3d0">
  <img alt="PowerShell" src="https://img.shields.io/badge/PowerShell-111111?style=for-the-badge&amp;logo=powershell&amp;logoColor=a7f3d0">
</p>

<p align="center">
  <img alt="Nix" src="https://img.shields.io/badge/Nix-111111?style=for-the-badge&amp;logo=nixos&amp;logoColor=a7f3d0">
  <img alt="Playwright" src="https://img.shields.io/badge/Playwright-111111?style=for-the-badge&amp;logo=playwright&amp;logoColor=a7f3d0">
  <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-111111?style=for-the-badge&amp;logo=jupyter&amp;logoColor=a7f3d0">
  <img alt="Sublime Text" src="https://img.shields.io/badge/Sublime_Text-111111?style=for-the-badge&amp;logo=sublimetext&amp;logoColor=a7f3d0">
  <img alt="JSFiddle" src="https://img.shields.io/badge/JSFiddle-111111?style=for-the-badge&amp;logo=jsfiddle&amp;logoColor=a7f3d0">
</p>

<p align="center">
  <img alt="Stockfish" src="https://img.shields.io/badge/Stockfish-111111?style=for-the-badge&amp;logoColor=a7f3d0">
  <img alt="Notion" src="https://img.shields.io/badge/Notion-111111?style=for-the-badge&amp;logo=notion&amp;logoColor=a7f3d0">
  <img alt="Discord bots" src="https://img.shields.io/badge/Discord%20bots-111111?style=for-the-badge&amp;logo=discord&amp;logoColor=a7f3d0">
</p>

### Experimental

<p align="center">
  <img alt="nanowiz" src="https://img.shields.io/badge/nanowiz-064e3b?style=for-the-badge&amp;logoColor=a7f3d0">
  <img alt="via" src="https://img.shields.io/badge/via-064e3b?style=for-the-badge&amp;logoColor=a7f3d0">
  <img alt="rerun" src="https://img.shields.io/badge/rerun-064e3b?style=for-the-badge&amp;logoColor=a7f3d0">
  <img alt="self" src="https://img.shields.io/badge/self-064e3b?style=for-the-badge&amp;logoColor=a7f3d0">
  <img alt="rsi" src="https://img.shields.io/badge/rsi-064e3b?style=for-the-badge&amp;logoColor=a7f3d0">
</p>

<p align="center">
  <a href="https://github.com/musha1140/JSEntropy"><img alt="Antigravity" src="https://img.shields.io/badge/Antigravity-064e3b?style=for-the-badge&amp;logo=python&amp;logoColor=a7f3d0"></a>
</p>

### AI models & ecosystem

<p align="center">
  <img alt="Claude: Mythos" src="https://img.shields.io/badge/Claude%3A_Mythos-064e3b?style=for-the-badge&amp;logo=anthropic&amp;logoColor=a7f3d0">
  <img alt="Claude: Opus" src="https://img.shields.io/badge/Claude%3A_Opus-064e3b?style=for-the-badge&amp;logo=anthropic&amp;logoColor=a7f3d0">
  <img alt="Claude: Fable" src="https://img.shields.io/badge/Claude%3A_Fable-064e3b?style=for-the-badge&amp;logo=anthropic&amp;logoColor=a7f3d0">
  <img alt="Claude Code CLI" src="https://img.shields.io/badge/Claude_Code_CLI-064e3b?style=for-the-badge&amp;logo=anthropic&amp;logoColor=a7f3d0">
  <img alt="OpenAI - DaVinci" src="https://img.shields.io/badge/OpenAI--DaVinci-064e3b?style=for-the-badge&amp;logo=openai&amp;logoColor=a7f3d0">
</p>

<p align="center">
  <img alt="OpenAI Codex" src="https://img.shields.io/badge/OpenAI_Codex-064e3b?style=for-the-badge&amp;logo=openai&amp;logoColor=a7f3d0">
  <img alt="Gemini" src="https://img.shields.io/badge/Gemini-064e3b?style=for-the-badge&amp;logo=googlegemini&amp;logoColor=a7f3d0">
  <img alt="Perplexity" src="https://img.shields.io/badge/Perplexity-064e3b?style=for-the-badge&amp;logo=perplexity&amp;logoColor=a7f3d0">
  <img alt="Nemotron" src="https://img.shields.io/badge/Nemotron-064e3b?style=for-the-badge&amp;logo=nvidia&amp;logoColor=a7f3d0">
  <img alt="Kimi" src="https://img.shields.io/badge/Kimi-064e3b?style=for-the-badge&amp;logo=moonshotai&amp;logoColor=a7f3d0">
</p>

<p align="center">
  <img alt="Grok" src="https://img.shields.io/badge/Grok-064e3b?style=for-the-badge&amp;logo=x&amp;logoColor=a7f3d0">
  <img alt="Hugging Face" src="https://img.shields.io/badge/Hugging_Face-064e3b?style=for-the-badge&amp;logo=huggingface&amp;logoColor=a7f3d0">
  <img alt="MCP" src="https://img.shields.io/badge/MCP-064e3b?style=for-the-badge&amp;logoColor=a7f3d0">
</p>

---

## Architecture

```mermaid
flowchart TD
  subgraph Edge["Edge / Demos"]
    TwitchMod
    GPTVibe["GPT Vibe Engine"]
    Slayy1
    v0GSL["GSL Hub"]
  end

  subgraph Stores["Stores"]
    Postgres[(PostgreSQL)]
    Redis[(Redis)]
    Snowflake[(Snowflake)]
  end

  subgraph Crypto["Crypto / Stego"]
    XOR_AES["XOR + AES"]
    Stego["LSB (.slayy)"]
  end

  subgraph ML["Modeling"]
    KMeans["SSID K-Means"]
    MCTS["Search / MCTS-style loop"]
  end

  Edge --> Stores
  Stores --> ML
  ML --> Edge
  Edge --> Crypto
  Crypto --> Edge

```
