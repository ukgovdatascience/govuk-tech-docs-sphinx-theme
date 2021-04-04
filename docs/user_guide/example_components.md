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

## Adding mathematics

To render mathematics in Sphinx, you need to have the [Sphinx MathJax extension enabled][sphinx-mathjax]. There are two
allowed formats; [dollar](#dollar-syntax), and [amsmath](#amsmath-syntax).

### Dollar syntax

Inline mathematics can be written as `$e=mc^{2}$`, which is rendered as $e=mc^{2}$. For block mathematics, wrap your
mathematics block with `$$`. For example:

```
$$
    e=mc^{2}
$$
```

becomes:

$$
    e=mc^{2}
$$

You can also label block mathematics by adding parenthesis after the closing `$$` and reference it like:

```
$$
    e=mc^{2}
$$ (eqn:example)
This is the equation for mass-energy equivalence {eq}`eqn:example`.
```

to give:

$$
    e=mc^{2}
$$ (eqn:example)
This is the equation for mass-energy equivalence {eq}`eqn:example`.

### `amsmath` syntax

This example is taken directly from the [documentation][myst-amsmath] for MyST. If you write the following block of
[`amsmath` syntax][amsmath]:

```
\begin{gather*}
a_1=b_1+c_1\\
a_2=b_2+c_2-d_2+e_2
\end{gather*}

\begin{align}
a_{11}& =b_{11}&
  a_{12}& =b_{12}\\
a_{21}& =b_{21}&
  a_{22}& =b_{22}+c_{22}
\end{align}
```

this will be rendered as:

\begin{gather*}
a_1=b_1+c_1\\
a_2=b_2+c_2-d_2+e_2
\end{gather*}

\begin{align}
a_{11}& =b_{11}&
  a_{12}& =b_{12}\\
a_{21}& =b_{21}&
  a_{22}& =b_{22}+c_{22}
\end{align}

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

[amsmath]: https://ctan.org/pkg/amsmath
[myst]: https://myst-parser.readthedocs.io/
[myst-amsmath]: https://myst-parser.readthedocs.io/en/latest/using/syntax-optional.html#syntax-amsmath
[myst-maths]: https://myst-parser.readthedocs.io/en/latest/using/syntax.html?highlight=images#math-shortcuts
[sphinx-mathjax]: https://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-sphinx.ext.mathjax
