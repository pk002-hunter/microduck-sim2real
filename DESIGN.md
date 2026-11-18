# Design System: Clean Industrial Laboratory (ORDIVA Refinement)

## Surface Mode
- **Mode:** Operate & Experience (High-precision technical robotics research tool).

## Color System (WCAG AA Compliant)
- **Outer Canvas:** `radial-gradient(circle at 90% 10%, #ec4899 0%, #3b82f6 35%, #1d4ed8 65%, #0a0f1d 100%)`
- **Surface Card:** `#ffffff` (Pure lab white with 20px rounded corners and subtle diffuse elevation)
- **Subtle Surface:** `#f8fafc`
- **Borders & Dividers:** `#e2e8f0` (1px solid hairline)
- **Primary Cobalt Accent:** `#2563eb` (Interactive controls, active states, key lights)
- **Kinematic Pin Accent:** `#be185d` (WCAG AA compliant 4.8:1 contrast on white for joint tracking and stage steps)
- **Text Hierarchy:**
  - High Contrast Dark: `#0f172a` (Headings, primary values)
  - Muted Technical: `#334155` (Body text, descriptions - 7.5:1 ratio)
  - Subtle Meta: `#475569` (Timecodes, secondary keys - 5.5:1 ratio)

## Typography & Rhythm
- **Sans Voice:** `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
- **Mono Voice:** `'JetBrains Mono', 'Consolas', monospace` with `font-variant-numeric: tabular-nums`
- **Quality Floor:**
  - No functional UI text below 11.5px (0.72rem).
  - Body text floor at 12.5px–13.5px.
  - Zero-offset chromatic halo shadows strictly prohibited.
  - Natural elevation shadows: `box-shadow: 0 1px 3px rgba(15, 23, 42, 0.08), 0 8px 24px rgba(15, 23, 42, 0.05)`.
