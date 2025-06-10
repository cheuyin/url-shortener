# URL Shortener Tasks

## What is a URL shortener?
- Purpose: Turns long URLs into shorter ones to make them easier to share and remember.
- How: Stores a database of short link -> long link mappings. When somebody clicks on the short link, the service redirects them to the longer link.
- Use cases:
  - Twitter user wants to fit a link but doesn't want to go over the character limit
  - Social media (e.g. Instagram) user wants to put a link in their bio but doesn't want to make it ugly; maybe even name it
  - Presenter wants to show links at the end of their presentation that are short enough for the audience to type in

## MVP v0.1.0
A website where users can generate shortened URLs with custom aliases.
- Core Value Proposition:
  - Users get clarity about how long their link will last
  - No frills flow for generating their link
- Features:
  - Single page where users can paste their link and get back a shortened link that persists for at least a month
  - Users can choose an alias or just generate a random alias
  - Allow users to configure how long their link lasts. When a link expires, the alias gets recycled for reuse.

