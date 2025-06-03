# URL Shortener Tasks

## Project Stages
- [x] Learn what a URL Shortener is and what an MVP looks like
- [ ] Design the basic architecture of the MVP
- [ ] Choose a tech stack
- [ ] Implement
- [ ] Deploy on the web

## What is a URL shortener?
- Purpose: Turns long URLs into shorter ones to make them easier to share and remember.
- How: Stores a database of short link -> long link mappings. When somebody clicks on the short link, the service redirects them to the longer link.
- Use cases:
  - Twitter user wants to fit a link but doesn't want to go over the character limit
  - Social media (e.g. Instagram) user wants to put a link in their bio but doesn't want to make it ugly; maybe even name it
  - Presenter wants to show links at the end of their presentation that are short enough for the audience to type in

## MVP Features
- Web page where users can paste a long link, click a button, and get back a working short link

## MVP Architecture
- Tech Stack:
  - NextJS for frontend
  - FastAPI for the backend
  - PostgreSQL to store link entries

## Future Roadmap
- Add Redis for caching to speed up redirects
- Dockerize for easier deployment
- Analytics for links (# clicks, geography of clickers)
- Allows users to name their links
- Show ads for ad revenue
- Short and memorable name
- Auto-delete old names
- Paid tier for longer hosting, faster speeds, better analytics