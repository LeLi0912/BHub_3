# Frontend Skeleton

Use `/前端骨架` when the project needs frontend structure, frontend repair, UI consistency, or a minimal runnable frontend base.

## Design-First Gate

Frontend architecture starts with design direction, not page generation.

Do not build pages, layouts, or component variants until these are written into frontend truth documents:

- Design priority: what the product should feel like for its users.
- Visual style: information density, spacing, typography, color direction, component shape, interaction tone, and page rhythm.
- Reference analysis: what to learn from references and what not to copy.
- UI library or component strategy.
- Design tokens: named rules for color, font, spacing, radius, shadow/elevation, layout width, breakpoints, and state styles.

If any of these are missing, stop before implementation and run a frontend architecture clarification. A non-technical user should see one recommended style route, not several equal visual directions.

Token-first means new pages and components must consume agreed tokens instead of inventing page-local colors, spacing, font sizes, border radii, shadows, or status colors.

## Before Coding

Define and write to truth documents:

- Product visual style.
- Main user flow and first visible route.
- Frontend framework or platform.
- UI component library or component strategy.
- Directory structure.
- Module boundaries.
- Component reuse rules.
- Design tokens.
- Internationalization rule if needed.
- Theme rule if needed.
- First-stage scope and validation.

## Design Style

Ask for references when the user has no vocabulary for style. Analyze references for visual language, information density, spacing, typography, component patterns, and whether they fit the product.

Do not copy a reference product directly.

Output one recommended style route:

- Recommended visual direction.
- Why it fits this product and user group.
- What reference patterns are useful.
- What reference patterns are rejected.
- How the style will be expressed through tokens and components.
- What must not be done, such as mixing multiple visual systems or changing style per page.

Do not start with a generic "modern/simple/clean" answer unless it is translated into concrete token and component decisions.

## Token Truth

Frontend architecture truth must define the minimum token set before skeleton code:

- Color tokens: background, surface, text, border, primary action, secondary action, danger, success, warning, disabled, focus.
- Typography tokens: font family, page title, section title, body, caption, button, table/list text.
- Spacing tokens: page padding, section gap, card/list gap, form gap, inline gap.
- Shape tokens: radius, border, shadow/elevation.
- Layout tokens: content width, sidebar/header height, grid/list density, responsive breakpoints.
- State tokens: hover, active, selected, loading, empty, error, disabled.

For existing projects, first find the current token or style owner. If tokens do not exist, create a minimal token truth before consolidating pages. Do not silently create a second token system.

## Framework And UI Library

Explain in plain language:

- Framework controls project structure and runtime.
- UI library controls common interface components.
- Styling utilities and raw CSS approaches are implementation tools, not design truth by themselves.

Prefer mature frameworks and UI libraries for non-technical users. Mature tools reduce AI improvisation.

If the UI library lacks a project-specific component, build a business component on top of the chosen UI library and design tokens. Do not casually abandon the UI library or mix multiple component systems because one screen is inconvenient.

If a low-level or utility-first styling route is used, it must be governed by the frontend truth document:

- Tokens are defined before page work.
- Component owner and theme/style entry point are explicit.
- Page-local one-off visual values are forbidden unless they become new tokens.
- Reusable components state which tokens they consume.
- Validation checks that new screens do not introduce a second visual system.

## Structure Rules

The frontend skeleton should define:

- Where pages/routes live.
- Where shared components live.
- Where API calls live.
- Where state management lives when needed.
- Where utilities live.
- Where styles and tokens live.
- Where text/i18n resources live when needed.
- How modules such as login, user, order, content, and settings are separated.
- When similar UI should become a reusable component.

Rule of thumb: if a UI structure appears more than twice and is meaningfully similar, consider a reusable component.

Any reusable component must state which tokens it consumes. If it needs a new token, update the token truth first.

## Minimal Runnable Skeleton

The first frontend skeleton should only prove the structure:

- App starts.
- One route/page opens.
- Routing is clear.
- UI library is connected.
- Tokens/theme are available.
- Base layout exists.
- Common components have initial versions.

Do not build all pages in the skeleton stage.

Do not generate pages horizontally one after another before the structure is proven. The skeleton stage proves the rules future pages must follow.

## Existing Project Repair

For existing frontend:

- Identify inconsistent UI patterns.
- Identify repeated components.
- Identify hard-coded colors, spacing, font sizes, and text.
- Identify module boundary problems.
- Propose consolidation in the owner layer.
- Avoid rewriting all pages unless the user approves.

## Validation

Collect evidence:

- Install/start command.
- Local URL or build output.
- Screenshot or visible behavior when possible.
- Files defining tokens, theme, layout, routing, and components.
- Evidence that at least one real route/page and common component consume the token system.
- Evidence that no new page-local visual system was introduced.
- Known unverified items.
- Git checkpoint readiness after the skeleton is proven.
