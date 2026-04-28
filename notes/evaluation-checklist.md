# Evaluation Checklist

Use this checklist before calling a method "SOTA" for a target use case.

## Data and Domain

- Indoor scenes: NYUv2, ScanNet, ScanNet++, ARKitScenes.
- Outdoor driving: KITTI, DDAD, nuScenes.
- In-the-wild images: internet photos, unusual focal lengths, non-standard cameras.
- Fine structures: railings, plants, transparent objects, hair, wires, chair legs.
- Videos: moving camera, moving objects, long temporal windows.

## Depth Type

- Relative depth: good ordering and scene structure, no physical scale.
- Metric depth: physical scale in meters.
- Affine-invariant depth: allows scale and shift alignment.
- Prompted metric depth: uses sparse depth, LiDAR, or other hints.
- Video depth: optimizes temporal consistency as well as per-frame quality.

## Metrics to Track

- AbsRel, SqRel, RMSE, log RMSE.
- Delta accuracy thresholds.
- Scale-invariant metrics.
- Boundary F1 or boundary recall where available.
- Temporal consistency for video.
- Runtime, VRAM, model size, and supported resolution.

## Practical Questions

- Does the method require camera intrinsics?
- Does it output metric scale directly?
- Does the license allow the intended use?
- Are weights public?
- Is the official code maintained?
- Does the method run on available hardware?
- Does the evaluation use the same crop, scale alignment, and split as prior work?

