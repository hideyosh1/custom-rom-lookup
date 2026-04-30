import phones from "../../data.json";
import { Grid } from "gridjs";
import "gridjs/dist/theme/mermaid.css";

// console.log(phones);
//
//
let data: any = [];
for (const [key, value] of Object.entries(phones)) {
  let element = document.createElement("tr");
  element.id = key;

  let phone = [
    value.name,
    value.vendor,
    value.codename,
    value.support.join(", ").trim().replace(/,/g, "\n"),
  ];

  data.push(phone);

  console.log(key);
}

new Grid({
  columns: ["name", "vendor", "codename", "support"],
  data: data,
  sort: true,
  pagination: {
    limit: 20,
    summary: false,
  },
  style: {
    table: {},
  },
}).render(document.querySelector("#phonetable")!);
