import { formatGrant, runGrantScan } from "./scanner.js";

const keywords = process.argv.slice(2);
const { grants, newlyFound } = await runGrantScan(keywords);

console.log(`Total stored: ${grants.length}`);
console.log(`New this scan: ${newlyFound.length}`);
for (const [index, grant] of grants.slice(0, 10).entries()) {
  console.log("\n" + formatGrant(grant, index + 1));
}

