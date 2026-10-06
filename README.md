# Purchase Predictor

Purchase Predictor is a retail intelligence application that turns receipt images into actionable buying insights. It captures what customers buy, learns their repeat purchase patterns, and recommends relevant sales, bundle offers, and specials based on their history.

This project is designed to help retailers move from manual receipt review to automated customer behaviour analysis and smarter promotional suggestions.

---

## Why this project matters

Retailers often receive large amounts of purchase data from receipts, but much of it remains unstructured and difficult to act on. This app solves that by:

- reading receipt images with OCR
- extracting purchased items and prices
- matching products to a catalog
- tracking customer purchasing habits over time
- suggesting relevant promotions based on behaviour

The result is a practical system for smarter, more personalized retail offers.

---

## Core workflow

1. A user uploads a receipt photo.
2. The backend extracts text from the image.
3. The system structures the item list.
4. Products are matched to known catalog entries.
5. Purchase history is stored for each customer.
6. Recommendations are generated from repeat purchases and active sales.

---

## Features

- Receipt image upload
- OCR-based extraction of items and totals
- Product normalization and catalog matching
- Purchase history tracking
- Repeat purchase detection
- Sales and special offer suggestions
- Dashboard-friendly product and customer insights
- Extensible recommendation engine for future ML enhancement

---

## Tech stack

### Frontend
- React
- Vite
- JavaScript

### Backend
- Python
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy-ready architecture

### AI and processing
- OCR integration for receipt text extraction
- Google Cloud Vision support in dependencies
- future-ready recommendation pipeline

### Data layer
- PostgreSQL-ready schema design
- product, receipt, and purchase tracking models
- recommendation service layer

---

## Repository structure

```text
purchase-predictor/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── __pycache__/
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
├── planning/
│   └── implementation-plan.md
├── README.md
├── .gitignore
├── .env.example
└── docker-compose.yml
```

---

## Current status

This project is in its early MVP stage.

The repository already includes:

- a FastAPI backend
- a React + Vite frontend
- a basic health-check API route
- a placeholder upload endpoint for receipt processing

Planned next steps include:

- OCR integration for real receipts
- item normalization and product matching
- persistent purchase history storage
- recommendation logic
- dashboard views and reporting

---

## Local development

### 1. Clone the repository

```bash
git clone <repository-url>
cd purchase-predictor
```

### 2. Set up the backend

```bash
cd backend
python -m venv .venv
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

Run the backend:

```bash
uvicorn main:app --reload --port 8080
```

API base URL:

```text
http://localhost:8080
```

### 3. Set up the frontend

```bash
cd ../frontend
npm install
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## API overview

The current backend includes:

- GET /
- GET /health
- POST /upload-receipt

These routes are the starting point for receipt upload and future OCR processing. The receipt upload endpoint currently confirms file receipt and is expected to evolve into a full parsing pipeline.

---

## Environment configuration

Use environment variables for deployment-specific setup such as:

- API port
- database URL
- OCR provider credentials
- file upload paths
- app secret settings

Example:

```env
BACKEND_PORT=8080
FRONTEND_PORT=5173
DATABASE_URL=postgresql://user:password@localhost:5432/purchase_predictor
GOOGLE_CLOUD_PROJECT_ID=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
```

---

## Roadmap

### Phase 1: Foundation
- backend and frontend connection
- upload endpoint
- environment setup
- project structure cleanup

### Phase 2: Receipt intelligence
- OCR integration
- text parsing
- product extraction
- item normalization

### Phase 3: Purchase intelligence
- product catalog matching
- purchase history storage
- category and repeat-purchase analysis

### Phase 4: Recommendation engine
- frequent purchase suggestions
- product affinity rules
- active special recommendations
- bundle suggestions

### Phase 5: Experience and launch
- dashboard UI
- manual review tools
- data validation and testing
- public-ready polish

---

## Contributing

Contributions are welcome as the project expands. For a clean development flow:

- keep frontend and backend concerns separated
- avoid mixing OCR logic into route handlers
- keep recommendation logic in dedicated services
- validate parsed receipt data before storing it as final product records

---

## Project documentation

- Implementation plan: [planning/implementation-plan.md](planning/implementation-plan.md)
- Backend entry: [backend/main.py](backend/main.py)
- Frontend app entry: [frontend/src/App.jsx](frontend/src/App.jsx)

---

## License

This project is currently under active development and has not yet been assigned a public license.

---

## Future direction

This app is intentionally designed to grow from a reliable proof of concept into a more advanced retail analytics product. The next major improvements may include:

- customer authentication and loyalty tracking
- promotion management tools
- more advanced basket analysis
- ML-based personalization
- mobile-first receipt capture
- retailer integrations with POS and inventory systems

