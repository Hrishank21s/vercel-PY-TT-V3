
# api/app.py
from test_full import TableTracker

# Create app instance
tracker = TableTracker()
app = tracker.app  # Vercel looks for a variable named "app"

# IMPORTANT:
# Do NOT call app.run() or start threads here.
# Your background thread code in TableTracker may not run in Vercel serverless,
# but the routes will still function.
