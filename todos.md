## Design
Define the MVP.
- [x] Summarize the MVP in one sentence
- [x] Define the core value proposition of the MVP
- [ ] Sketch the core user flow in Figma
- [ ] Choose UX library
- [ ] Design high-fidelity mock-ups

## Backend
Implement bare-bones functionality.
- [x] Create a Python virtual env in `backend/`
- [x] Start a FastAPI server
- [x] Create a `POST` endpoint that saves a long URL --> short URL mapping in memory
- [x] Create a `GET` endpoint for short URLs and redirects the user if the mapping exists
- [x] Make the root route the redirect route
Connect SQLite and ORM.
- [x] Install SQLite
- [x] Create DB
- [x] Install SQLAlchemy
- [x] Design DB schema and produce ER diagram
- [x] Learn how and why to save code snippets
- [ ] Write ORM model for `ShortURL` (30 minutes)
- [ ] Test inserting, updating, deleting, and reading records (60 minutes)
- [ ] Learn Alembic and write migrations (45 minutes)
- [ ] Create API routes for inserting and reading records

## Frontend

## Deployment

## Extras
- Add Redis for caching to speed up redirects
- Dockerize for easier deployment
- Analytics for links (# clicks, geography of clickers)
- Allows users to name their links
- Show ads for ad revenue
- Short and memorable name
- Auto-delete old names
- Paid tier for longer hosting, faster speeds, better analytics
- IP tracking to restrict number of link generations on the free tier