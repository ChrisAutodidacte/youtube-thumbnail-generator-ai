# 🎨 YouTube Thumbnail Generator — Multi-Entity & AI

> 🇫🇷 **Looking for the French version?** See the French repository: [generateur-IA-vignette-youtube](https://github.com/ChrisAutodidacte/generateur-IA-vignette-youtube)

> **Generate professional, high-CTR YouTube thumbnails** using AI (Google Gemini Image Generation) and a local 2-step pipeline, driven directly by a **Claude Code** skill or standalone Python scripts.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Gemini Image API](https://img.shields.io/badge/Gemini-Image_API-orange.svg)](https://aistudio.google.com)
[![Claude Code Ready](https://img.shields.io/badge/Claude_Code-Skill_Ready-purple.svg)](https://docs.anthropic.com)

---

## 💡 Why This Tool?

Most AI image generators fail at YouTube thumbnails for two critical reasons:
1. **Faces are distorted or unrecognizable**: AI generates uncanny human faces or struggles to faithfully reproduce the channel creator's real identity.
2. **Visual branding is unpredictable**: each generation starts from a blank slate with no memory of your color palette, fonts, or composition hierarchy.

### The Solution: A 2-Step Pipeline
1. **AI handles what it does best**: 16:9 composition, atmospheric high-contrast backgrounds, extra-bold readable typography, and thematic 3D/isometric illustrations — while strictly reserving clean negative space for the creator's portrait.
2. **A local Pillow script guarantees creator perfection**: your authentic cutout portrait is composited locally at exact pixel coordinates (circular crop, luminous neon border, subtle outer glow) — zero distortion, zero AI hallucination.

---

## 🧠 Behind the Scenes: How This Project Was Born

This project was born out of a real creator need and an artisan-developer approach, pairing human intuition with AI agents:

### 1. Upstream Research with NotebookLM (Battle-Tested Theory)
Before writing any code, I gathered top research papers, click-through rate (CTR) studies, and visual guidelines from leading YouTube strategists.  
I fed this entire documentation corpus into **NotebookLM** to synthesize actionable rules:
* Contrast psychology and visual hierarchy (the 3-second viewer decision rule).
* Mobile-optimized title constraints (28 characters max for primary titles).
* Safe-zone reservations to avoid YouTube's duration timecode covering crucial visual elements.

NotebookLM produced a **structured operational framework** ready to serve as the system prompt and specification sheet for our AI coding agent!

### 2. Local Dialogue with Claude Code: Co-Building Your Entities
This project is not a rigid script. It is designed to be operated via **direct local conversation with Claude**:
* **A sparring partner for your brand:** When creating a new entity (`entities/my-channel/`), simply ask Claude to help craft your `config.yml`. Describe your audience: Claude will suggest impactful color palettes, titling hooks (curiosity gap vs. direct question), and classify your portrait poses by emotional tone.
* **Creative synergy:** Because Claude natively reads and aligns with your entity's brand guidelines, generation prompts become remarkably sharp and consistent.

### 3. The Technical Breakthrough: "Two Layers, Two Passes"
Originally, the naive approach was to prompt the model for the entire thumbnail in a single shot (background + typography + creator face). **It was a frustrating dead end**:
* If the illustration was stunning but a word needed tweaking, re-running the prompt wiped out the entire image.
* AI-generated faces were unpredictable and inconsistent.

Through hands-on experimentation with Claude, the breakthrough emerged: **decouple generation into two distinct passes**:
1. **Pass 1 (AI Generation):** Generate an atmospheric background with the thematic illustration and typography, strictly forbidding any human figure and reserving a designated dark corner.
2. **Pass 2 (Local Compositing):** Once the background is approved, it is locked in. A local Python script with Pillow overlays the creator's real photo with a clean circular mask and luminous glow effect.

Result: **zero regression**, authentic creator recognition, and stress-free iterative refinement.

---

## 📁 Project Architecture

The project manages **multiple channels or creator brands (multi-entity)** with complete isolation:

```
youtube-thumbnail-generator-ai/
├── .claude/
│   └── skills/thumbnail-generator/skill.md   ← The Claude Code skill (/thumbnail-generator)
├── entities/
│   ├── _template/                             ← Ready-to-duplicate template for any new channel
│   └── demo/                                  ← Working demo profile pre-configured
│       ├── config.yml                         ← Brand guidelines, title rules, layouts
│       └── photos/                            ← Cutout photos (transparent PNG)
├── output/                                    ← Generated thumbnails folder (.gitkeep)
├── build_request.py                           ← API payload builder
├── extract_image.py                           ← Background extraction from JSON response
├── composite_portrait.py                      ← Local portrait compositing with cutout photo
├── .env.example                               ← API key template file
├── .gitignore                                 ← Airtight protection (ignores .env and generated images)
└── LICENSE                                    ← MIT open-source license
```

---

## 🚀 Quick Start

### 1. Prerequisites
* Python 3.10+ with Pillow:
  ```bash
  pip install Pillow pyyaml
  ```
* A Google Gemini API key ([Get a free key on Google AI Studio](https://aistudio.google.com/app/apikey)).

### 2. Configuration
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Edit `.env` and paste your key:
```env
NANOBANANA_API_KEY=your_api_key_here
```

---

## 🎬 Usage

### Method 1: With Claude Code (Recommended)

Launch Claude Code inside this project directory:
```bash
claude
```
The `/thumbnail-generator` skill is automatically detected. Simply run:
```
/thumbnail-generator
```

**What the skill handles interactively:**
1. Asks which entity to use (e.g. `demo` or your custom channel).
2. Asks for the video topic, keywords, and tone.
3. Proposes 3 high-CTR titles tailored to your brand style.
4. Recommends the best matching portrait pose from your photo catalog.
5. Generates the background and executes the local composite into `output/`.

*One-line prompt example:*
```
/thumbnail-generator for demo, topic: Automating SMB workflows with AI, keywords: productivity, time savings, python
```

---

### Method 2: Standalone Python Scripts

You can also run each step manually:
1. `python build_request.py`: creates the `request.json` payload.
2. `python extract_image.py`: decodes and saves the generated background image from `response.json`.
3. `python composite_portrait.py`: composites the transparent cutout portrait onto the background.

---

## 🎨 Setting Up Your Own Channel

1. Duplicate `entities/_template/` to `entities/my-channel/`.
2. Add your transparent PNG portrait photos to `entities/my-channel/photos/`.
3. Edit `entities/my-channel/config.yml` to set:
   * **Brand guidelines** (background mood, title colors, typography).
   * **Photo catalog** (styles, expressions, placements).
   * **Editorial line** and titling constraints.
4. Run `/thumbnail-generator for my-channel`!

---

## 🔒 Privacy & Security

* The `.env` file holding your API key is strictly excluded by `.gitignore`.
* Generated images in `output/` remain local and are never tracked by git.
* No data or photos are transmitted to third parties other than the official Google Gemini API call.

---

## 📄 License

Distributed under the **MIT License**. Free for personal and commercial use. See [LICENSE](LICENSE) for details.

---

## 👨‍💻 About the Author — Chris Figures It Out

I’m **Chris**, a self-taught creator who likes to figure things out.

I explore AI, automation, software, and digital tools — not by pretending to have all the answers, but by actually trying things, breaking things, and finding practical solutions to real-world problems.

On this channel, I share what I discover: useful tools, experiments, workflows, and things I build myself.

> *No hype. No guru talk. Just one simple principle:*  
> **"If there’s a problem, let’s figure it out."**

---

### 💼 Work & Contact
* 📺 English Channel: **Chris Figures It Out**
* 📺 French Channel: **[@ChrisAutodidacte](https://www.youtube.com/@ChrisAutodidacte)**
* 🌐 Business & Consulting: **[chrisconseil.fr](https://chrisconseil.fr)** (Custom AI automation & software workflows)

