# LateNightBirds website

Static site for latenightbirds.com, an AI marketing and automation agency. No framework, no bundler.

- `python3 tools/build.py` regenerates `index.html`, `blog/`, `404.html`, `_redirects`, `sitemap.xml` and `robots.txt`
  (blog source data: `tools/posts.json`, images: `blog/img/`).
- Preview: `python3 -m http.server 8765`
- Deploy: automatic. Every push to `main` is built and deployed by Cloudflare Workers Builds (config in `wrangler.jsonc`).
  Manual: `npx wrangler deploy`
