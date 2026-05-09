export const catalog = {
  githubProfile: "https://github.com/luciferprosun",
  mainRepo: "https://github.com/luciferprosun/LSC-6.0",
  auditRepo: "https://github.com/luciferprosun/LSC_MDLH_PRO",
  website: "https://luciferprosun.github.io/akasha-chronicles/",
  zenodoSearch: "https://zenodo.org/search?q=luciferprosun&l=list&p=1&s=10&sort=bestmatch",
  publications: [
    {
      title: "LSC 6.0 Working Paper",
      url: "https://doi.org/10.5281/zenodo.19780616",
      best: true
    },
    {
      title: "LSC 6.0 Software DOI",
      url: "https://doi.org/10.5281/zenodo.19785745",
      best: false
    },
    {
      title: "LSC v1.2.0 Computational Release",
      url: "https://doi.org/10.5281/zenodo.19843361",
      best: true
    },
    {
      title: "LSC 6.2.0 Preprint Release",
      url: "https://doi.org/10.5281/zenodo.19878587",
      best: true
    },
    {
      title: "MDLH Case Study in LLM Hallucination and AI-Assisted Science Audit",
      url: "https://doi.org/10.5281/zenodo.19851006",
      best: true
    },
    {
      title: "LSC 4.2 ULTRA",
      url: "https://doi.org/10.5281/zenodo.19602045",
      best: false
    }
  ]
};

export function formatGitHubLinks() {
  return [
    "GitHub and project links:",
    `- GitHub profile: ${catalog.githubProfile}`,
    `- Main repository: ${catalog.mainRepo}`,
    `- MDLH audit repository: ${catalog.auditRepo}`,
    `- Project website: ${catalog.website}`
  ].join("\n");
}

export function formatPublicationLinks(scope = "best") {
  const publications =
    scope === "all" ? catalog.publications : catalog.publications.filter((publication) => publication.best);

  return [
    scope === "all" ? "Zenodo publications and records:" : "Selected Zenodo publications:",
    ...publications.map((publication) => `- ${publication.title}: ${publication.url}`),
    `- Full Zenodo search: ${catalog.zenodoSearch}`
  ].join("\n");
}

export function formatServerDescription() {
  return [
    "Open computational research lab focused on neutrino-anomaly modeling, AI-assisted scientific workflows, reproducible simulation, and model-lineage audit research.",
    "",
    "This server supports open discussion, technical review, falsification, replication, and documentation across the LSC and MDLH research lines.",
    "",
    `GitHub: ${catalog.mainRepo}`,
    `Zenodo: ${catalog.publications.find((publication) => publication.title === "LSC 6.2.0 Preprint Release")?.url}`,
    `MDLH: ${catalog.publications.find((publication) => publication.title.includes("MDLH"))?.url}`
  ].join("\n");
}

export function formatWelcomePost() {
  return [
    "Welcome to Akasha Chroniclles Open Research Lab.",
    "",
    "This server is dedicated to open computational research across neutrino-anomaly modeling, AI-assisted scientific workflows, reproducible simulation, and model-lineage audit research.",
    "",
    "Core public resources:",
    `- GitHub: ${catalog.mainRepo}`,
    `- Website: ${catalog.website}`,
    `- Zenodo search: ${catalog.zenodoSearch}`,
    "",
    "Use `/github` and `/publications` to browse project links directly from the bot.",
    "Use `/ask` to query the research assistant."
  ].join("\n");
}

export function formatPapersPost() {
  return [
    "Selected publications and research records:",
    "",
    formatPublicationLinks("best")
  ].join("\n");
}
