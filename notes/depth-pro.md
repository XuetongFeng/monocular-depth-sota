# Depth Pro Notes

Source focus: [Apple ML Research](https://machinelearning.apple.com/research/depth-pro) and [apple/ml-depth-pro](https://github.com/apple/ml-depth-pro).

## Why It Matters

Depth Pro is important for spatial intelligence because it targets zero-shot metric depth from a single image without requiring camera intrinsics. That makes it closer to real-world use cases where images are collected from unknown cameras or scraped from the web.

## Core Ideas

- Predicts metric depth with absolute scale.
- Estimates focal length from a single image.
- Emphasizes high-resolution, sharp depth maps with fine boundaries.
- Introduces boundary-aware evaluation utilities in the official implementation.
- Targets fast inference for high-resolution outputs.

## Where It Fits

| Compared With | Depth Pro Position |
| --- | --- |
| Depth Anything V2 | More focused on metric depth and boundary sharpness; Depth Anything V2 is broader as a foundation model family |
| UniDepth | Both target metric depth; UniDepth frames the output as metric 3D points and camera representation |
| Metric3D | Both care about metric scale; Metric3D emphasizes camera-model ambiguity and geometry foundation modeling |
| Marigold / GeoWizard | Diffusion-based methods often produce strong details but may trade off speed and metric scale |

## Evaluation Plan

- Test boundary quality on thin objects, hair-like structures, railings, and object edges.
- Test metric scale on indoor, outdoor, and in-the-wild images.
- Compare focal length estimates when EXIF or known intrinsics are available.
- Compare failure cases against Depth Anything V2 and UniDepth.

## Future Repository Improvements

- Add a reproducible notebook using official Depth Pro weights.
- Add side-by-side qualitative comparisons with Depth Anything V2.
- Add a table separating relative depth quality from metric depth quality.

