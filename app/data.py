"""Portfolio content used across Flask templates."""

PROFILE = {
    "name": "Sai Pranavi Kasturi",
    "tagline": "Waterloo CS · automation · quality",
    "headline": (
        "I ship dependable software and strong automation — "
        "with machine learning when it actually moves the needle."
    ),
    "photo": "img/profile.jpg",
    "email": "pkasturi@uwaterloo.ca",
    "linkedin": "https://www.linkedin.com/in/sai-pranavi-kasturi-704807298/",
    "github": "https://github.com/ispilledmymilk",
    "portfolio": "https://ispilledmymilk.github.io/me/",
    "book_call": (
        "https://bookings.cloud.microsoft/bookwithme/user/"
        "f92eabac618d40b0b5a7190f01425a43%40uwaterloo.ca/meetingtype/"
        "W33sTLmNqUaWLWMrW0REuw2?anonymous&ismsaljsauthenabled"
    ),
}

ABOUT = """
Computer Science student (2B) at the University of Waterloo. I care about
automation, testable systems, and full-stack delivery — and I use machine
learning when it clearly improves the outcome.

From Playwright test suites at Zoocasa to AI-assisted compliance workflows and
hackathon-winning fraud detection demos, I like building things that teams can
trust in production. I'm open to recruiting conversations, coffee chats, and
collaboration on interesting technical problems.
""".strip()

EXPERIENCES = [
    {
        "title": "Automation Developer",
        "company": "Zoocasa",
        "location": "Toronto, Canada",
        "dates": "Jan 2026 – Apr 2026",
        "highlights": [
            "Built end-to-end test automation (Playwright, Postman) across JS and Go services, cutting manual QA effort 60%.",
            "Shipped an AI-assisted compliance workflow with natural-language Q&A over policy docs and structured JSON configs.",
            "Ran post-incident reviews and prioritized fixes that lifted reliability 47% in high-risk areas.",
        ],
    },
    {
        "title": "QA Specialist",
        "company": "DocTalk",
        "location": "Toronto, Canada",
        "dates": "May 2025 – Aug 2025",
        "highlights": [
            "Documented 1500+ functional requirements and test cases as a single source of truth for Product and Engineering.",
            "Owned B2B SaaS web improvements end-to-end and validated flows with clinical stakeholders.",
            "Built 1000+ automated regression scenarios (REST + UI) with Playwright and Postman.",
        ],
    },
    {
        "title": "Market Analyst Consultant",
        "company": "Happy Sneeze",
        "location": "USA, Remote",
        "dates": "Apr 2024 – Jul 2024",
        "highlights": [
            "Produced competitive landscape and financial benchmarking for 15+ health-market players.",
            "Sized market segments via reporting and scenario analysis for leadership-level strategy.",
            "Recommended 10 partnership targets with structured outreach narratives for BD.",
        ],
    },
]

EDUCATION = [
    {
        "school": "University of Waterloo",
        "degree": "Bachelor of Computer Science — 2B",
        "location": "Waterloo, Canada",
        "dates": "Sept 2024 – Present",
        "details": [
            "Coursework in algorithms, systems, and software engineering.",
            "Active in hackathons, product clubs, and campus tech community.",
        ],
    },
]

