import fs from "node:fs/promises";
import path from "node:path";

const dataDir = new URL("../data/", import.meta.url);
const grantsPath = new URL("../data/grants.json", import.meta.url);
const statePath = new URL("../data/state.json", import.meta.url);

export async function ensureDataDir() {
  await fs.mkdir(dataDir, { recursive: true });
}

export async function readJson(url, fallback) {
  try {
    return JSON.parse(await fs.readFile(url, "utf8"));
  } catch {
    return fallback;
  }
}

export async function writeJson(url, data) {
  await ensureDataDir();
  await fs.writeFile(url, JSON.stringify(data, null, 2), "utf8");
}

export async function readGrants() {
  return readJson(grantsPath, []);
}

export async function writeGrants(grants) {
  await writeJson(grantsPath, grants);
}

export async function readState() {
  return readJson(statePath, {});
}

export async function writeState(state) {
  await writeJson(statePath, state);
}

export function shortId(source, id) {
  return `${source}:${id}`;
}

export function displayPath(fileUrl) {
  return path.resolve(fileUrl.pathname);
}

