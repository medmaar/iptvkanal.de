// Cloudflare Pages Function for POST /api/trial.
// Sends the trial request to the inbox via Resend when RESEND_API_KEY is set
// (optional: TRIAL_TO, TRIAL_FROM). Without it the function answers 503 and the
// page falls back to a prefilled email, so the form always works.
const json = (body, status = 200) => new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' } });
const clean = (value, max = 200) => String(value || '').replace(/[\r\n]+/g, ' ').trim().slice(0, max);

export async function onRequestPost({ request, env }) {
  let data;
  try { data = await request.json(); } catch { return json({ ok: false }, 400); }
  if (data.website) return json({ ok: true }); // honeypot field: silently drop bots

  const lead = {
    first_name: clean(data.first_name, 80), last_name: clean(data.last_name, 80), email: clean(data.email, 120),
    phone: clean(data.phone, 40), device: clean(data.device, 80)
  };
  if (!lead.first_name || !lead.last_name || !lead.device || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(lead.email)) return json({ ok: false }, 400);
  if (!env.RESEND_API_KEY) return json({ ok: false, error: 'not_configured' }, 503);

  const response = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from: env.TRIAL_FROM || 'IPTV Kanal <testzugang@iptvkanal.de>',
      to: [env.TRIAL_TO || 'kontakt@iptvkanal.de'],
      reply_to: lead.email,
      subject: `Kostenlose Testanfrage: ${lead.first_name} ${lead.last_name}`,
      text: `Name: ${lead.first_name} ${lead.last_name}\nE-Mail: ${lead.email}\nWhatsApp: ${lead.phone || '-'}\nGerät: ${lead.device}\n`
    })
  });
  return response.ok ? json({ ok: true }) : json({ ok: false, error: 'send_failed' }, 502);
}

export const onRequest = () => json({ ok: false }, 405);