PROJECTS = [
    {
        "name": "RefiMatch",
        "tagline": "Refinance scenarios ranked with AI",
        "dates": "Apr 2026",
        "tags": [
            "Swift", "Python", "SwiftUI", "FastAPI", "Pydantic", "Pandas", "NumPy",
            "LangGraph", "LangChain", "RAG", "pgvector", "PostgreSQL", "Docker",
            "Kubernetes", "GitHub Actions", "pytest", "MCP",
        ],
        "highlights": [
            "Monorepo with SwiftUI iOS 17 client and FastAPI backend comparing refinance offers via a Pandas/NumPy amortization engine.",
            "LangGraph explanation flow with RAG retrieval, pgvector storage, and Langfuse-compatible tracing.",
            "MCP stdio server for lender catalog and scoring; K8s deployment with CI (Ruff, pytest, Promptfoo, DeepEval).",
        ],
    },
    {
        "name": "OmenAI",
        "tagline": "Insider-trading detection on prediction markets — TD Best AI hack winner",
        "dates": "Mar 2026",
        "tags": ["Python", "scikit-learn", "Next.js", "PostgreSQL", "Redis", "Isolation Forest"],
        "highlights": [
            "Scoped an MVP around unlabeled trade streams with tiered risk signals (rules + Isolation Forest).",
            "Prioritized 600K+ live trades into wallet-level features with segment-specific thresholds.",
            "Shipped a live ops dashboard with streaming feeds, radar views, and wallet drill-down.",
        ],
    },
    {
        "name": "Weathwise",
        "tagline": "Money APIs with trust issues—in a good way",
        "dates": "Dec 2025",
        "tags": ["Java", "TypeScript", "Spring Boot", "Angular", "PostgreSQL", "MongoDB", "JWT", "Docker"],
        "highlights": [
            "Defined security and data-isolation requirements (JWT, per-user row scoping, schema versioning).",
            "Scoped OLTP vs. analytics paths with failure-isolated batch slices.",
            "Delivered a containerized MVP with Docker Compose, health checks, and automated auth tests.",
        ],
    },
    {
        "name": "eXplicit",
        "tagline": "Compliance docs that answer back",
        "dates": "Jan 2026",
        "tags": ["Python", "Google Drive API", "OpenAI", "JSON", "Workflow automation"],
        "highlights": [
            "Natural-language Q&A over real-estate feed rules grounded in source docs.",
            "Document-to-config pipeline: Google Drive ingestion and structured JSON per jurisdiction.",
            "Change notifications on Drive edits to regenerate configs and prevent silent drift.",
        ],
    },
    {
        "name": "Squasher",
        "tagline": "Your repo's vibe check",
        "dates": "Jan 2026",
        "tags": ["Python", "TypeScript", "FastAPI", "LangGraph", "VS Code API", "ChromaDB", "SQLite", "Docker"],
        "highlights": [
            "Split client–server platform: FastAPI service plus VS Code extension with risk dashboards.",
            "LangGraph state machine fusing complexity, git-blame velocity, import graphs, and ChromaDB retrieval into a 0–100 score.",
            "SQLite metric history, WebSocket progress fan-out, Dockerized deploys with auth and health probes.",
        ],
    },
    {
        "name": "Saiborg",
        "tagline": "Talk, type, search, schedule—one assistant that remembers all",
        "dates": "Nov 2025",
        "tags": ["Python", "JavaScript", "FastAPI", "Electron", "Uvicorn", "OAuth 2.0"],
        "highlights": [
            "FastAPI assistant with Web Speech voice capture, typed chat, and Programmable Search with LLM summaries.",
            "Google Calendar OAuth desktop flow with token refresh and CRUD helpers.",
            "Electron wrapper supervising uvicorn with optional Spotify OAuth for now-playing cards.",
        ],
    },
    {
        "name": "Smart Mirror — AuraGlass",
        "tagline": "Mirror, mirror on the wall",
        "dates": "Oct 2024",
        "tags": ["Bash", "JavaScript", "Raspberry Pi 4", "OpenAI", "GitLab CI"],
        "highlights": [
            "Modular JavaScript services on Raspberry Pi 4 with Bash-orchestrated boot path.",
            "Integrated Google Calendar, Spotify, and OpenAI-powered glanceable cards.",
            "Team-led integration testing across seven mirror surfaces; ~90% scenario pass rate.",
        ],
    },
    {
        "name": "Running Alarm Clock — Alarmy",
        "tagline": "The snooze button's nemesis",
        "dates": "Sept 2023",
        "tags": ["Java", "Arduino", "Git"],
        "highlights": [
            "Java-hosted verification harness around Arduino alarm firmware with serial protocol tracing.",
            "20+ automated cases spanning wake windows, snooze edge cases, and power-loss recovery.",
            "80% measured pass rate on full test matrix with documented regression artifacts.",
        ],
    },
]

