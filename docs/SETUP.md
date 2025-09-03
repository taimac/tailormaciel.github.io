# Personal Website & Knowledge Base - Quick Setup Guide
## File-Based Knowledge System with Minimal Backend

This setup implements the **hybrid architecture** from the README: file-based content with optional minimal backend for authentication.

## 🎯 Architecture Overview

```
📁 Content Layer (Files + Metadata)
├── content/public/     → Static files (no auth needed)
├── content/private/    → Protected files (auth required)
└── .metadata.json      → Content descriptions & connections

🎨 Frontend (Static)
├── File explorer with OOP components
├── Search engine with multiple strategies
├── Knowledge graph visualization
└── Authentication UI

⚙️ Backend (Optional - 3 endpoints only)
├── POST /api/auth/login
├── GET /private/<file>
└── POST /api/auth/logout
```

## 🚀 Quick Start

### Option A: Pure Static (5 minutes)
```bash
# 1. Create project structure
mkdir personal-website && cd personal-website
mkdir -p content/{public,private}/{computer-science,mathematics,projects}
mkdir -p frontend/{js/{components,services,models},styles,assets}
mkdir -p docs scripts

# 2. Create sample content structure
cd content/public/computer-science
mkdir data-structures algorithms web-development
echo '{"title": "Computer Science", "tags": ["cs", "programming"]}' > .metadata.json

# 3. Basic frontend files
cd ../../../frontend
echo '<!DOCTYPE html>
<html><head><title>Knowledge Base</title></head>
<body>
  <div id="app">Loading...</div>
  <script type="module" src="js/main.js"></script>
</body></html>' > index.html

# 4. Start static server
python -m http.server 3000
# Visit: http://localhost:3000
```

### Option B: With Authentication Backend (15 minutes)
```bash
# Steps 1-3 from above, then:

# 4. Create minimal Flask backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install flask pyjwt python-dotenv

# 5. Create minimal backend
echo 'from flask import Flask, request, jsonify, send_file
from functools import wraps
import jwt
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "demo-secret-key"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if not token or token == "demo-token":
            return f(*args, **kwargs)  # Demo mode
        return {"error": "Invalid token"}, 401
    return decorated

@app.route("/api/auth/login", methods=["POST"])
def login():
    data = request.json
    if data.get("username") == "demo" and data.get("password") == "demo123":
        return {"success": True, "token": "demo-token", "user": {"username": "demo"}}
    return {"error": "Invalid credentials"}, 401

@app.route("/private/<path:filename>")
@token_required
def serve_private(filename):
    return send_file(f"../content/private/{filename}")

if __name__ == "__main__":
    app.run(debug=True, port=5000)' > app.py

# 6. Start both servers
python app.py &  # Backend on :5000
cd ../frontend && python -m http.server 3000  # Frontend on :3000
```

## 📁 Project Structure

```
personal-website/
├── content/                    # File-based knowledge system
│   ├── public/                 # Static content (GitHub Pages ready)
│   │   ├── computer-science/
│   │   ├── mathematics/
│   │   └── projects/
│   └── private/                # Auth-protected content
│       ├── work-projects/
│       └── personal-research/
│
├── frontend/                   # Static web app
│   ├── index.html              # Main entry point
│   ├── styles/                 # CSS architecture
│   ├── js/                     # ES6+ modules
│   │   ├── components/         # UI components (OOP)
│   │   ├── services/           # Business logic
│   │   └── main.js            # App bootstrap
│   └── assets/                # Static resources
│
├── backend/                   # Optional minimal Flask
│   ├── app.py                 # 3 endpoints only
│   ├── requirements.txt       # flask, pyjwt
│   └── .env                   # Secrets
│
└── docs/                      # Documentation
    ├── project_backlog.md
    └── learning_progress.md
```

## 🔧 Key Implementation Files

### 1. Content Metadata System
Each folder gets a `.metadata.json`:
```json
{
  "title": "Data Structures",
  "description": "CS fundamentals",
  "tags": ["cs", "algorithms"],
  "files": [
    {"name": "arrays.pdf", "type": "notes", "created": "2024-01-15"}
  ],
  "connections": [
    {"to": "../algorithms", "relationship": "prerequisite", "strength": 0.9}
  ]
}
```

