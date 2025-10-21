# RootStriker | Cybersecurity Writeups

A clean, professional website to showcase your cybersecurity writeups from GitHub.

## Features

- 🔍 Search and filter writeups by name and category
- 📁 Organized by categories and subcategories
- 🌙 Dark theme interface
- 🔄 Automatic updates via GitHub Actions
- 📝 GitHub-style markdown rendering

## Setup Instructions

### 1. Configure GitHub Repository

Open `index.html` and update these variables (around line 1123):

```javascript
const GITHUB_USER = '0xStr1k3r';           // Your GitHub username
const GITHUB_REPO = 'your-repo-name';      // Your repository name
const GITHUB_BRANCH = 'main';               // Your default branch (main or master)
```

**Example:**
If your repository is `https://github.com/0xStr1k3r/writeups`, then:
```javascript
const GITHUB_USER = '0xStr1k3r';
const GITHUB_REPO = 'writeups';
const GITHUB_BRANCH = 'main';
```

### 2. Add Your Writeups

1. Create your markdown files in organized directories:
   ```
   TryHackMe/
   ├── Soc-1/
   │   ├── Mod-4/
   │   │   ├── Sysinternals.md
   │   │   ├── Wazuh.md
   │   │   └── Windows Event Logs.md
   │   └── mod-6 Digital Forensics and Incident Response/
   │       ├── Critical.md
   │       └── Unattended.md
   └── sample.md
   ```

2. The website will automatically detect and display all `.md` files

### 3. Update files.json

The GitHub Actions workflow automatically updates `files.json` when you push changes. You can also manually update it:

```bash
python3 update_files.py
```

### 4. Deploy to GitHub Pages

1. Go to your repository settings
2. Navigate to Pages section
3. Select your branch (main/master)
4. Save

Your site will be available at: `https://yourusername.github.io/repository-name/`

## File Structure

```
.
├── index.html              # Main website file
├── files.json              # Auto-generated file list
├── update_files.py         # Script to update files.json
├── sample.md               # Example writeup
├── .github/
│   └── workflows/
│       └── update-files.yml  # Auto-update workflow
├── Images/                 # Image assets
└── TryHackMe/              # Your writeups organized by platform
```

## Customization

### Social Links

Update the footer links in `index.html` (around line 1105):

```html
<a href="https://github.com/0xStr1k3r" target="_blank">🐙 GitHub</a>
<a href="https://linkedin.com/in/your-profile" target="_blank">💼 LinkedIn</a>
<a href="mailto:your.email@example.com">📧 Email</a>
<a href="https://your-portfolio.com" target="_blank">🌐 Portfolio</a>
```

### Theme

The website uses a dark cyberpunk theme. You can customize colors in the CSS section of `index.html`.

## How It Works

1. **Automatic Updates**: When you push new .md files, GitHub Actions runs `update_files.py` to update `files.json`
2. **File Discovery**: The website reads `files.json` to display all available writeups
3. **GitHub Rendering**: Clicking "View" opens the markdown file using GitHub's native renderer
4. **Search & Filter**: Users can search and filter writeups by name and category

## Troubleshooting

### Markdown files not displaying?
- Make sure `GITHUB_USER`, `GITHUB_REPO`, and `GITHUB_BRANCH` are correctly set in `index.html`
- Verify your repository is public or you have proper access
- Check that `files.json` is being generated correctly

### GitHub Actions not running?
- Make sure the workflow file is in `.github/workflows/update-files.yml`
- Check that you have Actions enabled in your repository settings
- Verify the workflow triggers on push to your main branch

### Website not loading?
- Ensure GitHub Pages is enabled in repository settings
- Check that `index.html` is in the root directory or docs folder (depending on your Pages configuration)
- Wait a few minutes after pushing changes for Pages to rebuild

## License

© 2024 RootStriker. All rights reserved.