# Monocular Depth Estimation SOTA Papers

Updated: 2026-04-28

This page tracks representative top-tier and SOTA-relevant papers for monocular depth estimation and adjacent spatial intelligence work. It is organized by role in the field instead of publication date alone.

## Foundation Models and Robust Relative Depth

| System | Year | Venue | Main Idea | Links |
| --- | --- | --- | --- | --- |
| MiDaS | 2022 / 2023 | TPAMI / technical report | Robust relative depth through mixed-dataset training and model zoo releases | [GitHub](https://github.com/isl-org/MiDaS) |
| DPT | 2021 | ICCV | Vision transformers for dense prediction, including monocular depth | [CVF](https://openaccess.thecvf.com/content/ICCV2021/html/Ranftl_Vision_Transformers_for_Dense_Prediction_ICCV_2021_paper.html) |
| Depth Anything | 2024 | CVPR | Scales monocular depth training with large labeled and unlabeled data | [Project](https://depth-anything.github.io/), [GitHub](https://github.com/LiheYoung/Depth-Anything) |
| Depth Anything V2 | 2024 | NeurIPS | Improves V1 with synthetic labeled data, larger teachers, and pseudo-labeled real data | [Project](https://depth-anything-v2.github.io/), [GitHub](https://github.com/DepthAnything/Depth-Anything-V2) |

## Zero-Shot Metric Depth

| System | Year | Venue | Main Idea | Links |
| --- | --- | --- | --- | --- |
| ZoeDepth | 2023 | arXiv | Combines relative and metric depth for zero-shot metric transfer | [GitHub](https://github.com/isl-org/ZoeDepth) |
| Metric3D | 2023 / 2024 | ICCV / TPAMI extension | Resolves metric ambiguity across camera models for zero-shot metric depth and normals | [CVF](https://openaccess.thecvf.com/content/ICCV2023/html/Yin_Metric3D_Towards_Zero-shot_Metric_3D_Prediction_from_A_Single_Image_ICCV_2023_paper.html), [GitHub](https://github.com/YvanYin/Metric3D) |
| UniDepth | 2024 | CVPR Highlight | Predicts metric 3D points and camera representation from a single image | [Project](https://lpiccinelli-eth.github.io/pub/unidepth/), [GitHub](https://github.com/lpiccinelli-eth/UniDepth) |
| Depth Pro | 2024 | arXiv / Apple ML Research | Produces sharp metric depth and focal length without camera intrinsics | [Apple](https://machinelearning.apple.com/research/depth-pro), [GitHub](https://github.com/apple/ml-depth-pro) |

## Diffusion-Based Geometry

| System | Year | Venue | Main Idea | Links |
| --- | --- | --- | --- | --- |
| Marigold | 2024 | CVPR Oral | Repurposes Stable Diffusion priors for zero-shot monocular depth | [Project](https://marigoldmonodepth.github.io/), [GitHub](https://github.com/prs-eth/Marigold) |
| GeoWizard | 2024 | ECCV | Uses diffusion priors for single-image depth and normal estimation | [ECCV](https://eccv.ecva.net/virtual/2024/poster/1666) |

## Prompted and Video Depth

| System | Year | Venue | Main Idea | Links |
| --- | --- | --- | --- | --- |
| Prompt Depth Anything | 2025 | CVPR | Prompts Depth Anything with low-resolution LiDAR for 4K metric depth | [Project](https://promptda.github.io/), [GitHub](https://github.com/DepthAnything/PromptDA) |
| Video Depth Anything | 2025 | CVPR Highlight | Consistent depth estimation for arbitrarily long videos | [Project](https://videodepthanything.github.io/), [GitHub](https://github.com/DepthAnything/Video-Depth-Anything) |

## Spatial Intelligence and 3D Foundation Models

| System | Year | Venue | Main Idea | Links |
| --- | --- | --- | --- | --- |
| VGGT | 2025 | CVPR Best Paper | Infers cameras, depth maps, point maps, and point tracks from one or more views | [Project](https://vgg-t.github.io/), [GitHub](https://github.com/facebookresearch/vggt) |

## Notes on SOTA Claims

- Depth estimation leaderboards are fragmented across relative depth, metric depth, zero-shot transfer, indoor, outdoor, in-the-wild, video, and prompted settings.
- A model that is best for boundary sharpness may not be best for metric scale.
- A model that is strong on single images may not be temporally stable on videos.
- A model that reports strong benchmark metrics may have practical limitations around license, resolution, speed, VRAM, or camera assumptions.

