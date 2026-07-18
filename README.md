# bracket.ltd

Static site for [bracket.ltd](https://bracket.ltd). Hosted on GitHub Pages.

## Preview

```sh
make preview
```

Serves on `http://localhost:8000` the way GitHub Pages does, so extensionless links like `/terms` resolve to `terms.html`.

## Layout

```
index.html      app grid
kingbit.html    app showcase
terms/privacy/support/404
css/styles.css
assets/         logo, icons, screenshots, badges
```

## Adding an app

Drop a 512×512 icon in `assets/icons/`, then add an `<li>` to the `.apps` list in `index.html`. The list is ordered by App Store release date, newest first.

## Deploy

Push to `master`. `CNAME` points the Pages site at `bracket.ltd`.
