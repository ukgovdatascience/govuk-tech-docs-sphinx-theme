# Example components

Here is an example page containing the components of designed into this Sphinx theme. This text is part of the first
header, but you should only use the first header once per page! All text on this page is written in Markdown, and
rendered by the [`myst-parser`][myst] package.

You should see me in the sidebar in the `On this page` section.

## Heading 2

Here is some text under Heading 2. You should see me in the sidebar in the `On this page` section.

### Heading 3

Here is some text under Heading 3. You should see me in the sidebar in the `On this page` section.

#### Heading 4

Here is some text under Heading 4. You should see me in the sidebar in the `On this page` section.

##### Heading 5

Here is some text under Heading 5. You should see me in the sidebar in the `On this page` section.

###### Heading 6

Here is some text under Heading 6. You should see me in the sidebar in the `On this page` section.

## Including images

<!-- TODO: Add captions to figures -->

To include images, you can use either Markdown, reStructuredText (ReST), or pure HTML. We have a GOV.UK logo image at
`../_static/images/govuk-logo.png`.

### Markdown

To include the image in Markdown, add the following text:

```
![GOV.UK logo](../_static/images/govuk-logo.png)
```

to include the image with the alt text `GOV.UK logo`, like so:

![GOV.UK logo](../_static/images/govuk-logo.png)

Note you are limited in image configuration using Markdown.

### reStructured Text

To include the image in ReST, add the following text:

````rest
```{image} ../_static/images/govuk-logo.png
:alt: GOV.UK logo
:width: 200px
```
````

to include the image with the alt text `GOV.UK logo` at a set width of 200 pixels, like so:

```{image} ../_static/images/govuk-logo.png
:alt: GOV.UK logo
:width: 200px
```

Note this ReST syntax will not render in Markdown viewers such as GitHub - use [HTML](#html) instead.

### HTML

To include the image in HTML, add the following text:

```html
<img src="../_static/images/govuk-logo.png" alt="GOV.UK logo" width="200px">
```

to include the image with the alt text `GOV.UK logo` at a set width of 200 pixels, like so:

<img src="../_static/images/govuk-logo.png" alt="GOV.UK logo" width="200px">

[myst]: https://myst-parser.readthedocs.io/
