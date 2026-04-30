import * as gsmarena from "gsmarena-api";
import phones from "../data.json" with { type: "json" };

function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

for (const [key, value] of Object.entries(phones)) {
  await sleep(1000);
  const devices = await gsmarena.search.search(key);
  if (devices.length === 0) {
    continue;
  }
  const device = await gsmarena.catalog.getDevice(devices[0].id);
  if (device === null || device.status === 429) {
    break;
  }
  console.log(device);
}
