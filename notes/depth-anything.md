# Depth Anything Notes

Source focus: [Depth Anything](https://depth-anything.github.io/), [Depth Anything V2](https://depth-anything-v2.github.io/), [LiheYoung/Depth-Anything](https://github.com/LiheYoung/Depth-Anything), and [DepthAnything/Depth-Anything-V2](https://github.com/DepthAnything/Depth-Anything-V2).

## Why It Matters

Depth Anything is one of the central model families for modern monocular depth estimation. It is especially relevant to spatial intelligence because it treats depth as a scalable foundation-model problem rather than a narrow dataset-specific task.

## Model Family

| Model | Venue | Role |
| --- | --- | --- |
| Depth Anything | CVPR 2024 | Large-scale robust monocular depth foundation model |
| Depth Anything V2 | NeurIPS 2024 | Stronger details, robustness, and efficiency |
| Prompt Depth Anything | CVPR 2025 | Prompted 4K metric depth with low-resolution LiDAR |
| Video Depth Anything | CVPR 2025 Highlight | Temporal consistency for long videos |

## Key Technical Themes

- Scaling labeled and unlabeled data.
- Using pseudo labels and teacher-student style training.
- Building models that work in the wild rather than only on one benchmark.
- Offering model-size tradeoffs for accuracy, speed, and deployment.
- Extending from single-image relative depth to metric, prompted, and video settings.

## Evaluation Plan

- Use Depth Anything V2 as a default strong baseline for relative depth.
- Compare metric variants against Depth Pro, UniDepth, and Metric3D.
- Evaluate temporal stability with Video Depth Anything instead of frame-wise inference alone.
- Track license and model-size differences before recommending deployment.

## Future Repository Improvements

- Add a minimal inference script for Depth Anything V2.
- Add a model-selection guide: small/base/large/giant and relative/metric/video.
- Add a qualitative comparison set shared with Depth Pro.

