"""
runserver.py
-----
The main script to start guruxone-server
"""

import uvicorn


def main():
    uvicorn.run(
        "guruxone.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
