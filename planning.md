# URL Shortener Tasks

## What is a URL shortener?
- Purpose: Turns long URLs into shorter ones to make them easier to share and remember.
- How: Stores a database of short link -> long link mappings. When somebody clicks on the short link, the service redirects them to the longer link.
- Use cases:
  - Twitter user wants to fit a link but doesn't want to go over the character limit
  - Social media (e.g. Instagram) user wants to put a link in their bio but doesn't want to make it ugly; maybe even name it
  - Presenter wants to show links at the end of their presentation that are short enough for the audience to type in

## MVP v0.1.0
- Web page where users can paste a long link, click a button, and get back a working short link that persists for a specified amount of time
- Tech Stack:
  - NextJS for frontend
  - FastAPI for the backend
  - PostgreSQL to store link entries