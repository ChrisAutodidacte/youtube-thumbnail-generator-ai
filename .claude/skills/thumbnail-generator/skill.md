---
name: thumbnail-generator
description: >
  Autonomous multi-entity YouTube thumbnail generator powered by Gemini Image API and Claude Code.
  Supports multiple channels or creator brands with custom visual guidelines, layout affinities, and local portrait compositing.
  Usage: /thumbnail-generator
---

# Skill: YouTube Thumbnail Generator — Multi-Entity & AI

You are a YouTube growth and click-through rate (CTR) expert. This skill is **multi-entity**: it generates custom thumbnails for multiple distinct channels or creator personas, each with its own visual brand identity, cutout photo catalog, and titling rules.

## Step 0 — Identify the Target Entity

1. **Locate generator root**: Find the folder containing `entities/`, `output/`, and `.env`. Usually the current working directory.
2. **List available entities**: Scan `entities/` (ignore folders starting with `_` such as `_template`).
3. **Determine target entity**:
   - If specified by user (e.g., "for demo", "for my-channel"), use it.
   - If only one entity exists, use it directly.
   - Otherwise, prompt the user with the list of available entities.
4. **Verify**: Ensure `entities/{entity}/config.yml` and `entities/{entity}/photos/` exist.

## Step 1 — Load Entity Configuration

Read `entities/{entity}/config.yml`. This file defines all parameters: brand identity, colors, photo catalog, layouts, prompt template, and titling constraints. Never hardcode values that reside in YAML.

## Step 2 — Collect Video Information

Gather from the user (if not already provided in initial request):
1. **Video Theme**: Main topic or subject matter.
2. **Keywords**: 3 to 5 key search terms.
3. **Short Description**: 1-2 sentences summarizing the value proposition.
4. **Tone** (optional): Serious, energetic, educational, urgent, etc.

## Step 3 — Propose High-CTR Titles

Based on `title_rules` in config:
- Generate **3 distinct title + subtitle combinations**:
  - One curiosity-gap / shocking title
  - One direct question title
  - One listicle / numbered proof title
- Strictly respect character length limits.
- Present the 3 choices and let the user pick or customize.

## Step 4 — Select Portrait Photo

From the `photos` list in the entity config:
1. Analyze the chosen tone and title.
2. Recommend the best matching photo with a 1-sentence rationale.
3. Confirm with the user.

Photos are located in: `entities/{entity}/photos/{filename}`.

## Step 5 — Choose Layout & Build Prompt

### 5a — Layout
Select the layout whose `affinities` best match the theme and tone.

### 5b — Prompt Template
Fill in the prompt template from config:
- `{title}`, `{subtitle}`: From Step 3.
- `{theme}`, `{keywords}`: From Step 2.
- `{layout_composition}`: From selected layout.
- `{illustration_description}`: Generate a clean 3D or isometric illustration idea tailored specifically to the topic.
- `{creative_element}`: A visual contrast hook or focal point.
- `{brand.*}`: Brand colors, background gradient, typography.

**Crucial constraint**: Explicitly forbid drawing human figures or faces, and reserve a clean dark space in the designated corner for local portrait compositing.

## Step 6 — Call Gemini Image Generation API

1. Load API key from `.env` (`NANOBANANA_API_KEY`).
2. Build request payload and call the Gemini API endpoint.
3. Save the returned image as the base background in `output/{entity}/thumbnail-bg.jpg`.

## Step 7 — Local Portrait Compositing

Run the local Pillow composition script:
- Composite the creator cutout photo onto the background inside a clean circular crop.
- Apply the glowing neon border and subtle halo effect.
- Export the final 1280x720 JPEG thumbnail in `output/{entity}/`.
- Present the thumbnail to the user!
