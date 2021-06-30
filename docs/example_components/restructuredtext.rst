=====================================
Example components - reStructuredText
=====================================

Here is an example page containing the components of designed into this Sphinx theme.
This text is part of the first header, but you should only use the first header once
per page! All text on this page is written in reStructuredText (ReST).

You should see me in the sidebar in the ``On this page`` section.

Heading 2
=========

Here is some text under Heading 2. You should see me in the sidebar in the
``On this page`` section.

Heading 3
---------

Here is some text under Heading 3. You should see me in the sidebar in the
``On this page`` section.

Heading 4
^^^^^^^^^

Here is some text under Heading 4. You should see me in the sidebar in the
``On this page`` section.

Heading 5
~~~~~~~~~

Here is some text under Heading 5. You should see me in the sidebar in the
``On this page`` section.

Heading 6
_________

Here is some text under Heading 6. You should see me in the sidebar in the
``On this page`` section.


Adding mathematics
==================

`To render mathematics in Sphinx, you need to have the Sphinx MathJax extension
enabled <mathjax_>`_. `This example is taken directly from the documentation <myst_>`_
for MyST. If you write the following block of |amsmath|_: ::

    .. math::
        :label: eqn_a

        \begin{gather*}
        a_1=b_1+c_1\\
        a_2=b_2+c_2-d_2+e_2
        \end{gather*}

    .. math::
        :label: eqn_b

        \begin{align}
        a_{11}& =b_{11}&
        a_{12}& =b_{12}\\
        a_{21}& =b_{21}&
        a_{22}& =b_{22}+c_{22}
        \end{align}

this will be rendered as:

.. math::
    :label: eqn_a

    \begin{gather*}
    a_1=b_1+c_1\\
    a_2=b_2+c_2-d_2+e_2
    \end{gather*}

.. math::
    :label: eqn_b

    \begin{align}
    a_{11}& =b_{11}&
      a_{12}& =b_{12}\\
    a_{21}& =b_{21}&
      a_{22}& =b_{22}+c_{22}
    \end{align}

Adding tables
=============

.. TODO: Add captions to tables

Tables are rendered using standard ReST table styles, so this: ::

    +--------------------+-------------------------+
    | Column 1           | Column 2                |
    +====================+=========================+
    | This is some data. | This is some more data. |
    +--------------------+-------------------------+

becomes the following rendered output in the Sphinx documentation:

+--------------------+-------------------------+
| Column 1           | Column 2                |
+====================+=========================+
| This is some data. | This is some more data. |
+--------------------+-------------------------+

Note only left-aligned columns are supported by ReST, without injecting raw HTML.

Including images
================

.. TODO: Add captions to figures

We have a GOV.UK logo image at ``../_static/images/govuk-logo.png`` that we will use in
the following example. To include the image in ReST, add the following text: ::

    .. image:: ../_static/images/govuk-logo.png
        :alt: GOV.UK logo
        :width: 200px

to include the image with the alt text ``GOV.UK logo`` at a set width of 200 pixels,
like so:

.. image:: ../_static/images/govuk-logo.png
    :alt: GOV.UK logo
    :width: 200px

GOV.UK Design System components
===============================

`Some of the GOV.UK Design System components are incorporated into this
theme <govuk-design-components_>`_ .

Notification banner
-------------------

To add a notification banner, add the following code to your ReST file: ::


    .. note:: Notification banner title

        A notification to flag some useful information to the user.

which produces:

.. note:: Notification banner title

    A notification to flag some useful information to the user.

Warning
-------

To add a warning, add the following code to your ReST file: ::

    .. warning::

        A warning.

which produces:

.. warning::

    A warning.

.. |amsmath| replace:: ``amsmath`` syntax
.. _amsmath: https://ctan.org/pkg/amsmath
.. _govuk-design-components: https://design-system.service.gov.uk/components/
.. _mathjax: https://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-sphinx.ext.mathjax
.. _myst: https://myst-parser.readthedocs.io/en/latest/using/syntax-optional.html#syntax-amsmath
