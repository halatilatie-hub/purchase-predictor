# Purchase Predictor Implementation Plan

## Overview
This project is a receipt-based purchase intelligence app. The workflow is:

1. A user uploads a picture of a receipt.
2. OCR extracts the purchased items and totals.
3. The system matches the parsed items to a product catalog.
4. Purchase history is stored by customer and time period.
5. The app suggests sales, specials, and bundled promotions based on previous buying behaviour.

The first version should focus on a working end-to-end flow rather than a fully advanced recommendation system.

---

## Project goals
- Upload receipt images.
- Extract product data from images.
- Match products to a known catalog.
- Save purchase history over time.
- Suggest specials and likely repeat purchases.
- Show purchase patterns in a dashboard.

---

## Current repository structure
The project already has these major components:

- backend/ for API logic
- frontend/ for the React UI
- each side should remain separate for maintainability

---

## Recommended folder structure

```text
purchase-predictor/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── receipt_routes.py
│   │   │   │   └── recommendation_routes.py
│   │   │   └── deps.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── models/
│   │   │   ├── customer.py
│   │   │   ├── product.py
│   │   │   ├── receipt.py
│   │   │   └── recommendation.py
│   │   ├── schemas/
│   │   │   ├── receipt.py
│   │   │   ├── product.py
│   │   │   └── recommendation.py
│   │   ├── services/
│   │   │   ├── ocr_service.py
│   │   │   ├── receipt_parser.py
│   │   │   ├── product_matcher.py
│   │   │   └── recommendation_service.py
│   │   └── main.py
│   ├── tests/
│   │   ├── test_receipt_parser.py
│   │   └── test_recommendations.py
│   ├── uploads/
│   │   └── receipts/
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── upload/
│   │   │   ├── dashboard/
│   │   │   └── cards/
│   │   ├── pages/
│   │   │   ├── HomePage.jsx
│   │   │   ├── ReceiptUploadPage.jsx
│   │   │   └── DashboardPage.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── hooks/
│   │   │   └── useReceipts.js
│   │   ├── styles/
│   │   │   └── app.css
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── planning/
│   └── implementation-plan.md
├── README.md
├── .gitignore
├── docker-compose.yml
└── .env.example
```

---

## Phase 1: Project setup and connection

### Goal
Get the frontend and backend talking to each other reliably.

### Tasks
- standardize local ports
- fix frontend/backend CORS settings
- confirm health endpoint works
- set up environment variables for API base URL and database credentials
- create a minimal README for setup instructions

### Output
- backend server runs successfully
- frontend makes API requests successfully
- app is ready for feature work

---

## Phase 2: Receipt upload flow

### Goal
Allow a user to upload a receipt image.

### Tasks
- Add a file upload endpoint in backend
- validate image file type
- save raw image to uploads/receipts
- return upload status to frontend
- create upload UI in frontend
- allow preview of selected image before submission

### Backend responsibilities
- accept image file
- save the image
- return metadata such as filename and status

### Frontend responsibilities
- show file picker
- upload image
- display success or error message

### Output
- receipt upload works end-to-end

---

## Phase 3: OCR and parsing

### Goal
Convert image text into structured purchase data.

### Tasks
- integrate OCR provider
- extract text from uploaded receipt
- parse lines into:
  - product name
  - quantity
  - unit price
  - total
  - category hint if possible
- clean noisy OCR output
- store parsed receipt line items

### Example parsed output
```json
[
  {
    "product_name": "Milk 2L",
    "quantity": 1,
    "unit_price": 32.5,
    "total": 32.5,
    "category": "dairy"
  }
]
```

### Output
- raw receipt text becomes structured item data ready for matching and storage

---

## Phase 4: Product catalog and matching

### Goal
Match OCR results to known products.

### Tasks
- create product catalog model
- include fields like:
  - id
  - name
  - category
  - brand
  - sku
  - barcode
  - aliases
- normalize OCR strings
- match using:
  - exact match
  - fuzzy match
  - category heuristics
  - brand heuristics
- assign confidence score for uncertain matches

### Output
- parsed receipt items become recognized products
- uncertain items can be manually reviewed later

---

## Phase 5: Purchase history tracking

### Goal
Track what was bought over time.

### Tasks
- create database tables for:
  - customers
  - products
  - receipts
  - receipt_items
  - purchase_history
  - recommendations
- capture timestamp, total spend, and item list for each receipt
- aggregate repeated purchases by customer and category
- compute:
  - purchase frequency
  - recency
  - item affinity
  - category preference
  - basket size

### Output
- each customer has a purchase history that can be analyzed for trends

---

## Phase 6: Recommendation engine

### Goal
Suggest specials and bundles based on customer behaviour.

### Tasks
- build a recommendation service
- use rules such as:
  - frequently purchased products
  - products bought together
  - category-based promotions
  - recency-based reminders
  - active specials matching purchase history
- rank recommendations by relevance
- return result payload to frontend

### Example recommendation payload
```json
{
  "item": "Bread",
  "reason": "You buy this every week",
  "discount": "10% off",
  "confidence": 0.89
}
```

### Output
- personalized suggestions shown in a recommendations panel

---

## Phase 7: Dashboard and user experience

### Goal
Make the app useful and understandable to the user.

### UI features
- recent purchase history
- top categories
- frequent purchases
- special offers
- bundle recommendations
- “why this suggestion?” explanation text

### Pages
- Home or dashboard page
- receipt upload page
- purchase history page
- recommendation page

### Output
- store or customer can understand the app’s recommendations and trends

---

## Phase 8: Testing and validation

### Goal
Confirm the accuracy and stability of the MVP.

### Test focus areas
- OCR on different receipt styles
- product matching on similar item names
- recommendation relevance based on historical purchase behaviour
- data consistency after multiple uploads
- upload + parse + store + recommend end-to-end flow

### Output
- working MVP with confidence in the core features

---

## Phase 9: MVP release and future improvements

### MVP should include
- upload receipt image
- parse receipt line items
- match items to products
- keep purchase history
- suggest specials based on purchase history
- show dashboard summary

### Later improvements
- customer login and loyalty management
- better product matching rules
- richer recommendation model
- notification system for active promotions
- mobile app or camera-first UX
- integration with retailer POS or ERP systems

---

## Implementation order
The recommended delivery sequence is:

1. fix frontend/backend connection
2. set up upload API
3. OCR and receipt parsing
4. product matching
5. database and purchase tracking
6. recommendation logic
7. dashboard UI
8. testing and polish

---

## Recommended first sprint

### Sprint 1 goals
- backend runs locally
- frontend can upload receipt files
- OCR converts image text into usable data
- item data is saved in memory or database
- a basic recommendation example is returned

### Success criteria
- User uploads a receipt image successfully
- one or more products are extracted
- app provides a recommendation based on sample customer history

---

## Risk areas to monitor
- OCR accuracy on low-quality receipt photos
- inconsistent product names between receipts and catalog
- duplicate or noisy line items
- recommendation ranking not being meaningful enough
- too much complexity before the MVP is complete

---

## Final recommendation
Keep the architecture simple for the first version:
- React frontend
- FastAPI backend
- Postgres database
- OCR-based receipt parsing
- rule-based recommendation engine

This is the fastest route to a working proof of concept without building unnecessary complexity too early.
