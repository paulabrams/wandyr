# Wåndyr Interactive

A Jekyll-based website for the Wåndyr adventure game, featuring interactive tools and automatically generated links to all available markdown tables.

## Features

- **Interactive Game Tools**: Insight roller and Oracle dice roller
- **Automatic Table Discovery**: Automatically finds and links to all markdown tables in the `markdown/tables/` directory
- **Responsive Design**: Modern, mobile-friendly interface
- **Jekyll Integration**: Easy to maintain and update

## Quick Start

### Prerequisites

- Ruby (2.7 or higher)
- Python 3
- Bundler gem

### Installation

1. **Clone or download this repository**
2. **Install dependencies**:
   ```bash
   bundle install
   ```
3. **Build the site**:
   ```bash
   ./build.sh
   ```
4. **Serve locally** (optional):
   ```bash
   bundle exec jekyll serve
   ```

## How It Works

### Automatic Table Discovery

The build process automatically scans the `markdown/tables/` directory and creates Jekyll collection items for each markdown file. This means:

- **No manual linking required**: New tables are automatically discovered and linked
- **Automatic categorization**: Tables are categorized based on their directory structure
- **Rich metadata**: Titles and descriptions are extracted from markdown content

### File Structure

```
wandyr/
├── _config.yml          # Jekyll configuration
├── _layouts/            # HTML layouts
├── _includes/           # Reusable components
├── _tables/             # Auto-generated table collection (created by build script)
├── markdown/tables/     # Source markdown files
├── scripts/             # Build automation scripts
├── build.sh             # Automated build script
└── index_interactive_jekyll.md  # Main page content
```

### Adding New Tables

1. **Place your markdown file** in the `markdown/tables/` directory (or any subdirectory)
2. **Run the build script**:
   ```bash
   ./build.sh
   ```
3. **The table is automatically linked** in the main page

### Customization

- **Styling**: Edit `_includes/styles.html` to modify the appearance
- **Layout**: Modify `_layouts/default.html` to change the page structure
- **Scripts**: Update `_includes/scripts.html` to modify interactive functionality

## Build Process

The `build.sh` script performs these steps automatically:

1. **Dependency Check**: Ensures Ruby, Python 3, and Jekyll are available
2. **Table Generation**: Runs `scripts/generate_tables.py` to create Jekyll collection items
3. **Site Build**: Executes `bundle exec jekyll build`
4. **Output**: Creates the built site in the `_site/` directory

## Development

### Local Development

```bash
# Start local development server
bundle exec jekyll serve

# Build for production
./build.sh
```

### Adding New Features

1. **Interactive Tools**: Add new tools to the `tools-section` in `index_interactive_jekyll.md`
2. **Styling**: Add CSS to `_includes/styles.html`
3. **Functionality**: Add JavaScript to `_includes/scripts.html`

## Troubleshooting

### Common Issues

- **Build fails**: Check that all dependencies are installed (`bundle install`)
- **Tables not appearing**: Ensure markdown files are in the `markdown/tables/` directory
- **Styling issues**: Verify that `_includes/styles.html` is properly formatted

### Dependencies

- **Jekyll**: `~> 4.3.0`
- **Jekyll Sitemap**: For SEO optimization
- **Jekyll SEO Tag**: For better search engine optimization

## License

Copyright © 2025 Paul Abrams. All rights reserved.

---

For more information about Wåndyr, see the game documentation in the `docs/` directory. 