HOBBIES = [
    {
        "name": "Listening to Music",
        "description": (
            "Always have something playing — from focus playlists while coding "
            "to unwind tracks after a long day."
        ),
        "image": "img/hobbies/music-placeholder.svg",
        "link": {
            "url": "https://open.spotify.com/user/3175ftsdm6b3f32yuevfpbprd2pq?si=c44b05b9384d4ee8",
            "label": "My Spotify",
        },
        "extra_image": {
            "src": "img/hobbies/spotify-wrapped-placeholder.svg",
            "alt": "Spotify Wrapped",
        },
    },
    {
        "name": "Going to the Gym",
        "description": (
            "Regular gym sessions to stay active and clear my head between "
            "classes and project sprints."
        ),
        "image": "img/hobbies/gym-placeholder.svg",
    },
    {
        "name": "Eating Out",
        "description": (
            "Trying new restaurants around Waterloo and Toronto — always on the "
            "hunt for a good spot to catch up over a meal."
        ),
        "image": "img/hobbies/restaurant-placeholder.svg",
    },
    {
        "name": "Going to Costco",
        "description": (
            "The classic Costco run — stocking up, sample hunting, and somehow "
            "always leaving with more than planned."
        ),
        "image": "img/hobbies/costco-placeholder.svg",
    },
    {
        "name": "Hanging Out with Friends",
        "description": (
            "Game nights, campus hangouts, and spontaneous adventures with "
            "friends — the best way to recharge."
        ),
        "image": "img/hobbies/friends-placeholder.svg",
    },
]

TRAVEL_LOCATIONS = [
    {
        "name": "Waterloo, Canada",
        "lat": 43.4643,
        "lng": -80.5204,
        "note": "Home base — University of Waterloo",
    },
    {
        "name": "Toronto, Canada",
        "lat": 43.6532,
        "lng": -79.3832,
        "note": "Internships at Zoocasa & DocTalk",
    },
    {
        "name": "Vancouver, Canada",
        "lat": 49.2827,
        "lng": -123.1207,
        "note": "West coast visits",
    },
    {
        "name": "New York, USA",
        "lat": 40.7128,
        "lng": -74.0060,
        "note": "City exploration",
    },
    {
        "name": "San Francisco, USA",
        "lat": 37.7749,
        "lng": -122.4194,
        "note": "Tech scene & conferences",
    },
    {
        "name": "Hyderabad, India",
        "lat": 17.3850,
        "lng": 78.4867,
        "note": "Family visits",
    },
    {
        "name": "London, UK",
        "lat": 51.5074,
        "lng": -0.1278,
        "note": "Summer travel",
    },
    {
        "name": "Lagos, Nigeria",
        "lat": 6.5244,
        "lng": 3.3792,
        "note": "Nigeria visit",
    },
    {
        "name": "Barcelona, Spain",
        "lat": 41.3874,
        "lng": 2.1686,
        "note": "City exploration",
    },
    {
        "name": "Rome, Italy",
        "lat": 41.9028,
        "lng": 12.4964,
        "note": "Italian getaway",
    },
    {
        "name": "Naples, Italy",
        "lat": 40.8518,
        "lng": 14.2681,
        "note": "Southern Italy",
    },
    {
        "name": "Nice, France",
        "lat": 43.7102,
        "lng": 7.2620,
        "note": "French Riviera",
    },
    {
        "name": "Cannes, France",
        "lat": 43.5528,
        "lng": 7.0174,
        "note": "French Riviera",
    },
    {
        "name": "Dubai, UAE",
        "lat": 25.2048,
        "lng": 55.2708,
        "note": "UAE visit",
    },
]

# Navigation entries power the dynamic menu bar in base.html.
PAGES = [
    {"endpoint": "index", "label": "Home"},
    {"endpoint": "hobbies", "label": "Hobbies"},
    {"endpoint": "projects", "label": "Projects"},
    {"endpoint": "travel", "label": "Travel Map"},
]
