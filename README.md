# Monocular Depth Estimation SOTA

A research-oriented tracker for monocular depth estimation, metric depth, and spatial intelligence papers.

This repository is part of my AI and spatial intelligence portfolio. It focuses on top-tier papers, official implementations, and practical SOTA signals rather than being a raw bookmark list.

## What I Improved

- Organized monocular depth papers by research problem instead of only by year.
- Added mandatory coverage for Depth Pro, Depth Anything, and Depth Anything V2.
- Split the field into relative depth, metric depth, diffusion-based geometry, video depth, and spatial intelligence foundation models.
- Added concise technical notes for key model families so the repository is useful for review, reproduction, and interview discussion.
- Included a structured paper database in `data/papers.json` and a validation script to keep entries consistent.
- Added a practical evaluation checklist for future experiments on indoor, outdoor, in-the-wild, and video depth cases.

## Scope

The first version tracks papers and systems that are especially relevant to:

- Spatial intelligence
- Monocular depth estimation
- Zero-shot and foundation-model depth estimation
- Metric depth from a single image
- Geometry-aware scene understanding
- Depth as a bridge to 3D reconstruction, robotics, AR, and view synthesis

## Quick Map

| Problem | Strong starting points | Why it matters |
| --- | --- | --- |
| Robust relative depth | MiDaS, DPT, Depth Anything, Depth Anything V2 | Strong zero-shot structure and cross-domain generalization |
| Zero-shot metric depth | Depth Pro, Metric3D, UniDepth | Recover depth with physical scale from single images |
| High-frequency boundaries | Depth Pro, Marigold, GeoWizard | Better thin structures, object boundaries, and 3D reconstruction cues |
| Diffusion-based geometry | Marigold, GeoWizard | Uses generative priors for in-the-wild dense prediction |
| Video depth | Video Depth Anything | Adds temporal consistency for long videos |
| Spatial intelligence foundation models | VGGT, UniDepth, Metric3D | Moves from depth maps toward cameras, point maps, tracks, and scene geometry |

## Core SOTA Papers

| Paper / System | Venue | Type | Why I Track It |
| --- | --- | --- | --- |
| [Depth Anything](https://depth-anything.github.io/) | CVPR 2024 | Relative and metric depth foundation model | Large-scale labeled + unlabeled training made monocular depth more robust in the wild |
| [Depth Anything V2](https://depth-anything-v2.github.io/) | NeurIPS 2024 | Depth foundation model | Better details and robustness than V1, with efficient model scales |
| [Depth Pro](https://machinelearning.apple.com/research/depth-pro) | arXiv 2024, Apple ML Research | Zero-shot metric depth | Sharp metric depth and focal length estimation without camera intrinsics |
| [Prompt Depth Anything](https://promptda.github.io/) | CVPR 2025 | Prompted metric depth | Uses sparse LiDAR prompts for high-resolution metric estimation |
| [Video Depth Anything](https://videodepthanything.github.io/) | CVPR 2025 Highlight | Video depth | Extends the Depth Anything line to consistent long-video depth |
| [Metric3D](https://github.com/YvanYin/Metric3D) | ICCV 2023 / TPAMI extension | Zero-shot metric geometry | Handles metric ambiguity across camera models and supports depth + normals |
| [UniDepth](https://lpiccinelli-eth.github.io/pub/unidepth/) | CVPR 2024 Highlight | Universal metric depth | Predicts metric 3D points and camera representation from a single image |
| [Marigold](https://marigoldmonodepth.github.io/) | CVPR 2024 Oral | Diffusion-based depth | Repurposes latent diffusion priors for zero-shot depth |
| [GeoWizard](https://eccv.ecva.net/virtual/2024/poster/1666) | ECCV 2024 | Diffusion-based geometry | Jointly targets depth and normals from single images |
| [VGGT](https://vgg-t.github.io/) | CVPR 2025 Best Paper | Spatial intelligence foundation model | Infers cameras, depth maps, point maps, and 3D tracks from one or more views |

For a longer table with links and categories, see [papers/monocular-depth-sota.md](papers/monocular-depth-sota.md).

## Companion Project Repositories

These repositories turn selected SOTA models into focused portfolio projects by copying the original codebase and adding my own research notes, evaluation scaffolding, and comparison plans.

| Repository | Upstream Model | My Additions |
| --- | --- | --- |
| [depth-pro-research](https://github.com/XuetongFeng/depth-pro-research) | [apple/ml-depth-pro](https://github.com/apple/ml-depth-pro) | Boundary/focal-length notes, evaluation manifest, comparison plan |
| [depth-anything-research](https://github.com/XuetongFeng/depth-anything-research) | [DepthAnything/Depth-Anything-V2](https://github.com/DepthAnything/Depth-Anything-V2) | Family map, model-selection notes, evaluation manifest, comparison plan |
| [metric3d-research](https://github.com/XuetongFeng/metric3d-research) | [YvanYin/Metric3D](https://github.com/YvanYin/Metric3D) | Metric geometry notes, depth/normal manifest, comparison plan |
| [vggt-research](https://github.com/XuetongFeng/vggt-research) | [facebookresearch/vggt](https://github.com/facebookresearch/vggt) | Spatial intelligence notes, scene manifest, comparison plan |

## Reading Path

1. Start with MiDaS and DPT to understand robust relative depth and transformer dense prediction.
2. Move to ZoeDepth, Metric3D, UniDepth, and Depth Pro for the shift from relative depth to metric depth.
3. Read Depth Anything and Depth Anything V2 to understand dataset scaling and foundation-model depth.
4. Compare Marigold and GeoWizard for diffusion priors in single-image geometry.
5. Extend to Prompt Depth Anything and Video Depth Anything for prompted and temporal depth.
6. Connect the depth literature to spatial intelligence through VGGT and other geometry foundation models.

## Repository Structure

```text
.
├── README.md
├── data/
│   └── papers.json
├── notes/
│   ├── depth-anything.md
│   ├── depth-pro.md
│   └── evaluation-checklist.md
├── papers/
│   └── monocular-depth-sota.md
├── scripts/
│   └── validate_papers.py
└── LICENSE
```

## Next Work

- Add reproduction notes for Depth Pro and Depth Anything V2.
- Add a benchmark matrix for NYUv2, KITTI, ETH3D, DIODE, ScanNet++, and in-the-wild images.
- Add a small qualitative gallery after running selected models on the same images.
- Add a decision guide for choosing relative, metric, diffusion, or video depth models.

## Disclaimer

This repository is a curated research tracker. It does not claim to be an official leaderboard. SOTA status can depend on benchmark, training data, evaluation protocol, resolution, camera model, and whether metric scale is required.
