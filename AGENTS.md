# Delivery workflow

The repository owner has requested that completed tasks be committed and pushed
to `main` on `medmaar/iptvkanal.de`, then deployed to Cloudflare automatically.
This is standing authorization for this repository's normal delivery workflow.
The owner has confirmed that Cloudflare Pages is connected to this repository
and automatically deploys from `main`. A normal push is the deployment trigger;
no separate manual deployment or Cloudflare API token is needed for that trigger.

- Preserve unrelated changes. Run relevant checks before committing.
- Run `python3 scripts/version-assets.py` after editing JavaScript or custom CSS,
  before tests and commits, to update the browser cache keys in the HTML pages.
- Start the static server and use `node scripts/smoke-test.cjs` for site changes
  when Playwright and Chromium are available in the cloud environment.
- Push without force; reconcile upstream changes before delivery.
- Use the existing Cloudflare project and deployment integration. Verify its
  deployment result when access is available. A successful Git push alone does
  not confirm a successful Cloudflare deployment.
- If deployment configuration or access is missing, finish the GitHub delivery
  and report the precise deployment blocker. Keep credentials out of repository
  files, logs, and chat.
