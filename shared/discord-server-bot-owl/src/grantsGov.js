import { config } from "./config.js";

const SEARCH_URL = "https://api.grants.gov/v1/api/search2";
const DETAIL_URL = "https://api.grants.gov/v1/api/fetchOpportunity";

export async function searchGrantsGov(keyword, rows = config.grantsGovRows) {
  const response = await fetch(SEARCH_URL, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      rows,
      keyword,
      oppStatuses: "forecasted|posted",
      fundingInstruments: "G",
      sortBy: "openDate|desc"
    })
  });
  if (!response.ok) {
    throw new Error(`Grants.gov search failed: ${response.status}`);
  }
  const data = await response.json();
  const hits = data?.data?.oppHits || [];
  return hits.map((hit) => ({
    source: "grants.gov",
    id: String(hit.id || hit.number),
    title: hit.title || "Untitled opportunity",
    agency: hit.agencyName || hit.agencyCode || "",
    status: hit.oppStatus || "",
    openDate: hit.openDate || "",
    closeDate: hit.closeDate || "",
    url: `https://www.grants.gov/search-results-detail/${hit.id}`,
    keyword,
    contactEmail: "",
    summary: `${hit.agencyName || ""} ${hit.number || ""}`.trim()
  }));
}

export async function fetchGrantDetail(opportunityId) {
  const response = await fetch(DETAIL_URL, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ opportunityId: Number(opportunityId) })
  });
  if (!response.ok) {
    return {};
  }
  const data = await response.json();
  const synopsis = data?.data?.synopsis || {};
  return {
    contactEmail: synopsis.agencyContactEmail || "",
    contactName: synopsis.agencyContactName || "",
    awardCeiling: synopsis.awardCeilingFormatted || synopsis.awardCeiling || "",
    awardFloor: synopsis.awardFloorFormatted || synopsis.awardFloor || "",
    description: synopsis.synopsisDesc || ""
  };
}

