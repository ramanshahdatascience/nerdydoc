# Build a Python documentation site from NumPy-style docstrings

*Currently just an idea*

When building a quantitative tool in Python, I want a good readable static
documentation website that explains the public API of a good readable codebase.
I would write and maintain
[NumPy-style](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt)
docstrings, which I find quite compatible with a "good readable codebase." The
codebase would map to a bitwise-reproducible website with a single command
line. Configuration would be minimal and declarative, based on data, not code;
authorship outside of the codebase, beyond canonical text-based artifacts like
the project `README`, would be zero. To reward the author for good docstring
and `README` authorship and minimize locations for decaying documentation,
content in the site would be restricted to two sources: (a) docstring material
and (b) entire files, such as the `README` and `LICENSE`, patched into the
site. I'd be able to configure my repo to render GitHub Pages from the `docs/`
directory on `master` and be done.

I'm OK with an opinionated web design if it's good and removes moving parts
from the workflow. I'm OK jettisoning features like doctests that violate the
Single Responsibility Principle.

[Sphinx](http://sphinx-doc.org) is the de facto standard in this problem space.
The [napoleon](http://www.sphinx-doc.org/en/stable/ext/napoleon.html) Sphinx
extension handles NumPy-style docstrings. But for me, Sphinx has been a major
blocker in achieving the above goals.

- Configuring Sphinx is a nightmare. `sphinx-quickstart` is a pop quiz that I
  perennially fail. Mucking around in `conf.py` engenders enough friction that
  I end up without documentation websites at all.
- When maintaining the docs, the Sphinx diffs are a nightmare. When reviewing a
  PR, it is difficult to confirm by inspection that the docs were re-built to
  reflect the latest version of the codebase. I'd love a solution that involves
  a single source of truth in version control rather than a codebase and a
  duplicative static website susceptible to stale-cache mistakes. Deploying
  documentation with the old `gh-pages` workflow involved severe abuse of Git
  branching, which I hated. But now that GitHub Pages can deploy from `master`,
  I feel what GitHub offers is good enough to justify a single duplicative
  build artifact.
- `autodoc` makes it hard to surface a package's public API. By default, I am
  inundated with junk documentation of leading-underscore internal functions
  that the user is not supposed to know about. The natural naming surfaced by
  Sphinx reflects the directory structure of my package, not the idiomatic
  structure of the API the user is supposed to consume.
- Sphinx seems built around authorship external to the codebase. My patience
  for editing ReStructuredText files in `docs/source/` is quite thin; I'll do
  it when hosting teaching material on GitHub, but when building or maintaining
  a software library, I won't.

But to respect the ecosystem, I'd like `nerdydoc` to play nicely enough with
Sphinx. The systems will be different enough that "subset" is not a great term,
but one should not be able to write a `nerdydoc`-compilable piece of source
documentation (docstring, `README`, etc.) that breaks Sphinx. Then a `nerdydoc`
user has a clear roadmap to migrating to a fancier documentation site when the
need arises: simply switch to Sphinx. There would be no more overhead than in
configuring a Sphinx site in the first place.

I quite admire [pdoc](https://github.com/BurntSushi/pdoc); its performance,
ease of use, and focus on a package's public API is a major inspiration. But
enough details are different that a different documentation tool may be
warranted:

- I want to patch my `README`, `LICENSE`, etc., into the documentation site.
- I want to optimize for readability of the multi-paragraph documentation
  typically written for complex mathematical functions.
- I want to render NumPy-style docstrings.
- I want GitHub Pages conventions for the output to be the default.
