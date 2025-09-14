# Ubuntu_Requests

> "I am because we are" – Ubuntu Philosophy 🌍

## 🌐 Overview

This project is a respectful, community-centered Python script designed to fetch images from the internet and save them locally. It embodies the Ubuntu principles of:

- **Community**: Connecting with the global web
- **Respect**: Gracefully handling errors
- **Sharing**: Organizing fetched images for reuse
- **Practicality**: A simple tool that solves a real-world problem

## 🧰 Features

- Prompts user for an image URL
- Creates a `Fetched_Images` folder (if not present)
- Downloads the image using `requests`
- Extracts a filename or generates one
- Saves the image in binary mode
- Gracefully handles HTTP and connection errors

## 🐍 Requirements

- Python 3.x
- `requests` library

Install `requests`:

```bash
pip install requests
