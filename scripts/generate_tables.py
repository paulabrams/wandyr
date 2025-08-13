#!/usr/bin/env python3
"""
Script to automatically generate Jekyll collection items from markdown tables.
This script scans the markdown/tables directory and creates Jekyll collection items
with proper front matter for automatic linking.
"""

import os
import re
import glob
from pathlib import Path

def extract_title_from_markdown(content):
    """Extract title from markdown content (first # heading)"""
    lines = content.split('\n')
    for line in lines:
        if line.strip().startswith('# '):
            return line.strip()[2:].strip()
    return None

def extract_description_from_markdown(content):
    """Extract description from markdown content (first paragraph after title)"""
    lines = content.split('\n')
    title_found = False
    for line in lines:
        line = line.strip()
        if line.startswith('# '):
            title_found = True
            continue
        if title_found and line and not line.startswith('#') and not line.startswith('---'):
            # Clean up markdown formatting
            clean_line = re.sub(r'[#*`\[\]]', '', line)
            clean_line = re.sub(r'!\[.*?\]\(.*?\)', '', clean_line)  # Remove image markdown
            clean_line = clean_line.strip()
            if clean_line and len(clean_line) > 10:  # Only return substantial descriptions
                return clean_line[:200] + '...' if len(clean_line) > 200 else clean_line
    return None

def determine_category(filepath):
    """Determine category based on file path"""
    path_parts = Path(filepath).parts
    if 'world-oracle' in path_parts:
        return 'World Oracle'
    elif 'magical-world-oracle' in path_parts:
        return 'Magical World'
    elif 'encounters' in path_parts:
        return 'Encounters'
    elif 'characters' in path_parts:
        return 'Characters'
    elif 'treasure' in path_parts:
        return 'Treasure'
    elif 'equipment' in path_parts:
        return 'Equipment'
    elif 'settlements' in path_parts:
        return 'Settlements'
    elif 'wilderness' in path_parts:
        return 'Wilderness'
    elif 'travel' in path_parts:
        return 'Travel'
    elif 'names' in path_parts:
        return 'Names'
    elif 'npcs' in path_parts:
        return 'NPCs'
    elif 'combat' in path_parts:
        return 'Combat'
    elif 'loot' in path_parts:
        return 'Loot'
    elif 'political' in path_parts:
        return 'Political'
    elif 'rules' in path_parts:
        return 'Rules'
    elif 'starting-game' in path_parts:
        return 'Starting Game'
    else:
        return 'General'

def create_jekyll_collection_item(md_file_path, output_dir):
    """Create a Jekyll collection item from a markdown file"""
    
    # Read the markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract metadata
    title = extract_title_from_markdown(content)
    description = extract_description_from_markdown(content)
    category = determine_category(str(md_file_path))
    
    if not title:
        title = Path(md_file_path).stem.replace('-', ' ').replace('_', ' ').title()
    
    # Create front matter
    front_matter = f"""---
layout: default
title: "{title}"
category: "{category}"
description: "{description or 'Random table for Wåndyr adventures'}"
url: "/tables/{Path(md_file_path).stem}/"
---

{content}
"""
    
    # Create output file
    output_file = output_dir / f"{Path(md_file_path).stem}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(front_matter)
    
    print(f"Created: {output_file}")
    return {
        'title': title,
        'category': category,
        'description': description,
        'url': f"/tables/{Path(md_file_path).stem}/"
    }

def main():
    """Main function to process all markdown tables"""
    
    # Create output directory
    output_dir = Path('_tables')
    output_dir.mkdir(exist_ok=True)
    
    # Find all markdown files in the tables directory
    md_files = glob.glob('markdown/tables/**/*.md', recursive=True)
    
    if not md_files:
        print("No markdown files found in markdown/tables/")
        return
    
    print(f"Found {len(md_files)} markdown files")
    
    # Process each file
    processed_files = []
    for md_file in md_files:
        try:
            result = create_jekyll_collection_item(md_file, output_dir)
            processed_files.append(result)
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nSuccessfully processed {len(processed_files)} files")
    print(f"Output directory: {output_dir.absolute()}")
    
    # Create a summary file
    summary_file = output_dir / 'README.md'
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("# Wåndyr Tables Collection\n\n")
        f.write("This directory contains automatically generated Jekyll collection items from the markdown tables.\n\n")
        f.write("## Available Tables\n\n")
        
        for item in processed_files:
            f.write(f"- **{item['title']}** ({item['category']}) - {item['description']}\n")
    
    print(f"Created summary file: {summary_file}")

if __name__ == "__main__":
    main() 