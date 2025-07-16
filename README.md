# Hotwire Turbo Demo

A Flask web application demonstrating the core features of [Hotwire Turbo](https://turbo.hotwired.dev/), a JavaScript framework for building fast, interactive web applications without writing custom JavaScript.

## Purpose

This project showcases key Hotwire Turbo concepts through practical examples:

- **Turbo Frames**: Update specific parts of the page without full page reloads
- **Turbo Streams**: Push real-time updates to the client
- **Interactive Forms**: Handle form submissions seamlessly
- **Dynamic Content**: Live time updates and counter functionality

## Features

### Live Time Updates
Click to fetch the current server time using Turbo Frames for partial page updates.

### Interactive Counter
Increment and reset a counter with state management handled server-side.

### Form Handling
Submit forms with Turbo Frame responses that update specific page sections.

### Turbo Streams
Add items to a list using Turbo Streams for real-time content updates.

## Getting Started

### Prerequisites
- Python 3.7+
- Flask

### Installation
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install flask
```

### Running the Application
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate   # On Windows

python app.py
```

The application will start on `http://localhost:5001`

## Project Structure

```
hotwire_test
├── app.py
├── README.md
└── templates
    ├── index.html
    └── partials
        ├── counter.html
        ├── time.html
        └── turbo_stream.html
```

## Key Components

- **app.py**: Flask backend with routes for time, counter, forms, and streaming
- **templates/index.html**: Frontend demonstrating Turbo Frames and Streams
- **Turbo Integration**: Uses Hotwire Turbo 7.3.0 via CDN

## Further Reading

- [Hotwire Turbo Documentation](https://turbo.hotwired.dev/)
- [Turbo Frames Guide](https://turbo.hotwired.dev/handbook/frames)
- [Turbo Streams Guide](https://turbo.hotwired.dev/handbook/streams)
- [Flask Documentation](https://flask.palletsprojects.com/)
