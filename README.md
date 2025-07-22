# Developer Profile Project

A complete developer profile website with FastAPI backend and HTML/CSS/JS frontend.

## Features
- Responsive profile page
- Contact form with backend storage
- Easy customization
- Ready for deployment

## Setup Instructions

1. Clone the repository
2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Run the development server:
```bash
uvicorn main:app --reload
```

4. Access the application at:
```
http://localhost:8000
```

## Deployment Options

### Option 1: Render.com
1. Create new Web Service
2. Connect your GitHub repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn main:app --host 0.0.0.0 --port 8000`
5. Deploy!

### Option 2: Docker
1. Build the image:
```bash
docker build -t profile-app .
```

2. Run the container:
```bash
docker run -d -p 8000:8000 profile-app
```

## Customization Guide
1. Replace placeholder profile photo in `/static/assets/`
2. Update personal details in `templates/index.html`
3. Modify colors in `static/css/styles.css`
4. Add your projects in the projects section
5. Update social media links in footer
# profile
