# Entity Photos

Drop transparent cutout PNG portrait photos of the channel host or creator here.

## Recommendations

- **Format**: PNG with transparent background (cutout) — ideal for clean local compositing.
- **Resolution**: 1024x1024 minimum, ideally 2048x2048 for crisp sharpness.
- **Variety**: Prepare 3-5 distinct poses (smiling front, pointing forward, thumb up, thinking gesture) so the skill can choose the right expression for each video topic.
- **Lighting**: Even lighting with clean edges.

## Adding to Config

List each photo in your `entities/my-channel/config.yml` under `photos:`:

```yaml
photos:
  - file: "host-smiling.png"
    style: "cutout-color"
    description: "Front smiling headshot, energetic tone"
    placement: "bottom-right corner"
```
