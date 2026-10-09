# LateNightBirds website

Static site (HTML/CSS/JS, no build step) for latenightbirds.com — AI Marketing & Automation Agency.
Design inspired by palakonweb.in.

- Local preview: `python3 -m http.server 8765`
- Deploy: automatic — every push to `main` is built and deployed by Cloudflare Workers Builds (config in wrangler.jsonc). Manual: `npx wrangler deploy`
