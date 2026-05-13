# Git Setup Commands

Run these in order to create the repo and push it to GitHub.

```bash
# 1. Navigate to the repo
cd ~/smbforge-agentic-workflows

# 2. Initialize git
git init

# 3. Create .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
.env
.venv/

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo

# Screenshots (large files — add manually if needed)
media/*.png
media/*.jpg
media/*.jpeg
EOF

# 4. Add all files
git add -A

# 5. Commit
git commit -m "Initial commit: SMB Forge agentic workflows — production multi-agent AI system for service business automation

- Multi-agent architecture: SMS, voice, onboarding, quality monitoring
- 3-journey conversation model: booking, ordering, escalation
- Human-in-the-loop via Telegram owner bot
- Full docs: architecture, booking flow, invoicing, production metrics
- MIT License
- Safe, abstracted code examples — no secrets, no PII"

# 6. Create GitHub repo
gh repo create smbforge-agentic-workflows \
  --public \
  --description "Production multi-agent AI system that serves as the full back office for service businesses (plumbers, electricians, cleaners, etc.). Autonomous SMS/Telegram agents handle 24/7 call answering, booking, ordering, invoicing, and owner escalation." \
  --homepage https://smbforge.com \
  --license MIT \
  --push

# 7. Add topics
gh repo edit linmichael123/smbforge-agentic-workflows \
  --add-topic ai-agents \
  --add-topic agentic-ai \
  --add-topic multi-agent \
  --add-topic llm-workflows \
  --add-topic production-ai \
  --add-topic smb-automation \
  --add-topic google-calendar-integration \
  --add-topic telegram-bot \
  --add-topic autonomous-workflows

# 8. Verify
echo "✅ Repo created: https://github.com/linmichael123/smbforge-agentic-workflows"
echo "   Live at: smbforge.com"
echo "   Demo: Call/text (949) 565-1908"
```

## After Setup — Take Screenshots

Once the repo is live, add screenshots to the `/media` folder per the instructions in `media/README.md`. The README currently has embedded Mermaid diagrams that render beautifully, but real screenshots make it pop for hiring managers.

## Live URL

After running the commands above:
**https://github.com/linmichael123/smbforge-agentic-workflows**