### 2. Frontend Architecture (ES6 Modules)
```javascript
// js/main.js - App bootstrap
import { FileExplorer } from './components/FileExplorer.js';
import { SearchEngine } from './components/SearchEngine.js';
import { FileSystemService } from './services/FileSystemService.js';

class App {
  async init() {
    this.fileSystem = new FileSystemService();
    this.explorer = new FileExplorer(this.fileSystem);
    await this.explorer.navigateToPath('content/public');
  }
}

// js/services/FileSystemService.js - File operations
export class FileSystemService {
  async listDirectory(path) {
    // Parse .metadata.json + simulate directory listing
  }
  
  async getFileContent(filePath) {
    // Fetch and return file content by type
  }
}

// js/components/FileExplorer.js - Main UI component  
export class FileExplorer {
  constructor(fileSystemService) {
    this.fileSystem = fileSystemService;
  }
  
  async navigateToPath(path) {
    // Update breadcrumb, load content, render grid
  }
}
```

### 3. Minimal Backend (Optional)
```python
# backend/app.py - Only essential endpoints
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route('/api/auth/login', methods=['POST'])
def login():
    # Validate credentials, return JWT
    
@app.route('/private/<path:filename>')  
@token_required
def serve_private_file(filename):
    # Serve protected files only to authenticated users
```

## 🎓 Educational Progression

### Phase 1: Static Foundation (Week 1)
- [x] File-based content structure
- [x] Metadata system for connections
- [x] Basic file explorer with OOP
- [x] Static file serving

### Phase 2: Interactive Features (Week 2)
- [ ] Search with multiple strategies (Strategy pattern)
- [ ] Knowledge graph visualization
- [ ] Modal components (inheritance demo)
- [ ] Responsive design

### Phase 3: Authentication (Week 3) 
- [ ] Minimal Flask backend setup
- [ ] JWT authentication flow
- [ ] Private content protection
- [ ] Security best practices

### Phase 4: Polish & Deploy (Week 4)
- [ ] Performance optimization
- [ ] Error handling & validation
- [ ] Testing strategy
- [ ] Deployment (static + optional backend)

## 🚢 Deployment Options

### Static Only (GitHub Pages, Netlify)
```bash
# Deploy frontend/ folder as static site
# Perfect for public knowledge bases
```

### Hybrid Deployment
```bash
# Frontend: Static hosting (fast, cached)
# Backend: Railway/Render/Heroku (for auth)
# Best of both worlds
```

## 🔍 Why This Architecture?

**File-Based Benefits:**
- ✅ Version controlled content
- ✅ No database complexity  
- ✅ Portable and readable
- ✅ Easy backup and migration

**Hybrid Benefits:**
- ✅ Public content serves fast (static)
- ✅ Private content truly secure (backend)
- ✅ Can evolve complexity gradually
- ✅ Learn when to use simple vs complex solutions

## 🎯 Learning Objectives

- **OOP Principles**: FileExplorer, SearchService classes demonstrate encapsulation
- **Design Patterns**: Strategy (search), Observer (events), Service Layer 
- **Clean Architecture**: Services → Components → UI layers
- **Security**: Authentication, file access control, input validation
- **Progressive Enhancement**: Static → Dynamic → Authenticated

---

**Start with Option A (static) to understand the file-based architecture, then add Option B (backend) when you need private content protection.**

# Setup Guide (B01 — Hybrid Project Structure & Setup)

Purpose:
- Provide reproducible minimal setup for local development without Docker.
- Keep public content on static server; private content served by backend.

Prerequisites:
- Python 3.8+
- Git
- (Optional) pip and virtualenv for backend Python

Quick start (frontend only):
1. Serve frontend:
   ```bash
   cd frontend
   python3 -m http.server 3000
   ```
2. Open http://localhost:3000 in your browser and verify `index.html` and favicon load.

Backend (minimal stub):
1. Create and activate venv:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements.txt
   ```
2. Run backend (Flask placeholder):
   ```bash
   cd backend
   python -m flask run --port 5000
   ```
3. Verify /health or /api endpoints.

Project layout (verified for B01):
- content/public  — public files (committed)
- content/private — private files (gitignored)
- frontend        — static pages, assets, JS, CSS
- backend         — minimal Flask app (auth + private serving)
- scripts         — utilities (graph/metadata generation)
- docs            — backlog, ADRs, setup

Commit checklist (post-change):
- [ ] Update docs/backlog.md to reflect progress
- [ ] Commit docs/SETUP.md and .gitignore
- [ ] Push feature branch and open PR targeting `dev`