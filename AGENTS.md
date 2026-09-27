# Project Standards

Currently just one standing rule, added as I needed it. More may be added as conventions solidify.


## Seed / mock data quality

When generating, regenerating, or expanding seed data for this project (purchases, books, addresses, etc.), prefer realistic-sounding content over raw Faker output:

- **Book titles** should read as plausible real book titles — either real, well-known titles or invented-but-believable ones. Not Faker's random sentence generator (e.g. not "Wife car less." or "Sea century ever.").
- **Prices** should be realistic for the item type (e.g. a paperback: $8–25, a hardcover: $15–40), not arbitrary random decimals.
- **Addresses** should look like real addresses for the given country — real-sounding street names and city names, correct format — not Faker's occasionally nonsensical combinations.
- Faker remains fine for purely structural/random fields: dates, quantities, IDs, foreign keys.

When asked to touch seeding code or regenerate data, apply this bar without needing it re-explained.
