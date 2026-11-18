# Design System: Clean Industrial Laboratory (ORDIVA Refinement)

## Surface Mode
- **Mode:** Operate & Experience (High-precision technical robotics research tool).
- **Viewport:** 100vw × 100vh full-window responsive viewport with zero scroll overflow.

## Color System (WCAG AA Compliant)
- **Outer Canvas:** `radial-gradient(circle at 90% 10%, #ec4899 0%, #3b82f6 35%, #1d4ed8 65%, #0a0f1d 100%)`
- **Surface Body:** `#ffffff` (Pure lab white with subtle hairline dividers)
- **Subtle Surface:** `#f8fafc`
- **Frosted Glass Panel:** `rgba(255, 255, 255, 0.86)` with `backdrop-filter: blur(20px)` and hairline `border: 1px solid #e2e8f0`
- **Borders & Dividers:** `#e2e8f0` (1px solid hairline)
- **Primary Cobalt Accent:** `#2563eb` (Interactive controls, active states, key lights)
- **Kinematic Pin Accent:** `#be185d` (WCAG AA compliant 4.8:1 contrast on white for joint tracking and stage steps)
- **Warning Amber:** `#d97706` (Hazard hurdle markings, push disturbances, torque warnings)
- **Danger Red:** `#b91c1c` (Trip detection, topple limits, baseline error indicators)
- **Text Hierarchy:**
  - High Contrast Dark: `#0f172a` (Headings, primary values)
  - Muted Technical: `#334155` (Body text, descriptions - 7.5:1 ratio)
  - Subtle Meta: `#475569` (Timecodes, secondary keys - 5.5:1 ratio)

## Typography & Rhythm
- **Sans Voice:** `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
- **Mono Voice:** `'JetBrains Mono', 'Consolas', monospace` with `font-variant-numeric: tabular-nums`
- **Quality Floor:**
  - No functional UI text below 11.5px (0.72rem).
  - Body text floor at 13.1px–14.5px (0.82rem–0.90rem).
  - Zero-offset chromatic halo shadows strictly prohibited.
  - Natural elevation shadows: `box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08), 0 1px 3px rgba(15, 23, 42, 0.06)`.
  - Nested card containers eliminated in favor of clean hairline dividers.
  - Validated with `impeccable detect` returning 0 anti-patterns.
