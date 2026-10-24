# Ecovias

[Open the map](https://finnpauls.de/ecovias/)

An interactive map of ecovias, ecopistas, coastal cycleways and riverside walks across Norte and Centro, Portugal. Includes 49 places, numbered pins, regional and route-type filters, source links and GPX downloads.

Solid lines come from published GPS tracks; dashed lines show OpenStreetMap sections. Hollow pins mark locations without an included track. Gaps and incomplete coverage are described in the route details. Walking routes and cycling restrictions are identified separately.

## Edit and build

The published `index.html` is a self-contained document. Route data, Leaflet and fonts are embedded; an internet connection is needed for OpenStreetMap background tiles.

- `src/shell.html`: layout and map interactions.
- `src/map.css`: styling.
- `src/routes.json`: routes, coordinates, source links and access notes.
- `vendor/`: Leaflet 1.9.4 and embedded Barlow fonts.

After editing the source:

```sh
python3 scripts/build.py
```

Open `index.html` directly, or preview with `python3 -m http.server 8000`. Commit the rebuilt `index.html` with source changes. GitHub Pages publishes the root of `main`.

## Sources and attribution

Route information was collected on 24 October 2026. This is a curated discovery map, not an exhaustive inventory, navigation service or live report of closures. Follow local signs and the linked route operators' current information.

- [OpenStreetMap contributors](https://www.openstreetmap.org/copyright): basemap and route geometry, available under the [ODbL](https://opendatacommons.org/licenses/odbl/1-0/).
- [IP Património](https://www.ippatrimonio.pt/pt-pt/ecopistas): published railway-trail GPS tracks.
- Municipalities, regional tourism organizations and route operators: descriptions, distances and access guidance. Individual links are included in each route's data and map details. These materials retain their respective publishers' rights; no blanket license is asserted for third-party tracks.
- [Leaflet](https://leafletjs.com/): BSD-2-Clause; see `vendor/leaflet-LICENSE.txt`.
- Barlow and Barlow Condensed fonts: SIL Open Font License; notices are included in `vendor/` and in the embedded stylesheet.
