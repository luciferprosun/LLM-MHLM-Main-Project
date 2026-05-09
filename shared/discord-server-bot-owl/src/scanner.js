import { config } from "./config.js";
import { scanFoundationPages } from "./foundationPages.js";
import { fetchGrantDetail, searchGrantsGov } from "./grantsGov.js";
import { readGrants, shortId, writeGrants } from "./storage.js";

export async function runGrantScan(extraKeywords = []) {
  const keywords = [...new Set([...config.keywords, ...extraKeywords].filter(Boolean))];
  const existing = await readGrants();
  const byId = new Map(existing.map((grant) => [shortId(grant.source, grant.id), grant]));
  const newlyFound = [];

  for (const keyword of keywords) {
    const hits = await searchGrantsGov(keyword);
    for (const hit of hits) {
      const key = shortId(hit.source, hit.id);
      const detail = await fetchGrantDetail(hit.id);
      const grant = {
        ...byId.get(key),
        ...hit,
        ...detail,
        seenAt: byId.get(key)?.seenAt || new Date().toISOString(),
        updatedAt: new Date().toISOString()
      };
      if (!byId.has(key)) {
        newlyFound.push(grant);
      }
      byId.set(key, grant);
    }
  }

  for (const pageHit of await scanFoundationPages()) {
    const key = shortId(pageHit.source, pageHit.id);
    const grant = {
      ...byId.get(key),
      ...pageHit,
      seenAt: byId.get(key)?.seenAt || new Date().toISOString(),
      updatedAt: new Date().toISOString()
    };
    if (!byId.has(key)) {
      newlyFound.push(grant);
    }
    byId.set(key, grant);
  }

  const grants = [...byId.values()].sort((a, b) =>
    String(b.updatedAt || "").localeCompare(String(a.updatedAt || ""))
  );
  await writeGrants(grants);
  return { grants, newlyFound };
}

export function formatGrant(grant, index = null) {
  const prefix = index === null ? "" : `#${index} `;
  const dates = [grant.openDate && `open ${grant.openDate}`, grant.closeDate && `close ${grant.closeDate}`]
    .filter(Boolean)
    .join(" | ");
  const contact = grant.contactEmail ? `\nContact: ${grant.contactEmail}` : "";
  const money = [grant.awardFloor && `floor ${grant.awardFloor}`, grant.awardCeiling && `ceiling ${grant.awardCeiling}`]
    .filter(Boolean)
    .join(" | ");
  return [
    `${prefix}${grant.title}`,
    grant.agency ? `Agency/source: ${grant.agency}` : "",
    grant.status ? `Status: ${grant.status}` : "",
    dates,
    money,
    contact,
    grant.url
  ]
    .filter(Boolean)
    .join("\n");
}

export function filterGrants(grants, query) {
  const q = query.toLowerCase();
  return grants.filter((grant) =>
    [grant.title, grant.agency, grant.keyword, grant.summary, grant.description]
      .filter(Boolean)
      .join(" ")
      .toLowerCase()
      .includes(q)
  );
}

