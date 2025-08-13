#!/bin/bash

# Wåndyr Jekyll Build Script
# This script automatically generates Jekyll collection items from markdown tables
# and builds the site

echo "🚀 Starting Wåndyr build process..."

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Check if Ruby and Jekyll are available
if ! command -v ruby &> /dev/null; then
    echo "❌ Ruby is required but not installed."
    echo "Please install Ruby and try again."
    exit 1
fi

if ! command -v jekyll &> /dev/null; then
    echo "📦 Installing Jekyll..."
    gem install jekyll bundler
fi

# Install dependencies
echo "📦 Installing Jekyll dependencies..."
bundle install

# Generate Jekyll collection items from markdown tables
echo "🔧 Generating Jekyll collection items from markdown tables..."
python3 scripts/generate_tables.py

# Build the Jekyll site
echo "🏗️  Building Jekyll site..."
bundle exec jekyll build

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "✅ Build completed successfully!"
    echo "📁 Site built in _site/ directory"
    echo "🌐 You can serve the site with: bundle exec jekyll serve"
else
    echo "❌ Build failed. Please check the error messages above."
    exit 1
fi

echo "🎉 Wåndyr build process complete!" 