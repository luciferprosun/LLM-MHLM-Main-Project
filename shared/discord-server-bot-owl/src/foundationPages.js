import fs from "node:fs/promises";

const sourcesUrl = new URL("../sources.json", import.meta.url);

function cleanText(html) {
  return html
    .replace(/<script[\s\S]*?<\/script>/gi, " ")
    .replace(/<style[\s\S]*?<\/style>/gi, " ")
    .replace(/<[^>]+>/g, " ")
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/\s+/g, " ")
    .trim();
}

export async function loadSources() {
  return JSON.parse(await fs.readFile(sourcesUrl, "utf8"));
}

export async function scanFoundationPages() {
  const sources = await loadSources();
  const results = [];
  for (const source of sources) {
    try {
      const response = await fetch(source.url, {
        headers: { "user-agent": "discord-grant-bot/0.1 public funding monitor" }
      });
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      const html = await response.text();
      const text = cleanText(html);
      const lower = text.toLowerCase();
      const matched = (source.keywords || []).filter((keyword) =>
        lower.includes(String(keyword).toLowerCase())
      );
      const openSignal =
        /\b(open|apply|application|deadline|request for applications|rfa)\b/i.test(text) &&
        !/\bshowing \d+ results\s+closed\b/i.test(text.slice(0, 2000));
      results.push({
        source: source.id,
        id: source.id,
        title: source.name,
        agency: source.name,
        status: openSignal ? "check-now" : "monitor",
        openDate: "",
        closeDate: "",
        url: source.url,
        keyword: matched.join(", "),
        contactEmail: "",
        summary: text.slice(0, 280)
      });
    } catch (error) {
      results.push({
        source: source.id,
        id: source.id,
        title: source.name,
        agency: source.name,
        status: "error",
        openDate: "",
        closeDate: "",
        url: source.url,
        keyword: "",
        contactEmail: "",
        summary: String(error.message || error)
      });
    }
  }
  return results;
}

